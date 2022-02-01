---
layout: default
title:  "AWS"
parent: Engineering
# nav_order: 97
---

AWS는 Amazon Web Service의 준말인 것은 알았는데, 도대체 여기서 뭘 하길래 엔지니어링 분야에서 필수로 등장하는지 궁금했다. 얼마나 대단하길래 자기네 회사 프로그램을 잘 다룬다는 자격증까지 만들 정도일까

***

# 1. AWS

![](https://s-seo.github.io/assets/images/post_aws_1.PNG) 
> 출처: <https://aws.amazon.com/ko/blogs/korea/>

간단히 말하면 아마존닷컴의 클라우드 컴퓨팅 사업부다. IT 인프라 구축에 필요한 모든 서비스(가상 컴퓨터, 스토리지, 네트워크 인프라 등)을 제공한다. 아마존 전체 매출에선 10%를 차지하는데, 영업 이익 면에선 60~70%를 차지한다. <https://namu.wiki/w/%EC%95%84%EB%A7%88%EC%A1%B4%20%EC%9B%B9%20%EC%84%9C%EB%B9%84%EC%8A%A4?from=Amazon%20Web%20Services> 예를 들어, 내가 데이터 관련 사업을 시작하려는 스타트업 사장이라고 해보자. 쌓여만가는 데이터를 어떻게 저장하고, 처리할 것이며, 분석에 필요한 컴퓨팅 리소스는 어떻게 마련할 것인지 머리가 쪼개질 것이다. 직접 서버를 구매한 뒤, 제공하고자 하는 서비스에 해당하는 서버 소프트웨어를 설치하고, 구축한 서버를 운용해서 클라이언트에게 필요한 정보를 전송할 수 있겠지만 나는 통계 밖에 모른다. 네트워크나 서버 구축 관련 전문지식도 없을 뿐더러, 시간과 비용이 너무 많이 들 것이다. 이 때 클라우드 서비스가 대안이 될 수 있다. 

* 서버, 클라우드에 대한 개념은 <https://s-seo.github.io/docs/engineering/cloud/>를 참고



# 2. 

AWS ECR (Elastic Container Registry)
- Docker Container의 이미지를 저장하는 Repository 서비스
- Docker hub의 Repository 서비스와 동일한데 차이점은 Docker Private Repository를 구축, 관리하는 역할을 AWS에 맡기는 managed 서비스라는 점
- 장점: 컨테이너 이미지를 S3에 저장하기 때문에 고가용성 + AWS IAM 인증을 통해 이미지 push/pull에 대한 권한 관리가 가능함

IAM registry
- AWS(Amazon Web Service)의 ECR(Elastic Container Registry)을 사용하기 위한 도구
- IAM을 통해 사용자 권한 관리 가능




