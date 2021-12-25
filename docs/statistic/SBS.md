---
layout: default
title:  "Semantic Brand Score"
parent: Statistic
nav_order: 97
---

## 1. Introduction

Semantic brand score (SBS) 는 text data를 기반으로한 brand importance 측정 방법이다. 꽤 오래 전부터 있었을 것 같은 개념이지만 의외로 2018년에 나왔다. 이전에는 주로 설문을 사용해 brand importance를 파악했는데, 이 경우 biased된 집단으로부터 왜곡된 결과를 얻을 수 있다는 큰 단점이 있다. SBS는 brand와 관련된 모든 유형의 text data에 적용가능하다. 또 brand 뿐만 아니라 어떠한 유형의 keywords의 strength를 파악할 수도 있다. 


## 2. Basic Concept

SBS에서는 brand importance를 **brand prevalance, diversity, connectivity**라는 세가지 지표의 단순합으로 나타낸다. 이 세가지 지표는 각각 다음의 의미를 갖는다. 

- Prevalance : brand가 얼마나 언급되는지 (the extent to which a brand name is utilized)
- Diversity : brand가 얼마나 다양한 단어들과 연관되어 있는지 (heterogeneous textual associations)
- Connectivity : brand가 단어를 연결시키는 hub로서의 역할 정도 (embedded deeply at the core of a discourse)

그럼 이 세가지 지표를 어떻게 계산할까? 먼저 text data에 적합한 preprocess를 적용하고, word co-occurence network를 구축한다. 이 network는 word에 해당하는 node와 각 node를 잇는 link로 구성되는데, 만약 A 단어가 B 단어와 within a range of five words이면 link가 생성되는 원리다. 이러한 range를 co-occurrence range라고 하며 window와 비슷한 개념이다.


## 3. Calculation

i번째 단어를 $g_i$로 나타낼 때, 

$PREV(g_i) = \frac{f(g_i)}{totW}$

$DIV(g_i) = \frac{d(g_i)}{n-1}$

$CON(g_i) = \sum_{j < k} \frac{d_{jk}(g_i)}{d_{jk}}$

로 계산한다. $f$는 빈도수를 나타내는 함수이며 $d$는 degree를 의미하고, $d_{jk}(g_i)$는 $g_j$에서 $g_k$를 연결하는 가장 짧은 경로 중 $g_i$를 포함하는 경로의 개수를 의미한다. SBS는 위 세가지 지표를 정규화시켜 더한 값이다.

$SBS(g_i) = \frac{PREV(g_i) - \bar{PREV(g_i)}}{sd(PREV(g_i))} + \frac{DIV(g_i) - \bar{DIV(g_i)}}{sd(DIV(g_i))} + \frac{CON(g_i) - \bar{CON(g_i)}}{sd(CON(g_i))}$

본고에서 future work으로 different constant weighting을 제시하긴 한다. 


## 4. Python Code

<https://towardsdatascience.com/calculating-the-semantic-brand-score-with-python-3f94fb8372a6>를 참고했다. 

SBS + sentiment analysis와 python 실습을 다루겠다.






## References

[1] Fronzetti Colladon, A. (2018). The Semantic Brand Score. Journal of Business Research, 88, 150–160. <https://doi.org/10.1016/j.jbusres.2018.03.026>

[2] Calculating the Semantic Brand Score with Python <https://towardsdatascience.com/calculating-the-semantic-brand-score-with-python-3f94fb8372a6>




