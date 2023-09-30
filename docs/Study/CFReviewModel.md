---
layout: default
title:  "CF 파이썬 구현"
parent: Study
permalink: /study/CFReviewModel/
nav_order: 3
date: 2023-09-28
math: mathjax
---
TL;DR; (OpenAI API, github actions 기반 자동 요약문)
***
- Collaborative Filtering (CF)은 다른 사용자의 평가를 기반으로 추천을 하는 방식이다.
- Scikit-learn의 TruncatedSVD와 Surprise의 SVD 알고리즘은 SVD를 기반으로한 모델이다.
- CF 연구는 matrix factorization에 기반한 CF 연구가 활발해졌으며, 사용자와 아이템의 잠재 특징을 배우는 방식이다.
***


- 구글링하면서 CF란 거대한 흐름을 간단히 탐색해봤고, CF의 대표적인 논문을 읽고 파이썬으로 직접 구현해보고자 한다.
- 사실 가벼운 흥미로 시작한 공부라 논문까지는 생각없었는데, 구글링으로 찾은 포스트의 설명과 예제는 한계를 많이 느껴서(이해 안되는 부분이 많았음) 오히려 흥미가 떨어질 것 같았다.
- 목적은 어디까지나 실시간 추천 서비스 배포에 있기 때문에, 배포하려는 서비스의 형태와 특징을 최대한 반영한 코드를 작성하는 것

***

## 논문 정리

먼저 Collaborative Filtering (CF)은 아래 논문에서 처음 나온 개념인 것으로 보인다.

