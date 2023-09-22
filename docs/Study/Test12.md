---
layout: default
title:  "summary test"
parent: Study
permalink: /study/Test12/
nav_order: 3
date: 2023-09-14
---
TL;DR;
***
- 우분투 패키지 설치 가능한지 확인하기 위해 'sudo apt update' 실행
- 'sudo apt install wget'로 wget 설치
- 설치된 경로에서 'ls -alh'로 설치된 파일 확인 및 권한 설정(chmod +x Miniconda3-latest-Linux-x86_64.sh)
- Miniconda3를 실행시킬 수 있게 됨. 설치는 약간의 타이밍 필요.
- 최종 설치 후 'exit'하여 (base) 표시 확인. 미니콘다의 기본 가상환경(base)이 표시됨.
- 필요한 패키지를 설치하기 위해 파이썬 파일이 있는 경로인 'fc_chatgpt' 경로로 이동.
***



- 먼저 sudo apt update 로 어떤 우분투 패키지 설치 가능한지 확인 (?)
- 다음 sudo apt install wget 으로 설치
- 설치된 경로에서 ls -alh 하면 설치된 파일 확인 가능. 근데 권한 관련 문제 있어서 이거 또 설정해줘야함
- chmode +x Miniconda3-latest-Linux-x86_64.sh
- 이걸하면 이제 이 sh 파일을 실행시킬 수 있음. 설치 은근 타이밍 필요하네
- 여튼 최종 설치하고 exit 하면 앞에 (base) 생긴 것 확인 가능. 미니콘다의 기본 가상환경인 base가 보이는 것
- 파이썬 파일이 있는 fc_chatgpt 경로로 가서 필요한 패키지 설치


