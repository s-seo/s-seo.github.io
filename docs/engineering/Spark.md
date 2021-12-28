---
layout: default
title:  "Apache Hadoop & Spark"
parent: Engineering
nav_order: 97
---


데이터 사이언스는 business analysis, statistics와 data engineering의 교집합이다. 그래서인지 분석을 하다보면 분산 처리, 병렬 연산 등의 개념을 반드시 마주치게 된다. 이 기회에 저 쪽 개념을 확실히 알고자 의식의 흐름대로 이해한걸 정리해본다.

## Intro

데이터 분석 공모전이나 프로젝트를 하게 되면 데이터 크기 자체가 TB를 넘어가는 일은 잘 없다. 그래서 보통 개인 노트북이나 데스크탑 등에 데이터를 저장하고 R, Python 등의 분석 프로그램에서 매번 불러와 사용한다. 그러나 TB, PB, ZB 단위의 데이터는 애초에 R, Python에서는 불러오는 것조차 버겁다. 기업의 데이터는 사이즈 자체가 매우 크니까 DB를 따로 저장, 처리할 필요가 있는데 주로 사용할 수 있는게 RDBMS(related database management system)다. 간단하게 말하면 데이터가 저장된 서버에서 데이터를 처리하는 시스템이다. 정형 데이터에 적합하고 RDBMS는 라이선스가 비싸기 때문에 수십 테라 이상의 데이터를 RDBMS에 저장하고, 처리하려면 비용이 어마무시하다. 이에 반해 하둡은 여러 대의 서버에 데이터를 저장하고, 각 서버에서 동시에 데이터를 처리하는 분산 처리를 지원하며 비정형 데이터도 다룰 수 있다. 

> 그럼 하둡이 어떻게 작동되길래 저런걸 할 수 있는걸까?

## 1. Hadoop

* 정식 명칭은 Apache Hadoop이며 대용량 데이터를 분산 처리할 수 있는 Java 기반의 오픈 소스 프레임워크다. 2006년 Doug Cutting과 Mike Cafarella에 의해 개발되었으며 커딩의 아들이 가지고 놀던 코끼리 인형 이름에서 Hadoop이란 이름을 따왔다고 한다.

