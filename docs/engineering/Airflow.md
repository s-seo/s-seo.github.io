---
layout: default
title:  "Airflow"
parent: Engineering
nav_order: 97
---

DAG를 작성해야 하는 업무가 있었는데, 이 개념을 모르고 쓴다는건 너무 자존심 상해서 아예 Airflow라는 뿌리부터 공부해보려고 한다. Airflow를 다루기 앞서 workflow라는 개념을 알아야하는데, 간단히 정의하자면 아래와 같다. 

> 비효율적으로 반복되는 과정을 개선하기 위해, 각 과정들의 입출력만 표준화하고 각 테스크의 결과에 따른 조건부 처리를 미리 정의하고, 특정 조건에 따른 트리거를 설정하여 모든 과정들을 파이프라인에 맞춰 실행하는 논리 개념

> 출처: <https://blog.si-analytics.ai/59>

그럼 pipeline은 뭐길래 workflow와 구별될까? 좋은 설명이 있는데 pipeline은 a series of processes, usually liner이고 workflow는 a set of processes, usually nonlinear라는 것이다. 일반적으로 pipeline은 workflow 보다 가볍고, command line 같은 느낌이라면 workflow는 방대하고, 더 포괄적인 느낌으로 사용되는데 점차 둘의 경계가 희미해지고 있다. 출처: <https://www.biostars.org/p/17696/> 근데 완전 반대로 정의한 곳도 쉽게 찾아볼 수 있어서 이것도 나중에 따로 포스팅하겠다. 머신러닝 파이프라인을 위해 Argo, Luigi, Kubeflow 등의 다양한 툴이 제공되는데 <https://neptune.ai/blog/best-workflow-and-pipeline-orchestration-tools>, 그 중 pipeline 및 workflow 기능과 많이 사용자를 보유한 (그리고 회사에서 사용하고 있는) Apache Airflow에 대해 알아보겠다.


# Apache Airflow

***

