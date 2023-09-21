---
layout: default
title:  "CF 모델"
parent: Study
permalink: /study/CollaborativeFiltering/
nav_order: 3
date: 2023-09-15
math: mathjax
---


추천 시스템의 대표적 전략 중 하나인 Collaborative Filtering (CF)에 대해 정리 및 구현하고자 한다. 

## CF란?

- user-item interactions 데이터를 바탕으로 아이템을 추천하는 전략이다.
- 사용자 행동 데이터를 사용한다는 점에서 기존의 Content-based Filtering과 차이가 있다.
- 예를 들어 나에게 영화를 추천할 때, 나와 선호도가 비슷한(평점을 비슷하게 매긴) 사용자들이 좋은 평점을 매긴(그런데 나는 아직 안 본) 영화를 추천한다.
- CF 단점
    - Cold start: CF 기반 추천 시스템이 작동하려면 충분한 양의 user-item interactions가 있어야 함. 이 데이터가 충분히 쌓이기 전까진 이 방식으론 제대로 된 추천을 할 수 없다.
    - 새로운 사용자, 아이템 추가 시 기존의 interactions가 없기 때문에 추천받거나, 추천되기 어렵다. (이를 보완하고자 hybrid system 필요)
- CF 방법은 memory-based와 model-based로 나뉜다.

## Memory-based VS Model-based CF

- Memory-based CF는 user-item matrix를 메모리에 올려두고 새로운 추천이나 예측이 필요할 때 마다 이 행렬을 참조해서 유사도를 계산한다.
    - Memory-based CF는 먼저 비슷한 정도를 사용자 단에서 파악할 것인지, 아이템 단에서 파악할 것인지에 따라 item-based filtering과 user-based filtering으로 구분된다
- Model-based CF는 user-item 상호작용 데이터를 바탕으로 모델을 사전 학습시키고, 학습된 모델만을 사용해서 추천한다.

## Item-based Filtering VS User-based Filtering

- 이름에서 알 수 있듯이 전자는 아이템 간 유사성을, 후자는 사용자 간 유사성을 기반으로 추천한다.
- 유사한 정도를 추정하는 방식에서 매우 다양한 방법론이 나올 수 있다. 대표적인 방법으론,
    - Cosine Similarity
    - Pearson Correlation Coefficient
    - Euclidean Distance
- item-based의 경우 기존 CBF와 다른 점은 사용하는 데이터, 유사성에 대한 정의에 있다.
    - item-based: 사용자들의 행동 데이터를 기반으로 아이템 간 유사성 추정. 예를 들어 많은 사용자들이 영화 A와 B에 비슷한 평점을 부여하면, A와 B는 유사하다고 본다.
    - CBF: 아이템의 내용 또는 특성을 기반으로 아이템 간 유사성 추정. 예를 들어 영화 A와 B가 같은 장르와 같은 감독의 작품이라면 A와 B는 유사하다고 본다.


## Model-based CF