![](https://s-seo.github.io/assets/images/post_spark_1.PNG) 

* 하둡의 두 가지 키워드는 **scalable**과 **distributed computing**이다. 하둡은 아래 두 시스템으로 구성된다고 볼 수 있다.

### 1-(1). HDFS(Hadoop Distributed File System)

* 분산 파일 시스템이며, 물리적으로 나눠져 있는 서버를 논리적으로 하나의 서버 형태로 구현한 파일 시스템이다. 이 때 마스터 서버를 NameNode, 슬레이브 서버를 DataNode라고한다.  

![](https://s-seo.github.io/assets/images/post_spark_3.PNG) 
출처: <https://sodayeong.tistory.com/29>

* 파일을 적당한 블록 사이즈(64mb, 128mb)로 나눠서 각 노드 클러스터(개별 컴퓨터)에 저장한다. 외부 시스템에서 하둡에 대용량 파일을 저장하면, 이 파일을 블록으로 쪼개서 각 블록을 서버의 로컬 디스크에 저장한다. 나중에 이 대용량 파일을 읽을 때는 여러 서버(디스크)에서 동시에 읽는다. 

* HDFS를 사용하는 사람은 블록이 어디에 저장되어 있는지 모른다. 엄밀히 말하면 알 필요가 없기 때문이며 이를 투과성이라고 한다. 또한 디스크 용량이 부족하면 서버를 추가(scale-out)하면 되기 때문에 확장성이 좋다. 그리고 각 블럭이 복수의 서버에 다중으로 저장되기 때문에 (replication factor를 지원한다고 함) 데이터 유실의 위험이 적어 신뢰성이 높다. 

* 또한 NameNode를 이중화시켜서 마스터 서버 고장에 대비한다. 기존에는 NameNode와 secondary NameNode 구조를 가졌으며 두 네임노드가 동시에 다운될 경우 시스템 전체가 마비되는 Single Point Of Failure(SPOF) 문제가 있다. 이를 보완하고자 Zookeeper라는 방법을 적용했는데, NameNode 고가용성(HA, high availability?)가 가능하도록 구성한 것이다. 여러 개 NameNode 중 하나만 active고 나머지는 standby 상태로 두는 것이다.





### 1-(2). Mapreduce

* 분산 처리 시스템이며, Map 함수에서 데이터를 처리하고 Reduce 함수에서 원하는 결과값을 계산하는 프레임워크로 데이터를 병렬 처리할 수 있게 해준다. 

* 데이터에 실행하고 싶은 처리를 Job이라고 하며, 분산 저장된 데이터에 실행되는 처리를 Task라고 한다. 즉, Job도 Task로 분배해야 하는데, 각 서버(컴퓨터)마다 성능도 다르고 오류가 발생하는 경우도 다르니까 이를 고려할 필요가 있다. 또 처리 중 서버가 고장나면 Task를 재실행해야 하고, 각 Task 처리 결과를 취합해서 출력도 해야하는데 이를 모두 자동화한 것이 Mapreduce다.

* Mapreduce에선 JobTracker(마스터 서버), TaskTracker(슬레이브 서버)로 구분한다

* Mapreduce 처리 흐름은 다음과 같다. 먼저 하나의 Job을 우리가 정해서 Mapreduce의 input으로 넣으면,

1. Job을 Map task로 분할한다.
2. HDFS로 분할된 각 블록에 Map task를 전달한다. (Map 처리)
3. Map task가 각 블록을 처리하고 작업 분담을 위한 key를 부여한다. (Map 처리)
4. key 별로 데이터를 정렬한다. (Shuffle)
5. 모든 데이터에 Reduce task를 병행하여 데이터를 처리한다. (Reduce 처리)

![](https://s-seo.github.io/assets/images/post_spark_5.PNG) 
출처: <https://dreamshutter.tistory.com/24>

* 위 그림은 하둡의 word count process를 시각화한 것이다. 이러한 절차를 이해하는 것은 쉽지만 코드로 구현하는 것은 어려운데, 하둡 라이브러리의 객체를 상속받아 메서드 오버라이딩을 하고 최종적으로 구현된 클래스를 모아 jar 형태로 만들어 배치 형태로 하둡에 다시 제출해야 하기 때문이다. 

* 

### 1-(3). RDBMS와 비교

|  | RDBMS | Hadoop |
|-|-|-|
| 데이터 크기 | 몇 TB까지는 가능하다 | PB도 가능하다 |
| 응답 시간 | 몇 초 정도 소요하기 때문에 빠르다.  | 분산 처리를 위한 전처리가 필요하여 최저 10~12초의 오버헤드 발생 |
| 서버 대수와 성능 향상 | 한 대의 서버 능력을 향상시키는 scale-up | 서버를 추가함으로써 성능을 향상시키는 scale-out |
| 데이터 구조 | structered data (고정된 schema가 필요하며 데이터가 사전에 정의된 구조로 정규화되어야 함)  | semi-structered data (schema가 반드시 필요하지 않고 처리 시점에 데이터 정의가 가능함) |



### 1-(4). Hadoop Eco System

![](https://s-seo.github.io/assets/images/post_spark_2.PNG) 

하둡에서 제공하는 일종의 확장 프로그램이라고 이해했는데, HDFS와 MapReduce는 그 중 일부라는 것이 확실하게 보인다. 각각의 개념에 대해 다뤄볼 기회가 생기면 좋겠다.




### 1-(5). Hadoop1의 한계

1. batch에 최적화되어 있어 streaming에 약하다
2. MapReduce만 지원하는데 MapReduce는 ad-hoc 데이터 분석에 적합하지 않다. 
3. 그 외 (JobTracker 하나에 많은 로드, Map/Reduce task 분배에서 자원 활용 문제)


### 1-(6). Hadoop2

















## 2. Apache Spark

이제 본 포스트의 목적인 Spark에 대해 알아보자. 위의 Hadoop의 한계로 나온 것이 Spark라고 볼 수 있다. 2009년 U.C. Berkely의 AMPLab에서 시작했다고 한다. Spark는 인메모리 기반의 대용량 데이터 고속 처리 엔진으로 범용 분산 클러스터 컴퓨팅 프레임워크다. Spark의 주요 개념은 Resilient Distributed Datasets (RDD)와 Directed Acyclic Graph (DAG) execution engine이다.

![](https://s-seo.github.io/assets/images/post_spark_6.PNG) 
출처: <https://niceguy1575.tistory.com/entry/SPARK-Framework%EC%97%90%EC%84%9C-%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%B6%84%EC%84%9D%ED%95%B4%EC%95%BC%ED%95%98%EB%8A%94%EA%B0%80>

위 그림은 Spark의 프레임워크를 시각화한 것이다. 흔히 Spark를 하둡과 연계하여 HDFS에서 데이터 소스를 가져오지만, 직접 DBMS로부터 조회하거나, CSV를 호출하는 것도 가능하다. 또한 Spark engine을 사용해서 SQL, ML, streaming, Graph analysis의 분석을 할 수 있다.


ETL(Extract, Transform, Load)은 정제되지 않은 데이터를 분석에 용이한 형태로 가공하는 일련의 과정이다. Data sources에서 data warehouse로 탈바꿈시키는 과정을 일컫는다. Spark는 이 중 load 정도만 담당하고, load된 데이터를 분석할 수 있다. E,T는 하둡 프레임워크에서 담당한다.

Spark 프레임워크에서 데이터 처리 방법론은 다음과 같다.

1. Data source로부터 데이터를 호출하여 RDD화 한다.
2. Transformation: 수행하고 싶은 operation으로 RDD tranformation
3. Action

Spark의 특징 중 하나는 lazy excution인데, transformation 단계가 아닌 action 단계에서 데이터를 호출해서 작업을 처리하기 때문에 효율적이다.




#### 2-(1). Resilient Distributed Datasets (RDD)

RDD는 Spark에서 사용하는 데이터 형태다. 여러 분산 노드에 저장되는 변경 불가능한 데이터의 집합이다. 현재는 RDD의 단점을 보완한 Dataset, DataFrame이 나왔다.

- Resilient: 분산되어 있는 데이터에 오류가 발생해도 자동적으로 복구할 수 있음
- Distributed: 클러스터의 여러 노드에 데이터를 분산시켜 저장
- Dataset: 분산된 데이터의 모음





두 가지 작업만을 지원한다. 
- Transformation: 새로운 RDD 데이터를 생성
- Action: RDD를 처리



#### 2-(2). Directed Acyclic Graph (DAG) execution engine

Spark의 scheduling을 담당한다. 어느 작업이 어떤 노드에서 어떤 순서로 실행되는지 결정한다. 

MapReduce의 느린 부분을 제거한 엔진이다. 





#### Hadoop과의 비교

Spark는 In-Memory data engine을 통해 MapReduce 보다 100배 더 빠르게 작업을 수행할 수 있다.

또한 Spark는 다양한 언어를 지원하기 때문에 개발화 친화적이라는 점에서 하둡보다 유용하다. 

Spark에서는 하둡의 분산 처리 엔진이 갖는 복잡함을 간단한 메서드 호출로 커버한다. 예를 들어 word count process는 MapReduce에서는 50줄이 필요하지만 Spark에서는 몇 줄로 줄일 수 있다.


하둡은 HDFS와 MapReduce를 사용하기 때문에 Spark가 반드시 필요하지는 않다. Spark도 HDFS 외 다른 클라우드 기반 데이터 플랫폼과 융합될 수 있어 하둡이 반드시 필요하지는 않다. 

하둡은 매번 Job의 결과를 디스크에 기록하기 때문에 HDFS나 MapReduce 과정에서 오류가 나더라도 결과를 활용할 수 있고, Spark는 RDD를 사용하기 때문에 오류가 나도 완벽하게 복구할 수 있다. 방식만 다를 뿐 둘 다 오류에 강건한 프레임워크다.

하둡은 데이터 일괄 처리를 최우선으로 하고, PB 데이터를 저렴하게 저장, 처리할 수 있다. Spark는 streaming data로의 전환이 용이하다.



#### 특징
- Speed: In-Memory 기반의 빠른 처리

- Ease of Use: 다양한 언어(Java, Python, R, SQL 등)를 지원
다양한 언어를 지원하지만 언어마다 처리 속도가 다르다. Scalar가 가장 빠르다.

- Generality: SQL, streaming, ML, 그래프 연산 등 다양한 기능 지원
Spark라는 단일 시스템에서 Spark SQL, Spark streaming, MLib, GraphX 등 다양한 분석을 할 수 있다는 것

- Run everywhere: 다양한 클러스터(YARN, Mesos, Kubernetes 등)에서 동작 가능하며 다양한 파일 포맷(HDFS, Casandra, HBase 등) 지원
