---
layout: default
title:  "CF 모델"
parent: Study
permalink: /study/CollaborativeFiltering/
nav_order: 3
date: 2023-09-15
math: mathjax
---

추천 모델의 대표적 전략 중 하나인 Collaborative Filtering (CF)에 대해 정리 및 구현하고자 한다. 

## CF란?

- 사용자 간 협업(collaborative)을 바탕으로 아이템을 추천하는 전략이다. 사용자 행동 데이터를 주로 사용한다는 점에서 기존의 Content-based Filtering과 차이가 있다.
- collaborative라는 용어가 붙은 이유는, 다른 사용자들의 선호를 기반으로 특정 사용자의 선호를 추정하기 때문인 것으로 보인다.
- 사용자의 선호가 필수이므로, user-item 데이터를 사용하는데 보통 matrix 형태로 가져간다.
- 예를 들어 나에게 영화를 추천할 때, 나와 선호도가 비슷한(평점을 비슷하게 매긴) 사용자들이 좋은 평점을 매긴(그런데 나는 아직 안 본) 영화를 추천한다.
    - 먼저 비슷한 정도를 사용자 단에서 파악할 것인지, 아이템 단에서 파악할 것인지에 따라 item-based filtering과 user-based filtering으로 구분된다

## Item-based filtering VS User-based Filtering

- 이름에서 알 수 있듯이 전자는 아이템 간 유사성을, 후자는 사용자 간 유사성을 기반으로 추천한다.
- 유사한 정도를 추정하는 방식에서 매우 다양한 방법론이 나올 수 있다. 대표적인 방법으론,
    - Cosine Similarity
    - Pearson Correlation Coefficient
    - Euclidean Distance
- item-based의 경우 기존 CBF와 다른 점은 사용하는 데이터, 유사성에 대한 정의에 있다.
    - item-based: 사용자들의 행동 데이터를 기반으로 아이템 간 유사성 추정. 예를 들어 많은 사용자들이 영화 A와 B에 비슷한 평점을 부여하면, A와 B는 유사하다고 본다.
    - CBF: 아이템의 내용 또는 특성을 기반으로 아이템 간 유사성 추정. 예를 들어 영화 A와 B가 같은 장르와 같은 감독의 작품이라면 A와 B는 유사하다고 본다.
- 이러한 필터링 방식은 모두 유사도를 직접 계산한다는 점에서 memory-based CF의 주요 전략이다. 아예 사용자 간 상호작용 패턴을 통째로 학습해버린 뒤, 학습한 패턴으로 예측하는 model-based CF도 있다.

## Python Example (Memory-based)


## Memory-based VS Model-based

- 앞에서 user-item matrix를 만들었는데, 전자는 이걸 메모리에 올려두고 새로운 추천이나 예측이 필요할 때 마다 이 행렬을 참조해서 유사도를 계산한다.
    - 후자는 user-item 상호작용 데이터를 바탕으로 모델을 사전 학습시키고, 학습된 모델만을 사용해서 추천한다.
- 넷플릭스와 같이 대용량의 사용자 데이터를 기반으로 실시간 추천 서비스를 하는 프로덕트의 경우, memory-based로 추천을 하게되면 비용이 상당할 것
    - 이런 비용을 감수하고 서라도 memory-based를 사용할 이유는 없어보임. 당연히 model-based로 가는 것이 수순아닐까.
    - 넷플릭스에서 주최한 추천 알고리즘 대회에서도 SVD 사용한 방법이 우승했던 적이 있다

## Singular Value Decomposition (SVD, Model-based Filtering)

- Matrix Decomposition의 대표적인 기법 중 하나다. 학부 때 선형대수학에서 자주 접한 개념인데 추천 시스템에서 잘 쓰이고 있다니 신기하다.
- $$R$$라는 $$m*n$$ 행렬이 있다고 가정하자. $$m$$은 유저 수를 $$n$$은 아이템 수를 의미한다.
- $$R = USV^T$$로 decompose하는 것이 SVD이다
    - $$U$$: $$m*r$$의 orthogonal matrix, 각 행은 사용자의 잠재적 특성을 나타냄
    - $$\Sigma$$: $$r*r$$의 diagonal matrix, 대각선 원소는 각 잠재적 특성의 중요도를 나타냄
    - $$V$$: $$n*r$$의 orthogonal matrix, 각 행은 아이템의 잠재적 특성을 나타냄
- SVD를 사용해 $$R$$의 latent factors를 추출함으로써 차원을 $$r$$개로 줄일 수 있다. 각 사용자와 아이템을 $$r$$개의 잠재 요인으로 나타내는 것과 같다.
- 
- SVD는 단순한 matrix decomposition 기법. 이걸 기반으로 모델을 학습시키는 것은 아래 과정이 추가됨
    - user-item matrix를 SVD 시켜 얻은 초기 $$U$$, $$V$$를 무작위로 초기화함 (shape만 따오는건가?)
    - 두 행렬의 내적을 가지고 예측 평점 행렬을 구함 ($$R_{pred}$$)
    - $$R$$과 $$R_{pred}$$ 간의 오차 (SSE 또는 RMSE)를 계산
    - Gradient Descent와 같은 최적화 알고리즘을 사용해 loss를 최소화하는 방향으로 $$U$$, $$V$$를 반복적으로 업데이트시킴
    - 오차의 변화가 특정 임계값 이하로 줄어들면 학습 종료
    - 이렇게 학습된 $$U, V$$로 새로운 사용자와 아이템의 평점을 예측할 수 있음
    - 예측한 평점에서 높은 평점을 추천할 수 있음


## Python Example (Model-based)


### 왜 SVD일까?

- 방법을 이해하고 나니 드는 의문은, 왜 RS에서 굳이 matrix factorization을, 그 중에서도 SVD를 선택한걸까라는 것이다
- 일단 RS의 user-item matrix의 보편적 특징을 먼저 짚어볼 수 있다
    - extremly high sparsity: RS에서 다루는 대부분의 user-item matrix는 매우 sparse하다. 
        - 애초에 모든 유저가 모든 아이템을 다 경험했다면 추천할 것이 없다. (재탕에 대한 니즈가 있는 시장이라면 얘기가 달라질까?)
        - 이렇게 안 이쁜 행렬을 이쁘게 만들어주는 어떤 전처리 과정이 들어가지 않는 이상, 현재 이 User-item matrix에 적용 가능한 기법은 많지 않다
    - 유저의 아이템에 대한 선호를 결정짓는 일종의 latent factor가 있을 것이라는 가정 (이 가정 하에선 모든 추천 문제를 matrix decomposition으로 접근 가능함)
- SVD는 high-sparse matrix에 적용 가능할 뿐더러(eigen-decomposition과 달리) 차원까지 축소시켜 이를 latent variable model로도 볼 수 있다는 강력한 장점이 있다.
- latent variable model도 처음에는 이해하기 어려웠다. 관련 설명을 읽어보면, 결국 값에 의미를 부여하는 것처럼 보이는데, 값 자체는 의미가 담길 수 없으니까.
    - 그렇게 보겠다~라는 정도로 받아들이면 될 것 같다.



