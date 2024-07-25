---
layout: post
title:  "AWS 기반 Github archive 데이터 ETL 파이프라인 구축"
parent: Projects
permalink: /project/destudyproject1/
date: 2024-07-25
last_modified_date: 2024-07-25
---

# 배경

- 회사에서 데이터 업무를 하다보면 엔지니어링 쪽 다룰 일이 많다.
- 이참에 데이터를 직접 수집, 전처리 후 적재하는 ETL 파이프라인을 구축해보고 싶었다.
- 실무에서 GCP 보단 AWS를 주로 사용하기 때문에 AWS의 여러 솔루션을 사용해보는 것도 목적

# 파이프라인 개요

깔끔한 도식화는 차치하고 줄글로 풀어 설명해보자면,
- AWS Lambda 레이어 위에서
    - 파이썬 google 모듈의 bigquery를 사용해 깃헙 아카이브 데이터를 쿼리
    - 전처리한 데이터를 json으로 변환
    - json 데이터를 s3에 파케이로 업로드
    - 슬랙 웹훅을 걸어 업로드 결과를 슬랙 채널에 전송
- 위 과정을 AWS Eventbridge로 스케줄링
- VSC 등에서 boto3 모듈로 s3에 접근
- 파케이 파일의 json 데이터를 가져와 데이터프레임으로 변환 후 분석

# 트러블 슈팅 - 람다 내 파이썬 패키지 로드

- 람다 자체에는 파이썬의 여러 모듈이 설치되어 있지 않기 때문에 필요한 모듈을 직접 설치해야 한다.
- 나의 경우 아래 모듈이 필요했다

```
import json
import boto3
import pandas as pd
from google.cloud import bigquery
import os
from io import BytesIO
from datetime import datetime, timedelta
from collections import defaultdict
import requests
```

- 이 중 pandas, google-cloud-bigquery는 따로 설치를 해줘야 하는데, 람다에선 패키지 설치가 까다롭다
- 다행히 위 두 패키지는 누군가 공유한 레이어가 있어 이걸 설치해주면 쉽게 해결됐다
    - https://api.klayers.cloud/api/v2/p3.11/layers/latest/ap-northeast-2/html

# 트러블 슈팅 - pandas dataframe이 아닌 json으로 전처리

- 람다 레이어가 제공하는 리소스 자체가 작다보니 (프리 티어..) pandas로 처리할 경우 테스트가 매번 실패했다
- 좀 더 가벼운 json으로 처리하게 함으로써 해결했다

# 트러블 슈팅 - 깃헙 아카이브 데이터 크기

- 하루치 깃헙 아카이브 데이터를 쿼리해도 oom 에러가 발생한다
- extract query에서 필터를 몇가지 걸어서 해결했다
- 만약 실무에서 쓰일 데이터 마트를 구축하기 위해 필요한 컬럼, 레코드가 oom 에러를 발생시킨다면 어떻게 할까?
    - 쪼개서 가져올 수 있으면 되지 않을까. 그만큼 자주 실행시켜줘야 하는 번거로움이 있겠지만 리소스를 돈주고 증가시킬 필요는 없을 것 같다는 짧은 생각

# 결론 및 배운점

- 깃헙 아카이브 데이터 자체가 매일 업데이트 되는 양질의 데이터 소스라 파이프라인 구축하는 것이 어렵지 않았다.
    - 더 까다로운 시나리오를 다뤄보고 싶다. 데이터가 매우 크거나, 클 수 밖에 없는 상황?
- AWS는 알려진 자료가 많아 수월한 것도 있었다. GCP로도 구축해봐도 재밌을 것 같다.
- EventBridge의 경우 Airflow의 기능을 단순화시킨 버전 같다고 느꼈다. 내가 원할 때 이 스케줄을 돌린다거나, 백필과 같은 상황에선 Eventbridge가 그다지 좋은 선택은 아닌 것 같다.
- 이렇게만 해도 비용이 전혀 안든다
- GCP에서 region 잡아서 가져오는 데이터와 정합할지 체크해볼 필요는 있다.
- ETL을 람다 내 한 스크립트에서 모두 처리하는데, DE 관점에서 이 방식이 어떤 장단점이 있을까
    - 생각나는건 디버깅 어렵거나, 특정 함수 실패하면 전체 파이프라인 중단되는 정도?
- 여러 토큰, 키 등을 secret manager 등으로 안전하게 관리해보는 것도 좋은 경험인데, 여기선 못했다.
    - 그나마 구글 빅쿼리 토큰(json 파일)을 s3에 보관해서 가져오는 방식으로 구현했다.
- 7월 한 달은 파이프라인 돌게 해놨다. 이걸 기반으로 추천 모델 학습, 추론도 해볼 계획

![](https://s-seo.github.io/assets/images/post_destudyproject1_1.png){: width="500" height="300" .image-border}

