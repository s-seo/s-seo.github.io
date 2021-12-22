---
layout: default
title:  "Airflow"
parent: Engineering
nav_order: 97
---



Airbnb에서 개발한 open-source workflow management platform for data engineering pipeplines, 즉, workflow scheduling, monitoring tool 이다. 

`Airflow is a platform that lets you build and run workflows. A workflow is represented as a DAG (a Directed Acyclic Graph), and contains individual pieces of work called Tasks, arranged with dependencies and data flows taken into account.`
출처: <https://airflow.apache.org/docs/apache-airflow/stable/concepts/overview.html>

현재는 Apache의 Top-Level Apache Software Foundation project로 자리잡았다. 오픈 소스라 딱히 인수할 것도 없고 그냥 개발한지 2년 후인 16년에 Apache Incubator project가 된 것 같다. (https://en.wikipedia.org/wiki/Apache_Airflow) 깃헙 주소도 있다. (github.com/apache/airflow) 난 Airflow는 batch 관리 시스템 정도로만 알고 있었는데, workflow를 관리하는 도구라...그럼 batch와 workflow 간 차이가 있나? 아니 애초에 workflow란 뭘까? 이건 

Airflow는 파이썬으로 만들어졌고 (깃헙 보면 알 수 있다), pip으로 설치 가능하고, 파이썬 스크립트를 사용해 워크플로우를 정의한다 (DAGs)

Airflow 동작 원리는 다음과 같다.
![](https://s-seo.github.io/assets/images/post_airflow_1.PNG) 
출처: <https://airflow.apache.org/docs/apache-airflow/stable/concepts.html>
Data engineer인 내 입장에서 본다면, 



특성은 dynamic, extensible, elegant, scalable 이다.

특징이라면 Directed Acyclic Graph (DAG) 형식의 workflow다.
- DAG는 network theory 개념이다. workflow라고 명시한 분도 있는데 내 생각에 둘은 엄연히 다른 개념인 것 같다. DAG로 표현, 관리된 workflow라고 말하는게 맞지 않을까?
- 또는, DAG는 일종의 task 집합으로 각 task가 어떤 순서로 실행되는지, 어떤 dependency를 갖는지, 어떤 스케줄로 실행할지 등의 정보를 모아놓은 것.
- Network theory 관점에서 DAG는 단방향 + 비순환 그래프인데, 링크가 한 방향만을 가리키고, 순환하지 않아 시작과 끝이 명시되어 있는 그래프를 일컫는다. 




Amazon MWAA

- Apache Airflow의 managed orchestrationg service 다.
- AWS ECR이 Docker hub의 private repository 구축, 관리를 쉽게 manage하는 서비스인 것과 비슷한 개념
- 크래프톤에선 MWAA를 사용해 airflow를 관리한다. 


Oozie, Azkaban과 같은 DAG-based schedulers도 이전에는 많이 쓰였는데, 이것들은 DAGs를 만들려면 multiple configuration files와 file system trees를 요구하는 반면 Airflow는 파이썬 스크립트 하나면 된다는 차이점이 있다.



