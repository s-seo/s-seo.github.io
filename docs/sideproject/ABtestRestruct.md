---
layout: default
title:  "A/B test 재구성"
parent: Side Projects
permalink: /sideprojects/ABtestRestruct/
date: 2023-07-28
---

***

회사에서 진행했던 A/B test를 회고하고, 부족했던 부분을 보완해서 다시 분석해보는 것이 목적

***

## A/B test 분석, 결과 전달에 필수적으로 들어가야 할 내용

- 가설 탐색
- 실험 진행 여부 결정
  - 이 가설을 검증하는데 A/B test가 꼭 필요한지?
    - 비즈니스 임팩트는 있는지?
    - 비즈니스 임팩트가 있는데, 불확실성이 존재함을 확인했는지?
    - 불확실성? 기존에 존재하지 않은 새로운 기능이 추가될 때 (과거 데이터가 없으니 판단 어려움)
- 실험 설계
  - 실험 타켓
    - 어떤 유저에게 test를 진행할지?
    - 어떻게 A/B를 나눌지?
  - 지표
    - 실험을 통해 어떤 지표를 개선하고 싶은지?
    - Primary, Secondary, Guardrail Metric은 무엇?
    - MDE를 설정했는지?
  - 실험 기간
    - 언제, 어느 기간 동안 진행할지?
    - 유의미함이 검증될 수 있는 샘플 수는 무엇이고, 그에 따라 책정된건지?
    - 샘플 책정 시 MDE를 고려했는지?
    - 강의에선 보통 2주가 필요하다고 함
    - 프로모션 등 외부 요인이나 계절성 존재하는 기간 제외되었는지?
  - 실험 방식
    - 빈도주의 접근. 어떤 통계 검정 방식을 사용할 것인지?
  - 멘탈 시뮬레이션을 했는지
    - 실험이 잘 되었을 때 / 안되었을 때 어떤 행동을 할까?
    - 의사 결정할 수 없는 실험 결과일 경우 어떤 행동을 할까?
  - 실험을 위한 데이터 로그 설계
- 기능 배포: 데이터 잘 들어오는지 확인, 결과 분석 준비
- 실험 분석
  - 지표 확인
    - 가드레일 지표는?
    - Primary metric은?
    - P 값은
  - 결과 해석
    - 초두 효과(Primary effect), 신기 효과(Novelty effect) 등의 현상이 나타났는지?
  - 실험 결과가 애매하다면, 사후 분석을 진행했는지?
    - Segment 분석 (주로 유저 정보 기반)
    - A/A test는 시도해봤는지? (트래픽만 분할하고 화면 그대로 두고 실험 진행)
  - 종합해서 실험 종료 판단
    - decision tree와 비슷한 방식으로 실험을 종료시켰는지?
- 실험 회고: 회고 및 이후 action plan 수립
- 기타
  - 실험이 진행되는 기간 사내 전파했는지? 마케팅이나 CS에 전파해서 실험에 영향 받는 이슈 있으면 바로 확인 필요
  - 실험에 대한 내용 잘 기록했는지 (다음 분석을 위한 토대)
  - 조직에 lesson learned 잘 공유했는지
  - 실험이 많아질 것을 대비해 분석 자동화를 고려했는지
    - 스크립트를 자동화 염두에 두고 코딩해볼 수도 있고
    - 실험 플랫폼 도입할 것을 건의해볼 수도 있고

***

## A/B test 1: 인게임 재화 충전 모달 A/B test

- 21년 11월에 진행
- 충전 모달에 표시되는 상품 금액은 모두 달러
- 충전 모달 퍼널

