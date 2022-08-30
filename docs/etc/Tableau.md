---
layout: default
title:  "Tableau"
parent: ETC
# nav_order: 97
---


***

# Tableau

* Tableau는 BI(Business Intelligence)에 특화된 interactive data visualization software로 스탠포드의 CS 연구원 3명이서 창립했다고 한다. 비교적 최근인 2019년에 Salesforce가 $15.7 bilion에 인수했다고 한다. Tableau의 근본은 시각화 툴이니까 창립자 중 실용미술(?)과 관련된 사람도 있을줄 알았는데, 공대생들이 data visualization 쪽으로 작정하고 만든 작품이라니 놀랍다. 중간에 많은 발전이 있었겠지만..!

* RDBMS, online analytical processing cubes, cloud databases, spreadsheets 등을 지원한다는데, 이 중 RDBMS, spreadsheets만 좀 익숙하고 나머지는 아직 관심 분야다. 아직 갈 길이 멀다. 

* In-memory data engine에서 데이터를 extract, store, retrieve 한다는데, 도대체 In-memory가 뭐길래 Spark부터 계속 나오는걸까? 그냥 메모리에 저장한다는게 서버에 저장하는 것과 어떻게 다르길래? 부가적인 개념은 뒷부분에서 다루겠다.

* 과거의 BI 솔루션은 진입 장벽이 높아서 IT 부서에 높은 의존성을 가졌는데, Tableau, Power BI 등의 BI 솔루션이 나오면서 진입 장벽이 낮아졌고, 스스로 데이터를 보고 이해할 수 있는 self-BI가 대두되었다.


***

# 특징

* 자유도가 높은 만큼 다른 BI 솔루션보다 배우는데 시간이 좀 더 걸리지만, 그만큼 다양한 시각화가 가능하다. 단순히 drag & drop으로 시각화가 가능할정도로 편리하고, 속도가 빠르다. Interactive visualization이 가능하고 자체 분석 기능도 있다.

* 그러면 R, Python으로 데이터를 시각화하고 분석해온 사람 입장에서 Tableau와 같은 툴이 왜 필요할까? 에 대한 답이 위 특징들이다. General하게 편리하고 설득력있는 결과를 빨리 내는게 기업 입장에서는 중요하니까 이런 BI 솔루션이 각광받는다고 생각된다. 



***

# 데이터 연동

* 지원하는 커넥터
    * Excel, JSON, pdf 등 로컬 디스크에 저장된 파일
    * Tableau server 또는 Tableau online
    * Cloudera Hadoop, MarR Hadoop Hive, Spark SQL
    * MySQL, Oracle 등

* 방법