- 아이디어: user-item interactions의 패턴을 통째로 학습한 뒤, 학습한 패턴을 기반으로 사용자가 선호할만한 top-N items를 예측
- Memory-based CF에 비해 sparse한 user-item matrix에서도 효과적인 추천 가능
- ![https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0](https://s-seo.github.io/assets/images/post_CollaborativeFiltering_1.png){: width="600" height="400"}
- Non-parametric approach: 유사성을 추정하되 비지도 학습 방식을 사용한다는 점에서 메모리 기반 CF와 다르다. 대표적으로 KNN 방식이 있다.
- Matrix Factorization based algorithm: 사용자-아이템의 선호도를 latent factor로 설명할 수 있다는 가정에 기반한다.
    - 대표적으로 Singular Value Decomposition (SVD)가 있다. 
    - $$R$$라는 $$m*n$$ 행렬이 있다고 가정하자. $$m$$은 유저 수를 $$n$$은 아이템 수를 의미한다.
    - $$R = USV^T$$로 decompose하는 것이 SVD이다
        - $$U$$: $$m*r$$의 orthogonal matrix, 각 행은 사용자의 잠재적 특성을 나타냄
        - $$\Sigma$$: $$r*r$$의 diagonal matrix, 대각선 원소는 각 잠재적 특성의 중요도를 나타냄
        - $$V$$: $$n*r$$의 orthogonal matrix, 각 행은 아이템의 잠재적 특성을 나타냄
    - SVD를 사용해 $$R$$의 latent factors를 추출함으로써 차원을 $$r$$개로 줄일 수 있다. 각 사용자와 아이템을 $$r$$개의 잠재 요인으로 나타내는 것과 같다.
- Deep Learning: MF를 응용한 것이라 볼 수 있는데, NN을 사용해서 embedding matrices의 값을 업데이트(최적화)하는 방식이다.
    - SVD는 단순한 matrix decomposition 기법. 이걸 기반으로 모델을 학습시키는 것은 아래 과정이 추가됨
        - user-item matrix를 SVD 시켜 얻은 초기 $$U$$, $$V$$를 무작위로 초기화함 (shape만 따오는건가?)
        - 두 행렬의 내적을 가지고 예측 평점 행렬을 구함 ($$R_{pred}$$)
        - $$R$$과 $$R_{pred}$$ 간의 오차 (SSE 또는 RMSE)를 계산
        - Gradient Descent와 같은 최적화 알고리즘을 사용해 loss를 최소화하는 방향으로 $$U$$, $$V$$를 반복적으로 업데이트시킴
        - 오차의 변화가 특정 임계값 이하로 줄어들면 학습 종료
        - 이렇게 학습된 $$U, V$$로 새로운 사용자와 아이템의 평점을 예측할 수 있음
        - 예측한 평점에서 높은 평점을 추천할 수 있음

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

### Model-based CF 구현 예제

[https://machinelearningmastery.com/using-singular-value-decomposition-to-build-a-recommender-system/](https://machinelearningmastery.com/using-singular-value-decomposition-to-build-a-recommender-system/)
[https://analyticsindiamag.com/singular-value-decomposition-svd-application-recommender-system/](https://analyticsindiamag.com/singular-value-decomposition-svd-application-recommender-system/)
- SVD를 사용해서 item의 latent features를 구한 뒤, 이걸 기반으로 Cosine similarity를 구해 아이템 간 유사도를 측정함. Memory-based CF의 item-based filtering을 SVD 사용해서 구한 예제

[https://data-science-hi.tistory.com/73](https://data-science-hi.tistory.com/73)
- item-based filtering, user-based filtering을 KNN & cosine similarity를 사용해 구현

[https://keras.io/examples/structured_data/collaborative_filtering_movielens/](https://keras.io/examples/structured_data/collaborative_filtering_movielens/)
- NCF를 keras로 구현한 예제

[https://www.kaggle.com/code/indralin/movielens-project-1-2-collaborative-filtering](https://www.kaggle.com/code/indralin/movielens-project-1-2-collaborative-filtering)
- SVD를 사용하는데, user-item matrix에서 mean matrix(?)를 빼서 Sparsity를 우회한 행렬에 SVD 적용, 결과로 얻은 세 행렬을 기반으로 내적시킨 값 + 앞에서 뺀 mean matrix를 다시 더해 예측 평점을 구함
- 왜 굳이 mean matrix를 뺏을까? (추정) sparse matrix에 SVD를 적용할 경우, 아래와 같은 문제가 있을 수 있다고 함 [https://stats.stackexchange.com/questions/31096/how-do-i-use-the-svd-in-collaborative-filtering](https://stats.stackexchange.com/questions/31096/how-do-i-use-the-svd-in-collaborative-filtering)
    - 계산 복잡도 ($$O(m*n*min(m,n))$$)
    - 누락된 데이터가 0으로 해석되어 결과 왜곡

[https://simonezz.tistory.com/23](https://simonezz.tistory.com/23)
- 파이썬 surprise 라이브러리의 SVD 함수 사용한 예제. 


### 실시간 추천 서비스에서 model-based CF 구현 시 고민

- 위 예제는 대부분 memory-based CF의 느낌이 있음. 새롭게 유입되는 유저의 선호도 데이터에 대한 예측을 할 때, 위 예제를 적용하려면 결국 기존 User-item matrix에 concat 시켜서 다시 svd를 구해야 함
    - 다르게 보면 새로운 사용자에게 아이템 추천을 해야할 때 마다 모델을 재학습시킨다는건데 계산적으로 비효율 아닌가
    - user-item matrix가 얼마나 더 들어와야 모델을 재학습시키는 것이 효율적일지에 대한 문제?
- (추정) 학습된 사용자 특성 행렬($$U$$)과 아이템 특성 행렬($$V$$)가 있다고 할 떄, 새로운 사용자 선호도 벡터 $$r$$이 주어진 상황
    - 이 사용자에 대한 추천은 결국 해당 사용자의 잠재 특성 벡터 $$u$$를 찾는 문제와 같음 (이걸 찾으면 여기에 아이템 특성 행렬를 곱해 선호도 높을 것이라 예상되는 아이템을 추천할 수 있음)
    - $$u$$가 존재한다고 하면, $$uV$$는 $$r$$과 유사해야함. $${min}_u norm(r - uV)$$ 라고 한다면
    - $$r$$을 $$V$$에 선형 회귀시켜 구한 계수 = $$\hat{u}$$
    - $$\hat{u}V$$의 벡터에서 선호가 높은 n개 아이템을 추천
- surprise 라이브러리의 SVD() 함수는 어떻게 새로운 사용자에 대한 아이템을 추천하는 것일까 (_chatGPT 답변 정리했는데 못 믿겠음. 공식 문서 봐야할 것 같다_)
    - 전체 데이터셋의 평균 평점을 기본 예측값으로 사용
    - 사용자와 아이템 바이어스: SVD()는 사용자와 아이템의 바이어스 (편향)도 함께 학습합니다. 이 바이어스는 해당 사용자나 아이템의 평점이 전체 평균에서 얼마나 떨어져 있는지를 나타냅니다. 새로운 사용자나 아이템에 대한 예측을 생성할 때, 이 바이어스를 전체 평균에 더하여 예측값을 조정합니다.
    - 잠재 특성: 만약 새로운 사용자에 대한 아이템의 평점을 예측하려면, 이 사용자의 잠재 특성을 알아야 합니다. 그러나 이 사용자의 잠재 특성은 학습 데이터에 포함되지 않았기 때문에 직접적으로 알 수 없습니다. 이 경우, SVD()는 전체 사용자의 평균 잠재 특성을 사용할 수 있습니다 (반대의 경우에도 마찬가지입니다).
    - 결합: 위의 세 가지 구성 요소 (평균 평점, 바이어스, 잠재 특성)를 결합하여 새로운 사용자나 아이템에 대한 평점 예측을 생성합니다.


### hybrid-system의 시초?

- CBT, CF, Hybrid system의 대표적인 모델 하나씩 구현해보면 재밌을 것 같음 (실시간 추천에 들어간다는 가정)

### 궁금한 추천 모델? 추천 시스템? 방향

- 필터 버블을 느끼게 되면 유저는 서비스를 이탈하는 것 같음 (개인적 경험)
- 이런 한계를 보완하는 여러 방법 중 serendipity를 어떻게 구현하는지
- 동적인 추천 알고리즘을 제공하면 필터 버블을 자각한 유저의 이탈을 막을 수 있지 않을까
    - 웹에서 사용자가 직접 추천 알고리즘의 여러 paramters를 조정할 수 있는 시스템
    - 예를 들어 '다양성'를 1~100까지 스크롤로 보여주고, 기본 값이 50이라 했을 때 유저가 100으로 늘리면 100의 입력값을 받아서 이걸 모델에 적용
- **스터디 참여한 동기가 된 고민. 추천 시스템 이해가 부족해서 막연한 아이디어가 오히려 혼란만 가중시킬 우려가 있을 것 같음... 일단 기본적인 모델 구현 + 서비스 안착시킨 뒤 고민해봐도 될 문제같다**



***

- mean matrix 빼는 이유: bias 컨트롤하고자. 사용자 편향을 잡아주려고
- SVD 사용 이유: sparisty 때문. 기존 매트릭스 그대로 사용하면 비효율적. 압축시킨다는 의미에서 SVD 차용하는 것도 있음.
- Memory-based에서 실시간 추천하는 방법? 논문 찾아볼 것 (호텔 예시)
- 추천 시스템에서 애초에 제대로 된 실시간 interaction 이 어려움
    - 실시간에선 MAB(Multi-armed bandit)를 많이씀. 빠르다는 특징
- 모델 재학습 주기? 모델 학습시키는데걸리는 시간 (ex. 4시간)
- 필터 버블