[Goldberg, D., Nichols, D., Oki, B. M., & Terry, D. (1992). Using collaborative filtering to weave an information tapestry.](https://dl.acm.org/doi/10.1145/138859.138867)
{: .fs-3 .ls-10 .bg-grey-lt-200 .text-grey-dk-300 .note }

- Tapestry라는 시스템 소개글에 가깝다. 이 시스템을 소개하면서 collaborative filtering이란 용어가 처음 등장했고, CF의 개념, 시스템 아키텍쳐 등에 대해 언급함
    - 'Collaborative filtering simply means that people collaborate to help one another perform filtering by recording their reactions to documents they read'
- 메일 시스템에서 추천 모델이 나왔다는게 인상깊다. 개인용이나 업무용 메일 모두 양이 그렇게 많지 않아 대부분 확인하는 편인데, 아마 그 당시에는 모든 뉴스, 광고, 업무가 메일로 온 것으로 추정되어서 자연스레 필터링이 필요했던 것으로 보인다.
- 사용자가 문서에 대한 평가를 anootate하고 이 값을 기반으로 다른 사용자에게 문서를 추천한다. 이 때 임의의 다른 사용자가 아닌, 나와 평가가 비슷한 사용자를 필터링한다.
    - 논문에선 '비슷한 사용자', 즉 사용자 간 유사도를 어떻게 계산하는지 구체적으로 언급하진 않았다. 이후에 코사인 유사도, 피어슨 상관계수 등의 방법에 기반한 논문이 나온 것 같다.
- 이 논문에선 추천을 하는게 아니라, 필터링을 한다고 느꼈던 부분이
    - 사용자가 직접 다른 사용자의 평가를 활용해서 정보를 필터링하도록 설계함.
    - 필터링도 일반 SQL로 쿼리하는 것이 아닌, 별도의 쿼리 언어(Tapestry Query Language)를 만들어서 사용
    - 사용자가 서로의 평가를 공유할 수 있고, 이걸 공유 DB 형태로 제공해서 직접 쿼리해서 알아서 필터링하라는 것
    - 사용자가 스스로한테 추천을 해야하는 방식이라는 점에서 현대의 추천 시스템과 많이 다르다고 느낌
- 사용자의 평가(annotation)에 직접적으로 의존하기 때문에 memory-based라고 할 수 있다.
- pseudo code 같은 구체적인 알고리즘이 없어 이 논문은 그냥 읽기만 하고 따로 구현할 것은 없었다.

***

이후에 memory-based CF의 여러 variation이 나왔고, model-based CF 연구도 나왔지만, matrix factorization에 기반한 CF 연구는 아래 논문을 기점으로 활발해진 것으로 보임

[Koren, Y., Bell, R., & Volinsky, C. (2009). Matrix factorization techniques for recommender systems.](https://datajobs.com/data-science-repo/Recommender-Systems-[Netflix].pdf)
{: .fs-3 .ls-10 .bg-grey-lt-200 .text-grey-dk-300 .note }

- model-based CF에는 여러 방법론이 있음
    - Latent Semantic Indexing
    - Clustering Models
    - Bayesian Networks
    - Probabilistic Latent Semantic Analysis
    - Markov Decision Process
    - etc.
- 위와 같은 방법론이 나오다가, 2006년 Netflix Prize 경연에서 Simon Funk의 SVD 기반 CF가 우승하면서 matrix factorization(MF)에 기반한 model-based CF가 각광 받은 것으로 보임
    - 2009년에 나온 위 논문은 Simon Funk가 저술한 것은 아니지만, Simon Funk의 SVD를 중점적으로 두면서 MF 기반 model-based CF의 개론(?)같은 느낌
    - Simon Funk는 2006년에 자신의 블로그에 사용한 방법에 대한 글을 올림 [https://sifter.org/~simon/journal/20061211.html](https://sifter.org/~simon/journal/20061211.html)
- 논문을 통해 알고자 했던 것은,
    - 왜 model-based CF를 검색하면 SVD가 대세일지. 왜 이런 연구 흐름(?)이 생겼었는지
    - user-item matrix는 sparse matrix이고 incomplete하기 때문에 SVD를 적용하기 불가능할 것 같은데 어떻게 적용했다는 것인지
    - 파이썬 라이브러리(scikit-learn, Surprise)에서도 SVD에 기반한 학습 알고리즘을 제공하는데, 원리가 궁금했음 

### 1. 왜 SVD를 model-based CF에 적용하려는 흐름이 생겼을까?

- Memory-based CF 등장 (당시엔 이런 이름 없었음. 단순히 NN 알고리즘에 기반)
- NN 알고리즘을 대체할 latent factor model based CF이 나옴
- Latent factor model의 여러 기법 중 matrix factorization methods이 대표적임
    - $$ \hat{r}_{ui} = q_i^T p_u $$
- Matrix factorization methods의 여러 기법 중 singular value decomposition에 기반한 방법이 나옴
- Conventional SVD에 기반한 학습 알고리즘 한계: sparse matrix(+ imputation도 불완전), overfitting
    - 그냥 imputation 없이, 정규화만 반영함
- 아래의 최적화 문제를 해결하는 것과 같음
    - $$ \min_{q*,p*} \sum_{(u,i) \in \kappa} (r_{ui} - q_i^T p_u)^2 + \lambda (||q_i||^2 + ||p_u||^2) $$
    - 방법은 stochastic gradient descent와 alternating least squares
    - user-item matrix $$ R $$이 있다고 할 때, 이 행렬을 두 개의 행렬 $$ P, Q $$의 곱으로 근사시킴
        - $$ R \approx PQ^T $$
        - $$ P $$: 사용자와 잠재 특성 공간 간 매핑시키는 행렬
        - $$ Q $$: 아이템과 잠재 특성 공간 간 매핑시키는 행렬
    - $$ P, Q $$를 주어진 shape에 맞춰 무작위 값으로 초기화함
    - 주어진 평점 데이터와 근사시킨 평점 데이터 간 예측 오차를 최소화하도록 $$ P, Q $$를 SGD 방법으로 업데이트 함

### 2. sparse, incomplete matrix에 SVD를 어떻게 적용했다는 것인지?

- 이 논문에서 말하는 SVD는 Funk의 SVD (Funk SVD)를 말함
    - 논문에서도 sparse matrix에 SVD를 적용하기 위해 imputation을 해볼 수도 있다고 하는데, 불확실성이 증대해 비추한다고 나옴
    - 'Hence, more recent works suggested modeling directly the observed ratings only, while avoiding overfitting through a regularized model.'
- Conventional SVD를 적용하기 위해선 해당 행렬이 complete matrix라는 가정이 필요하며, 주어진 행렬을 세 개의 행렬의 곱으로 분해함
    - Funk SVD는 sparse matrix에도 적용 가능하며, 세 행렬의 곱이 아닌 두 행렬의 곱으로만 근사시킴
- SVD와 Funk SVD간 연결점을 따지자면, 주어진 행렬을 latent factor model의 관점에서 다룬다는 것
- 복잡하게 생각할 것 없이 Funk SVD는 그냥 전통적인 SVD의 latent factor space라는 아이디어, 개념, 의미를 차용했다고 보면 됨
    - 두 행렬로 분해시켜서 각각 학습시킨다는 관점에서만 보면 QR decomposition이나 eigendecomposition 등 일반적인 matrix decomposition을 사용했다고 해도 무방하지 않을까?
    - 다만 잠재 특성이라는 개념을 사용했다는 점에서 SVD의 variation이라고 할 수 있는 것
    - 상당히 직관적인 사고방식이다. 수학적 공식에 의해 만들어낸 알고리즘이라기 보다는, 지식을 넘어선 지혜에 기반한 방법론 같아 인상 깊음

### 3. scikit-learn, Surprise에선 어떤 방식으로 SVD 기반 학습 알고리즘을 구현한 것인지? (ChatGPT 참고)

- scikit-learn의 TruncatedSVD는 기존의 conventional SVD와 달리 $$ \Sigma $$의 작은 값을 제거해서 행렬의 차원을 truncated 시킨 후, 이 행렬을 SVD 하는 방식
- Surpise의 SVD 알고리즘은 Simon Funk의 SVD를 구현한 것
- 두 방법 모두 conventional SVD의 변형(응용? 활용?)인 셈이라 sparse matrix에도 적용 가능하며, 사용자와 아이템의 잠재 특성을 학습하는 알고리즘

### 4. 그 외 논문 읽고 든 생각

- 구글링 할 때와 달리 논문을 읽고 정리 된 생각 중 하나
    - 구글링: user-item matrix를 어떻게든 SVD 시켜서 나온 세 개의 행렬을 가지고 학습시키는 줄 알았음
    - 논문: SVD의 개념만 차용. 학습시키는 행렬 자체는 무작위 추출에 가까움
- Mean matrix ($$ \mu $$)를 왜 빼는건가 궁금했었고, 스터디에서 사용자의 편향을 다루기 위한 장치라는 피드백을 받았는데, 논문에 이를 더 자세하게 설명함. 이해한대로 정리해보면,
    - bias를 고려해야 하는 이유는 결국, 평가는 주관적일 수 밖에 없고, 그걸 수치화한 값 역시 사용자의 편향이 있음. 이러한 편향을 고려하지 않고 CF를 적용한다면, 대체로 평점이 높은 특정 아이템 군만 추천이 되거나, 대체로 높은 평점을 주는 특정 유저 그룹의 선택만이 추천될 수 있음. 그럼 편향을 모델에 어떻게 반영하고, 어떻게 측정할 것인지?
    - 임의의 유저 $$ u $$가 임의의 아이템 $$ i $$에 대해 매긴 평가가 $$ r_{ui} $$이라고 할 때, 이 평가에 포함된 bias를 $$ b_{ui} $$ 라고 함
    - $$ \hat{r}_{ui} = b_{ui} + q_i^T p_u $$로 위 식이 확장됨
    - 논문에서는 가장 기본적인 first order approxiamte을 통해 $$ b_{ui} = \mu + b_u + b_i $$로 정의함
    - $$ \hat{r}_{ui} = \mu + b_u + b_i + q_i^T p_u $$로 정의할 수 있음
    - $$ \min_{q*,p*,b*} \sum_{(u,i) \in \kappa} (r_{ui} - (\mu + b_u + b_i + q_i^T p_u))^2 + \lambda (||q_i||^2 + ||p_u||^2 + b_u^2 + b_i^2) $$
    - bias는 intercepts와 비슷한 위치인 것 같음
- Bias 외 overfitting을 완화하기 위한 정규화 장치, implicit data(ex. user click rate 등)를 반영한 모델, temporal dynamics라는 시간에 따른 유저 선호도 변화까지 반영한 모델을 다루는게 인상 깊음
    - 논문에서 말하는 implicit data가 결국 우리가 배포하려는 서비스의 input data 형태가 될 것 같다. 논문에선 implicit data를 추가해서 예측을 보완하지만, 우리는 implicit data만으로 예측을 해야함
    - 추천 시스템에 기반한 프로덕트의 retention을 위해서라도 temporal dynamic 모델을 다루는 것이 좋을 것 같다.
        - 들어올 때 마다 같은 아이템만 표시한다면, 다시 이 서비스를 찾을 이유가 그렇게 크지 않을 것 같음
        - 내 선호가 바뀜에 따라 추천 받는 아이템도 바뀌는 것이 상식적으로도 그럴듯함

***

## Funk SVD 기반 CF model (+ biased) 파이썬 구현

- $$ \min_{q*,p*,b*} \sum_{(u,i) \in \kappa} (r_{ui} - (\mu + b_u + b_i + q_i^T p_u))^2 + \lambda (||q_i||^2 + ||p_u||^2 + b_u^2 + b_i^2) $$
- SGD를 사용해서 각 파라미터를 아래와 같이 업데이트 시킴
    - $$ b_u \leftarrow b_u + \alpha \left( e_{ui} - \lambda b_u \right) $$
    - $$ b_i \leftarrow b_i + \alpha \left( e_{ui} - \lambda b_i \right) $$
    - $$ p_u \leftarrow p_u + \alpha \left( e_{ui} \cdot q_i - \lambda p_u \right) $$
    - $$ q_i \leftarrow q_i + \alpha \left( e_{ui} \cdot p_u - \lambda q_i \right) $$
    - $$ e_{ui} = 1 - \left( \mu + b_u + b_i + q_i^T p_u \right) $$ 는 예측 오차
    - $$ \alpha $$는 learning rate
- Train data: user_id, movie_id 열로 구성된 테이블
    - 영화 시청 여부라는 implicit data만을 가지고 학습
- Ratings가 아닌 implicit data로 학습할 때 차이점?
    - error 계산 시 추정한 값을 1에서 뺀다는 점
- 새로운 유저에게 추천
    - user_id (int)와 movie_id (list)를 받아서 추천하는 movie_id의 index(movie_indices)를 출력
    - 출력된 movie_indices를 movies.dat에 조인시켜 최종 추천 결과 받음
    - 새로운 유저가 유입될 때 마다 모델 전체를 학습시킬 필요 없이, 새로운 유저에 대응하는 파라미터만 학습시킴
- 보완
    - 추천 결과는 받을 수 있는데 이걸 장고 페이지에 어떻게 띄울지? (+ post method로 유저가 입력한 값 받는 상황도 반영해야)
    - 모델 성능 평가 메서드 추가 (이걸 실시간 서비스에서 어떻게 활용하는건지도)
    - 만약 같은 유저가 여러번 페이지 접근하는 경우, 매번 다른 추천 결과를 띄워주는 방향?
    - 유저의 선호는 시간에 따라 변할 수 있음. 이런 temporal dynamics를 반영한 모델
        - 필요할까?
    - 기존 유저가 본 영화가 추가되는 경우