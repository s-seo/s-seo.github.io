---
layout: default
title:  "AWS"
parent: Engineering
nav_order: 97
---



AWS ECR (Elastic Container Registry)
- Docker Container의 이미지를 저장하는 Repository 서비스
- Docker hub의 Repository 서비스와 동일한데 차이점은 Docker Private Repository를 구축, 관리하는 역할을 AWS에 맡기는 managed 서비스라는 점
- 장점: 컨테이너 이미지를 S3에 저장하기 때문에 고가용성 + AWS IAM 인증을 통해 이미지 push/pull에 대한 권한 관리가 가능함

IAM registry
- AWS(Amazon Web Service)의 ECR(Elastic Container Registry)을 사용하기 위한 도구
- IAM을 통해 사용자 권한 관리 가능
