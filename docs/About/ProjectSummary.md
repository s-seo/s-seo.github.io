---
layout: default
title: Projects Summary
parent: About
has_children: true
nav_order: 97
has_toc: false
---

***
# Non-Profit Data Analysis

계획: AWS resource, streaming data, batch, airflow, crawling, ETL, simple modeling, tableau


***
# 2020 빅콘테스트

### 공모전 소개

국내 데이터 분석 공모전 중 가장 규모가 큰 [2020 빅콘테스트](https://www.bigcontest.or.kr/index.php) 챔피언 리그에 참여함. 대회 주제는 다음과 같음

* NS Shop+편성데이터(NS홈쇼핑) 를 활용하여 방송편성표에 따른 **판매실적을 예측**
* 최적 수익을 고려한 요일별, 시간대별, 카테고리별 **편성 최적화** 방안(모형) 제시


#### 문제 정의 및 해결

공모전의 가시적인 주제인 매출 예측하는 기본적인 시계열 분석 (효율성, 정확성, 지속가능성) 외에 고려한 부분 :

|                             문제                             |                  해결 방안                  |
| :----------------------------------------------------------: | :-----------------------------------------: |
| 2019년도의 데이터로 2020년 6월의 매출을 예측해야 한다는 time gap 문제 |             Recursive 변수 반영             |
| COVID-19의 영향력이 크지만 관련 데이터가 주어지지 않았다는 한계 | 네이버 쇼핑 데이터 웹크롤링, COVID 19 Index |
| COVID-19을 반영해 어찌어찌 예측했다 하더라도 제대로 반영했는지? |           Counterfactual Analysis           |
|       편성표 최적화 (최적화 개념 정의와 구체적인 방법)       |             Hungarian Algorithm             |


#### 역할

* 팀리더로서 프로젝트 총괄
* 웹크롤링을 사용한 데이터 수집 (네이버 쇼핑)
* Counterfactual analysis를 사용한 인과관계 분석
* 데이터 시각화 (R)
* 최적화 알고리즘 문제 정의,구축 및 결과 해석([헝가리안 알고리즘](https://en.wikipedia.org/wiki/Hungarian_algorithm) 응용)


##### More : [**2020 빅콘테스트 ㅁㅁㅁㅉ팀**](https://s-seo.github.io/projects/bigcon)


***


# 서울의대 GAN 프로젝트

### 프로젝트 소개

서울대학교 의료빅데이터연구센터(MBRC)에서 의료빅데이터 융합인재 양성을 위해 진행한 보건의료 데이터 기반의 연구 과제. 직접 데이터와 주제를 선정한 뒤 의미있는 결과를 도출, 발표하는 방식.


### 문제 정의 및 해결

임상빅데이터연구실(CBL)에서 연구원으로 근무하며 파악한 국내 의료 통계의 가장 큰 한계점은 통계 분석, 모델이 교육 및 연구에 잘 사용되지 않는다는 것. 이와 관련한 여러 요인 중 개인정보보호법에 대해 관련 문제를 정의하고 GAN을 사용해 해결하고자함

|                             문제                             |                          해결 방안                           |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| 개인정보보호법에 의해 사용 가능한 의료 데이터가 절대적으로 부족해서 충분한 성능의 모델이 없음 | GAN을 사용해 fake image를 생성하고 이를 다시 model fitting에 사용 |


### 역할

* 문제 정의
* 데이터 전처리
* GAN, CNN 모델링 및 결과 해석

![](https://s-seo.github.io/assets/images/project_gan_1.PNG) 

##### More : [**GAN project(keep updating)**](https://s-seo.github.io/projects/GAN)


***


# 모나미 수요예측 프로젝트

### 프로젝트 소개

2018 연세 빅데이터 분석 공모전의 연장선으로 (주)모나미에서 인턴 기회를 얻어 (주)모나미에서 제조, 유통하는 문구류 SKU(stock keeping unit)별 재고를 효율적 관리할 필요성을 파악하고 이에 수요예측 프로젝트를 진행함.

### 문제 정의 및 해결

|                             문제                             |                          해결 방안                           |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| 제품의 수요 예측 정확도를 높여 불필요한 재고를 줄이고, 재고 생산 비용, 관리 비용을 감축시킬 수 있음 | RDBMS 및 ER diagram 구축  <br> spatial 변수 등 다양한 변수를 생성 <br> 이를 반영한 다변량 시계열 모델(dynamic regression) 사용 |

### 역할

* 팀리더로서 프로젝트 총괄
* 데이터 통합 (정합성 검증), 전처리, feature engineering (Geocoding, product categorization)
* Dynamic regression in Forecast Pro 모델링 및 결과 도출 (MAPE 10%p 감소)
* 보고서, 매뉴얼 작성 


### More : [**Demand forecasting project(keep updating)**](https://s-seo.github.io/projects/monami)


***

# 2018 연세 빅데이터 분석 경진대회

### 공모전 소개 

연세대학교 상경대학에서 주최한 데이터 분석 공모전으로 기업의 빅데이터를 토대로 주제 선정부터 결과 발표까지 팀 단위로 진행됨.


### 분석 주제

1. 모나미 로드
   2014년 한국행정구역 체계를 토대로 모나미 제품의 매출 패턴을 지도로 시각화함

![](https://s-seo.github.io/assets/images/project_yonsei_1.PNG) 


2. 반품 예측 모델
   반품을 예측하고 반품의 결정적인 요인을 파악함으로써 모나미와 거래처의 손실을 줄이고자함

![](https://s-seo.github.io/assets/images/project_yonsei_2.PNG) 


### 역할

* 팀리더로서 프로젝트 총괄 
* 데이터 전처리, feature engineering(한국행정구역 변수, 품목명 카테고리화 등), EDA, 시각화(모나미 로드)
* 반품 예측 모델링(Random forest, AUC = 0.995)

### More : [**2018 Yonsei project(keep updating)**](https://s-seo.github.io/projects/yonsei)

(당시에는 따뜻함이라는 모나미의 브랜드 이미지에 꽂혀서 이런 이미지를 더 많은 소비자와 거래처에게 전달하겠다는 목적 아래 위와 같은 분석을 했다고 어필했는데 지금 생각하면 살짝 부담스럽다...)