| 퍼널 1                                       | 퍼널 2                                       | 퍼널 3                                       |
|----------------------------------------------|----------------------------------------------|----------------------------------------------|
| ![](https://s-seo.github.io/assets/images/post_ABtestRestruct_1.png){: width="400" height="200"} | ![](https://s-seo.github.io/assets/images/post_ABtestRestruct_2.png){: width="400" height="200"} | ![](https://s-seo.github.io/assets/images/post_ABtestRestruct_3.png){: width="400" height="200"} |


- 발단: 국가별 퍼널 전환율 차이가 남을 데이터 통해 확인
  - 왜 전환율 차이가 날까?
    - 추측 1 : 실제로 결제해야 하는 금액을 정확히 인지한 시점에 이탈이 발생한다.
    - 추측 2 : 스팀의 충전과정이 불편하기 때문에 이탈한다.
- 가설: G-Coin 충전 모달에서 자국통화로 예상결제 금액을 보여주면 전환율이 높아지지 않을까? (NA 지역 외에서)
- 실험 설계
  - PC 플랫폼 대상
  - 타겟 유저: 마지막 OS언어가 중국어 간체 zh_CN인 유저
  - A/B 구분 방법: account_id 첫글자가 0, 1, 2, 3, 4, 5, 6, 7이면 A, 나머지는 B
  - 확인하려는 지표: G-coin 충전모달의 전환율
  - 일정: 21년 9월에 10일 동안 진행

- 테스트하려는 UI

| 기존                                       | 변경                                       |
|--------------------------------------------|--------------------------------------------|
| ![](https://s-seo.github.io/assets/images/post_ABtestRestruct_4.png){: width="400" height="200"} | ![](https://s-seo.github.io/assets/images/post_ABtestRestruct_5.png){: width="400" height="200"} |


- 분석
  - 가설
    - 귀무가설: A 그룹과 B 그룹 간 전환율은 통계적으로 유의미한 차이가 없다
    - 대립가설: A 그룹과 B 그룹 간 전환율은 통계적으로 유의미한 차이가 있다
  - 검정 방법: 비율 검정, 카이제곱 검정

- 결과
  - 기존 UI(달러만 표시)에 비해, 자국 통화를 같이 표시한 경우, 충전모달에서 전환율이 낮아지고(약 10%p), 스팀 결제 단계에서 전환율이 높아졌다(약 9%p)
  - 그룹 간 전환율은 통계적으로 유의미하게 차이가 있다.
    - 보다 정확히는, 차이가 없다고 보기엔 주어진 데이터(전환율 차이)가 너무 강력한 반증이다.
    - = 추측 1을 어느정도 뒷받침함
  - 스팀 결제가 불편했다면, 스텀 결제 단계에서 전환율이 높아지지 않았을 것 →  유저들이 스팀 결제 시스템을 불편하다고 느끼진 않는다.
    - = 추측 2에 대한 반증

## 회고 (생각나는 것들만)

- 지표를 하나만 봄
- MDE 설정 없음
- 샘플 수 계산 없이 실험 기간 잡음
- 일부 유저도 아닌 전체 유저 대상이었던 것 같음...
- 멘탈 시뮬레이션 무 (결과 안 좋으면 당연히 롤백~ 끝! 이었고, 이후 사후분석을 진행할 생각 없었음)
- 로그 설계는 필요없었음. 패스
- 애매한 실험 결과인데, segment 어찌 나눠보긴 했으나 전달력이 떨어졌음 (결과 해석하면서 나도 무슨 말 하는지 몰랐던 기억이..)
- decision tree와 같이 정형화된 의사결정 방식이 아니라, 그냥 주먹구구 식으로 결과 전달하고, 흐지부지 된 것으로 기억남


***

# 재구성

총 두 개 문서 작성 필요: A/B 테스트 설계 문서, 결과 분석 문서

## GCoin 충전모달 A/B Test 설계 문서

- 가설 탐색
  - 목표: UI/UX 관점에서 지코인 상품 구매 전환율 증가
  - 현재 상황:
    - 지코인을 충전하는 모달의 퍼널 전환율이 국가마다 차이 있음
    - 달러 국가권에선 높은 전환율을, 그 외 통화권에서는 낮은 전환율
  - 가설: 지코인 충전 모달에서 자국 통화로 예상 결제 금액을 보여준다면, 달러 비사용 국가권에서의 최종 전환율이 높아질 것

- 실험 진행 여부 결정
  - 이 가설을 검증하는데 A/B test가 꼭 필요한지
    - 비즈니스 임팩트는 있는지
      - _최종 전환율을 높인다면 매출이 증가할 것으로 기대해볼 수 있음. 그러나 자국 통화를 띄우는 퍼널2에서 이탈이 높아진다면, 전환율 증가분이 상쇄될 수도 있음_
      - _당장 전환율 증가분이 매출 상승으로 이어지지 않더라도, 제공하는 프로덕트에서의 사용성 개선이 이뤄진다면, 추후 매출이 증가하는데 걸림돌을 없애는 것과 같음_
    - 비즈니스 임팩트가 있는데, 불확실성이 존재함을 확인했는지?
      - _비즈니스 임팩트는 있다고 보이나, 기존에 없던 기능 & 데이터가 필요해서 불확실성이 존재함 -> 실험 필요_

- 실험 설계
  - 실험 타켓
    - 어떤 유저에게 test를 진행할지?
      - _비달러권 국가 중 CN 유저 대상_
      - _왜 CN 유저만? 가장 큰 파이를 차지하는 것도 있고, 다양한 국가의 다양한 통화를 모두 실험 때 반영하는 것은 리소스 크다고 판단. 두가지를 고려해 위안화만 사용할 수 있고 임팩트 큰 중국 유저 대상으로만 진행_
    - 어떻게 A/B를 나눌지?
      - _접속할 때 언어가 중국어 간체인 유저_
      - _실험 기간 동안 OS 언어가 변경되지 않은 유저 대상_
      - _account_id 앞글자가 특정 집합에 속하면 A, 아니면 B로 5:5 비율로 배분_
  
- 지표
  - 실험을 통해 어떤 지표를 개선하고 싶은지? MDE는?
    - Primary: 최종 구매 전환율 (MDE 10%)
    - Secondary: 충전 모달 체류 시간 (MDE -10%)
      - 유저가 고민했어야 할 문제를 제공함으로써 유저 경험 개선을 시키는 영향도 있을 것이라 생각함
      - 이게 드러나는 지표로 모달에서의 체류 시간을 선정
    - Guardrail: 충전 팝업에서 이탈율 - 최종 구매 전환율 (MDE는 10%p)
      - 최종 구매 전환율을 높이는 것이 목적이라 이탈을 감내해야 하긴 하는데, 최종 전환율보다 이탈이 높아지는 것은 막아야 함
      - 이탈 유저 수 - 최중 구매 유저 수 는?

  
- 실험 기간
  - 언제, 어느 기간 동안 진행할지? _21년 9월 8일 ~ 17일_
  - 유의미함이 검증될 수 있는 샘플 수는 무엇이고, 그에 따라 책정된건지?
    - 비율 검정이 필요하고, 단측 검정임을 감안했을 때 sample size 구하는 공식은, 
    - _애초에 검정하려는 효과가 커서 적은 수의 샘플만 필요하다고 나옴. 저 기간 동안 충분한 유저 수 수집될 것으로 예상_

![](https://s-seo.github.io/assets/images/post_ABtestRestruct_6.png){: width="300" height="100"}

![](https://s-seo.github.io/assets/images/post_ABtestRestruct_7.png){: width="300" height="100"}

  - 샘플 책정 시 MDE를 고려했는지?
    - _이건 어떻게 하는걸까_
  - 프로모션 등 외부 요인이나 계절성 존재하는 기간 제외되었는지?
    - _해당 사항 없는 것 확인_

- 실험 방식
  - 빈도주의 접근. 어떤 통계 검정 방식을 사용할 것인지? _검정이랑 베이지안 둘 다 해보면?_

- 멘탈 시뮬레이션
  - 실험이 잘 되었을 때 / 안되었을 때 어떤 행동을 할까?
    - ![](https://s-seo.github.io/assets/images/post_DataLiteracy_8.png){: width="600" height="400"}
  - 의사 결정할 수 없는 실험 결과일 경우 어떤 행동을 할까?
    - _테스트와 달리 실제 기능 개발에는 더 큰 리소스 필요 (여러 국가 환율 반영해야 하기 때문)_
    - _환율 데이터 수집부터, 데이터 무결성, 정합성 검증 및 데이터 파이프라인 구축 외 백, 프론트 개발 필요_
    - _애매한 결과일 경우, 롤백하는 것이 적절_
  - 실험을 위한 데이터 로그 설계
    - _이미 심어져 있어 별도 로그 설계, 개발 불필요_

***

## GCoin 충전모달 A/B Test 분석 문서

- 실험 분석
  - 지표 확인
    - Primary = 최종 전환율
      - A: 0.3
      - B: 0.29
    - Secondary = 충전 모달 체류 시간
      - A: 6.8초
      - B: 8.9초
      - 5% 단위로 모든 백분위수 살펴봤는데, B에서 체류 시간이 대체로 2~4초 높음
    - Guardrail = 최종 전환율 - 충전 모달 이탈율
      - A: 0.3 - 0.26 = 0.04%p
      - B: 0.29 - 0.43 = -0.14%p

- 결과 해석
  - _가드레일 지표가 B안에서 마이너스.. 성공 지표는 MDE보다 낮은 차이.. 심지어 B안에서 더 낮아짐_
  - 검정 결과? _검정까지 갈 필요가.._
  - 실험 결과가 애매하다면, 사후 분석을 진행했는지?
    - Segment 분석 (주로 유저 정보 기반)
    - A/A test는 시도해봤는지? (트래픽만 분할하고 화면 그대로 두고 실험 진행)
  - 종합해서 실험 종료 판단
    - _위 decision tree에 따라 충분한 데이터 쌓였지만, 가드레일 지표 하락 & 성공 지표 하락으로 롤백 결정_

- 실험 회고: 회고 및 이후 action plan 수립
  - 교훈? _위안화를 표시함으로써 유저 행동에 유의미한 변화를 일으키긴 했는데, 그게 최종 전환율 증가로 이어지기는 어려움_
  - 시도해볼만한 사후 분석
    - _충전 모달에 유입되는 경로에 따라. 현재는 크게 두가지 있음_
    - _지코인 가격을 처음 접한 유저 대상으로만. 지코인 상품 자체는 고정적이라 기존에 구매했던 유저는 어느정도 위안화에 익숙해서 B안에 별다른 영향이 없었을 것_

---

## A/B test 스터디 회고

소감
- 아는 만큼 보이는 것처럼, a/b test의 전반적인 프로세스를 직접 계획하고 분석하니, 봐야 할 지표가 그려지는 경험이 신기했음
- 프로젝트 내내 '그 떄 이렇게 했더라면, 그 떄 이 결과값을 전달했더라면..' 중얼거림. 후회가 많이 남긴한데, 그만큼 반성 & 성장 많이 한 것 같음
- a/b test 자체에 대한 기획, 기술적인 피드백, 평가가 있었어도 좋았겠지만, 이런 기회를 통해 직접 무언가를 해서 남겼다는 것에 큰 의의가 있음

아쉬운 점
- 테스트 자체에 대한 통계적 지식이 더 완벽했으면 ()
- 여러 a/b test 플랫폼을 직접 활용해보는 기회가 있었으면 더 좋았을 듯
  - 그 플랫폼에서는 어떤 통계적 기법을 사용하는지 탐구하는 것도