![](https://s-seo.github.io/assets/images/post_airflow_2.PNG) 
> 출처: <https://airflow.apache.org/docs/apache-airflow/stable/concepts/overview.html>

Airbnb에서 개발한 open-source workflow management platform for data engineering pipeplines, 즉, workflow scheduling, monitoring tool 이다. 현재는 Apache의 Top-Level Apache Software Foundation project로 자리잡았다. 오픈 소스라 딱히 인수할 것도 없고 그냥 개발한지 2년 후인 16년에 Apache Incubator project가 된 것 같다. <https://en.wikipedia.org/wiki/Apache_Airflow> 깃헙 레포도 있다. <https://github.com/apache/airflow> 난 Airflow는 batch 관리 시스템 정도로만 알고 있었는데, workflow를 관리하는 도구라...그럼 batch와 workflow 간 차이가 있나? 아니 애초에 workflow란 뭘까? 간단히 생각하면 batch는 타켓이 데이터고, workflow는 분석, 모델링 등 전반을 아우르는 process라고 생각되는데 이건 <https://s-seo.github.io/docs/engineering/Batch/>에서 다루도록 하자. Airflow는 파이썬으로 만들어졌고 (깃헙 보면 알 수 있다), pip으로 설치 가능하고, 파이썬 스크립트를 사용해 워크플로우를 정의한다. 실무에서도 사용하고 있기 때문에 직접 코드를 짜서 실습까지 해보자. Airflow는 아래와 같은 특징이 있다.

- Dynamic : Airflow pipeline(동작순서, 방식)을 python을 이용해 구성하기 때문에 동적인 구성이 가능
- Extensible : python을 이용해 Operator, executor을 사용해 사용자 환경에 맞게 확장 사용 가능
- Elegant : 간결하고 명시적이며 jinja template를 이용해 parameter를 이용해 데이터를 전달하고 파이프라인을 생성하는 것이 가능
- Scalable : 분산구조와 메세지큐를 이용해 scale out와 워커간 협업을 지원
> 출처: <https://dydwnsekd.tistory.com/27?category=897626>


Airflow 동작 원리는 다음과 같다.

![](https://s-seo.github.io/assets/images/post_airflow_1.PNG) 
> 출처: <https://airflow.apache.org/docs/apache-airflow/stable/concepts.html>

![](https://s-seo.github.io/assets/images/post_airflow_3.PNG) 
> 출처: <https://airflow.apache.org/docs/apache-airflow/stable/concepts.html>

위는 Apache Airflow 공식 사이트에서 따온 것이고, 아래는 같은 개념인데 좀 더 직관적인 그림이다. 상단에 있는 airflow.cfg는 Airflow의 Configuration 파일로 깃헙 페이지하면서 수없이 건드렸던 그 config 파일과 같은 역할을 한다. 하단에 나와있듯이 Airflow는 Directed Acyclic Graph (DAG) 형식의 workflow를 지원한다. DAG는 network theory 개념이다. workflow라고 명시한 분도 있는데 내 생각에 둘은 엄연히 다른 개념인 것 같다. DAG로 표현, 관리된 workflow라고 말하는게 맞지 않을까?

> Airflow is a platform that lets you build and run workflows. A workflow is represented as a DAG (a Directed Acyclic Graph), and contains individual pieces of work called Tasks, arranged with dependencies and data flows taken into account.

> 출처: <https://airflow.apache.org/docs/apache-airflow/stable/concepts/overview.html>

또는, DAG는 일종의 task 집합으로 각 task가 어떤 순서로 실행되는지, 어떤 dependency를 갖는지, 어떤 스케줄로 실행할지 등의 정보를 모아놓은 것이다. Network theory 관점에서 DAG는 단방향 + 비순환 그래프인데, 링크가 한 방향만을 가리키고, 한 번 통과한 노드는 다시 통과하지 않아 시작과 끝이 다른 그래프를 일컫는다. 대학원 강의 때 들었던 개념이 이런 engineering에서 나오니까 신기하면서 반갑다.  

Engineer가 하는 작업은 주로 DAGs 스크립트를 작성하거나, Web server에 접속해서 DAGs와 task를 inspect, trigger, debug 한다. DAHs로 표현된 워크플로우(py)를 정의하고, 프롬프트에서 `airflow scheduler`를 실행하면 DAGs가 등록된다. 그리고 웹서버에 접속하면 내가 올린 DAG가 잘 등록되어 있는 것을 확인 가능하다. 그럼 Scheduler가 Meta DB에 저장된 Task에 대한 정보(스케줄, 상태)를 관리하고 정해진 스케줄에 맞춰 task를 Executor에 전달한다. 만약 내가 workflow를 만들고 싶다면 task를 짜는 것이 가장 기본 작업이다. Task는 하나의 작업 단위를 일컫으며 여러 Task를 묶어 하나의 DAG를 생성한다. Task 간에는 순서를 >>로 지정할 수 있다. Task는 Operator로 만들 수 있다. 그럼 Operator는 뭐길래? Task를 만들기 위해 사용되는 Airflow class다. `BashOperator`, `PythonOperator` 등 여러 Operator가 제공된다. 직접 Operator를 생성할 수도 있다. <https://dydwnsekd.tistory.com/28> Executor는 task 수행에 필요한 worker process를 실행한다. 이 때, Executor의 종류에 따라 Worker의 동작 방식이 다양하다. Executore 간단한 예시는 아래와 같다.

- SequentialExector (default): task 순차 처리 / SQLite3를 backend로 설정 / TEST로 사용 권장
- LocalExecutor: task 병렬 처리 가능 / MySQL이나 PostgreSQL을 backend로 설정 / task마다 subprocess를 생성
- CeleryExecutor: task를 여러 서버(node)에 분산 처리 가능 (cluster) / Celery backend (RabbitMQ, Redis, …) 설정이 필요
- DaskExecutor: Celery와 같은 역할이지만 Dask로 처리
- KubernetesExecutor: Kubernetes로 cluster 자원을 효율적으로 관리 가능 / 1.10 버전부터 지원
> 출처: <https://yahwang.github.io/posts/airflow>

그럼 Airflow를 실제로 사용해보려면 뭘 해야할까? 일단 회사에선 접속은 바로 된다. 근데 Airflow를 아직 내가 직접 사용해보진 않았으니까 어떤 프로그램을 미리 설치해야 하고, 어떻게 작동시키는지 알아보겠다. 당연히 Airflow를 설치해야하고, 메타데이터 저장을 위한 MySQL과 Celery backend를 제공하는 Redis가 필요하다. Docker container 기반으로 설치할 수 있다. <https://blog.si-analytics.ai/59> 설치가 끝나면 `airflow webserver`를 입력하면 airflow가 실행된다. 그럼 workflow를 만들어서 실행시킬 수 있다. 여기서 앞에 나온 DAG 개념이 나오는데, 아래와 같이 dag 스크립트를 작성하면 된다. 작성한 DAG 스크립트는 airflow.cfg에서 설정한 경로에 저장하면 된다.


```python
# 출처: https://blog.si-analytics.ai/59
from airflow import models
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
 
default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2020, 2, 9),
        'retries': 1,
        'retry_delay': timedelta(minutes=5)}
 
with models.DAG(
        dag_id='echo_test', description='echo_test',
        schedule_interval=None,
        max_active_runs=5,
        concurrency=10,
        default_args=default_args) as dag:
 
    text_file_path = '/root/airflow/dags'
 
    #### create txt file  --> 텍스트 파일을 생성합니다
    create_text_file_command = f'cd {text_file_path} && echo hello airflow > test.txt'
    create_text_file = BashOperator(
            task_id='create_text_file',
            bash_command=create_text_file_command,
            dag=dag)
 
    #### cat txt file  --> 텍스트 파일을 읽습니다
    read_text_file_command = f'cd {text_file_path} && cat test.txt'
    read_text_file = BashOperator(
            task_id='cat_text_file',
            bash_command=read_text_file_command,
            dag=dag)
 
    #### remove txt file  --> 텍스트 파일을 삭제합니다.
    remove_text_file_command = f'cd {text_file_path} && rm test.txt'
    remove_text_file = BashOperator(
            task_id='remove_text_file',
            bash_command=remove_text_file_command,
            dag=dag)
 
    create_text_file >> read_text_file >> remove_text_file  # 이것은 위의 task를 이어주는 줄입니다.
```

위와 같이 구체적인 DAG가 아니라 간단한 DAG는 아래와 같다.

```python
with models.DAG('my_dag', start_date=datetime(2016, 1, 1)) as dag:
    task_1 = DummyOperator('task_1')
    task_2 = DummyOperator('task_2')

    # task_1을 실행한 후 task_2 실행
    task_1 >> task_2 # Define dependencies
```

DAG를 정의하는 방법은 <https://cloud.google.com/composer/docs/how-to/using/writing-dags>, <https://getchan.github.io/data/airflow_2/>에 보다 자세히 나와있다. 이후 `airflow scheduler`를 실행한 뒤 웹서버에 접속하면 아래와 같은 UI가 뜬다.

![](https://s-seo.github.io/assets/images/post_airflow_4.PNG) 
> 출처: <https://airflow.apache.org/docs/apache-airflow/stable/concepts.html>

이게 잘 작동되는건지 확인하려면 해당 task를 클릭한 뒤 `Graph View`를 눌러 worflow가 잘 만들었는지 확인하고 `Trigger DAG`를 눌러 workflow를 실행할 수 있다. 정상적으로 실행되면 박스의 윤곽선이 초록색으로 바뀐다. 아래는 workflow 예시다

![](https://s-seo.github.io/assets/images/post_airflow_5.PNG) 
> 출처: <https://airflow.apache.org/docs/apache-airflow/stable/concepts.html>

![](https://s-seo.github.io/assets/images/post_airflow_6.PNG) 
> 출처: <https://blog.si-analytics.ai/59>

아래는 일반적인 detection + classification의 workflow다. 




# Amazon MWAA

***

회사에서는 MWAA를 사용한다. Amazon Managed Workflows for Apache Airflow의 준말이다. Apache Airflow의 managed orchestrationg service라고 되어 있는데 쉽게 이해하자면 AWS ECR이 Docker hub의 private repository 구축, 관리를 쉽게 manage하는 서비스인 것과 비슷한 개념이다. 이 회사에선 MWAA를 사용해 airflow를 관리한다. AWS에서 관리하면 뭐가 더 좋은건지 대충 이해한 것은

- AWS의 다른 툴과 연동 가능
- S3 저장소에 단순히 DAG를 업로드하면 자동으로 스케줄링되는 것 같음
- 보안이 더 좋겠지 (IAM)

이 외에도 다양한 featuers가 있다. MWAA의 architecture는 아래와 같은데 어렵다.

![](https://s-seo.github.io/assets/images/post_airflow_7.PNG) 
> 출처: <https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html>

VPC는 또 뭐냐...정말 engineering은 꼬리에 꼬리가 물리는 수준을 넘어서 꼬리 하나에 꼬리 백 개가 물리는 지식의 늪이다. MWAA는 추가로 작성하자. 





# 기타

***

- 그럼에도 풀리지 않는 궁금증: 저 위에 airflow는 사내 gitlab 프로젝트 중 하나에 대해 저 workflow를 명시적으로 사용하고 있길래 호기심이 생길 수 있었다. 근데 사내 다른 프로젝트에서는 meta.yaml이란 것만 가지고 dependency를 정의하고, 그 외 스케줄을 뭘로 관리하는지 모르겠다. 이걸 알아야 더 이해할 수 있을 것 같다. 근데 대충 Airflow 사용하는 것 같긴하다. 다만 meta.yaml이 어떻게 작동하는지? 이렇게 작동하는 방식이 일반적인건지? 아니면 회사에서 만든 고유 방식인지?

- Workflow라는 개념이 비단 데이터에만 국한되지 않는 것 같다. <https://ko.myservername.com/20-best-workflow-management-software-2021>를 보면 다양한 workflow 관리 툴이라고 되어 있어서 들어가봤는데 kissflow 등에 대한 사이트 모음이다. 여기서 정의하는 workflow는 비즈니스 프로세스 자동화에 가까운 것 같다. 

- Git에서도 workflow라는 개념이 쓰이는데, git에서 이뤄지는 작업 방식 그 자체를 의미한다. master branch만 사용하면 centralized workflow, branch까지 사용하면 feature branch workflow 등으로 나뉜다. 오픈소스 프로젝트라면 forking workflow로 쓴다는 그런 맥락...

- <https://www.researchgate.net/publication/240947020_Batch_Processing_in_Workflow_the_Model_and_the_Implementation>는 2005년 1월에 Chemical Engineering에 발간된 논문인데 이 때 까지만 해도 batch와 workflow 간 경계가 심했던 것 같다. 

- Oozie, Azkaban과 같은 DAG-based schedulers도 이전에는 많이 쓰였는데, 이것들은 DAGs를 만들려면 multiple configuration files와 file system trees를 요구하는 반면 Airflow는 파이썬 스크립트 하나면 된다는 차이점이 있다.



# 그 외 참고 

***

- <https://yahwang.github.io/posts/airflow>
- <https://www.one-tab.com/page/5RQ5X0laS06OliC6dxNlwQ>




