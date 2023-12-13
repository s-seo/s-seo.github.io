---
layout: default
title:  "[Statistics] Item Response Theory"
parent: Study
permalink: /study/ItemResponseTheory/
---

***

# Item response theory

- 개인의 ability level을 측정하고자 할 때, 행운, 문제 난이도 차이 등과 같은 혼동 요인을 최대한 배제하고 응시자의 실력을 정확하게 추정하려는 이론
- 주로 교육심리학에서 아래의 목적으로 사용된다.

1. developing and designing exams, 
2. maintaining banks of items for exams,
3. equating the difficulties of items for successive versions of exams

- 아래의 가정이 필요하다.

1. A unidimensional trait denoted by $\theta$ following $N(0,1)$
2. Local independence of items
3. The response of a person to an item can be modeled by a mathematical item response function (IRF)


***

# Item response function
- the probability that a person with a given ability level ($\theta$) will answer correctly.
- the 3 parameter logsitic model (3PL)

<!-- \begin{aligned}
p_i(\theta) &= c_i + \frac{1-c_i}{1+e^{-a_i(\theta-b_i)}} \\\\\\
\theta: &\text{a latent trait parameter (or ability) of a person}\\\\\\
a_i: &\text{the item discrimination parameter for an item }i \\\\\\
b_i: &\text{the item difficulty parameter for an item } i \\\\\\
c_i: &\text{the guessing parameter for an item }i
\end{aligned} -->

- $a_i$는 로지스틱 곡선의 기울기를 결정한다. 
- $b_i$는 $i$th item의 어려움을 나타낸다. 이 값을 응시자의 latent trait에서 뺀 것을 $X$로 두고, 정답 유무를 $y$로 두어 로지스틱 회귀를 적합시켜 정답 확률을 구하는 것이 기본 원리다. 내 기본 능력에서 문제의 난이도가 높을수록 이 $X$는 작아지고 따라서 정답 확률이 0에 가까워진다. 
- $c_i$는 행운을 반영한 변수다. 우연히 정답을 맞출 확률을 나타내는 실수다. 우연히 정답을 맞추는 사건을 A라고 한다면 3PL을 indication function을 사용해서 아래와 같이 나타낼 수 있다. 이게 더 직관적인 표현인 것 같다.

<!-- \begin{aligned}
p_i(\theta) &= I(A^c)) + I(A) \frac{1}{1+e^{-a_i(\theta-b_i)}} \\\\\\
\text{where } A \sim Bern(c_i)
\end{aligned} -->