![](https://s-seo.github.io/assets/images/post_tableau_6.PNG) 

*데이터 연결*을 클릭하고

![](https://s-seo.github.io/assets/images/post_tableau_7.PNG) 

원하는 방식을 선택한 뒤, *초기 SQL...* 버튼을 누르면

![](https://s-seo.github.io/assets/images/post_tableau_9.PNG) 

이렇게 간단한 SQL query를 입력할 수 있다. 서버에 있는 데이터에 이 query가 반영이 되어서 Tableau에 호출되는 것 같다.

* MySQL,MS SQL, ORACLE등의 OLAP 데이타 백앤드에 연결해서 AD HOC 방식으로 리포트를 뽑아낼 수 있다.





***
# 기타 개념

### In-Memory Computing

데이터를 하드 디스크가 아닌 메인 메모리에 올려서 작업하는 것을 의미한다. 기존에 메모리는 연산을 수행하는 도구로만 인식됐는데 (엄밀히 말하면 아님. 기존 DBMS도 caching을 통해 자주 사용되는 데이터는 메모리에 넣어서 입출력 속도를 향상 시킴) 이 메모리 영역을 대용량 데이터 처리 공간으로 사용하는 것이다. 예전에 비해 메모리 가격이 많이 낮아져서 가능한 것도 있다고 한다. 즉, RAM이 데이터 관리에 사용된다는 개념이 In-Memory Computing이다. 

![](https://s-seo.github.io/assets/images/post_tableau_1.PNG) 
> 출처: <https://m.blog.naver.com/PostView.nhn?blogId=gkenq&logNo=10183400845&proxyReferer=https:%2F%2Fwww.google.com%2F>


### BI

* 데이터를 활용해 최선의 의사 결정을 내리고 결과적으로 비즈니스 목표를 달성하게 만드는 모든 과정과 방법을 의미한다. 기업 내외부의 데이터를 수집, 처리, 분석하는 과정과 BI의 결과물로 얻을 수 있는 고객 이탈 위험도, 행동 패턴, 수익성 등을 망라한 개념이다.

* BI 솔루션은 정말 많은데 IT 분야 리서치 기업인 가트너에 따르면 MS의 Power BI, Qlik의 Qlik Sence와 Tableau 이 3개가 대표적인 솔루션이라고 한다. 

![](https://s-seo.github.io/assets/images/post_tableau_2.PNG) 
> 출처: <https://www.yellowfinbi.com/campaign/gartner-magic-quadrant-for-analytics-and-bi-platforms-2021>

* BI의 출발은 데이터 소스다. 

* Tableau는 대표적인 BI 솔루션이자 그 중 데이터 시각화에 특화된 툴이다. 데이터 저장부터 분석까지 가능한 self-BI tool, self-analysis가 특징 중 하나다. 당연히 R, Python과 연동하여 복잡한 분석을 시각화할 수도 있다.

![](https://s-seo.github.io/assets/images/post_tableau_3.PNG) 
> 출처: <https://jaydata.tistory.com/66?category=870794>

* 위 그림은 BI 시스템의 아키텍쳐를 도식화한 것이다. 데이터 소스에서 ETL(Extract, Transform, Load)을 거쳐 data warehouse를 구축하고, BI 솔루션의 목적에 적합하게끔 가공한 데이터 마트를 구축한다. 데이터 마트가 우리가 흔히 말하는 DB에 해당하는건가? 아니면 DB는 데이터 웨어하우스와 마트를 포괄하는 개념인가..?

* Tableau는 BI 솔루션이기 때문에 데이터 소스에 SQL을 사용해서 데이터 마트를 구축한 뒤, 대시보드를 구성한다는 아키텍쳐를 따른다. 이 과정을 정리한 두 가지 문서를 작성해야 하는데, 데이터 소스 정의서와 데이터 흐름 정의서다. 

### 데이터 소스 정의서
데이터 마트와 Tableau를 연동할 경우, 데이터 마트에서 필요한 데이터를 추출하는데, 이렇게 추출된 데이터를 Tableau data source라고 한다. 이와 관련된 여러 정보를 정리한 것이 데이터 소스 정의서다.

![](https://s-seo.github.io/assets/images/post_tableau_5.PNG) 
> 출처: <https://jaydata.tistory.com/66?category=870794>

### 데이터 흐름 정의서
데이터 소스, 데이터 마트, 시각화의 3단계를 거치는 일련의 과정을 정리한 것이 데이터 흐름 정의서다. 

![](https://s-seo.github.io/assets/images/post_tableau_4.PNG) 
> 출처: <https://jaydata.tistory.com/66?category=870794>

이 두가지가 있어야 나중에 문제가 발생하더라도 어디서 데이터 정합성 문제가 발생했는지 알 수 있고, 결과에 대한 올바른 분석을 할 수 있다.




### AD HOC 방식

* Ad-hoc 방식이라하면 네트워크 관련된 내용이 주로 나오는데, BI에서 ad-hoc analysis라는 개념도 있고... 이 부분은 좀 더 공부가 필요하다. 내가 알고 싶은 ad-hoc 방식은 BI 솔루션과 연관된 것!

* OLAP의 필드를 가지고, X,Y,Z 측으로 지정하여 분석하고 리포트나 그래프등을 표현할 수 있는 툴로써 비교하자면 엑셀의 피봇테이블과 같은 기능을 데이타 베이스에 연결하여 활용 가능한 시각화 Tool이다.



