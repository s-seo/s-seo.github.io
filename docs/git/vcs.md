---
layout: default
title:  "VCS"
parent: Git
nav_order: 1
---

***

지금 다니는 회사에선 GitLab을 쓰는데, 사실 이게 정확히 뭔지, git에 기반한 버전 관리 툴이고 github과 유사하지만 기능, 라이센스 면에서 살짝 다르다는 것은 알겠는데 왜 이걸 도입했고, 어느정도까지 활용하고 있는지 등 알려주는 사람이 없어 내가 직접 알아본 것을 정리해보려고 한다.

# Version Control System(VCS, 버전 관리 시스템)

개발이나 분석 프로젝트를 진행할 땐 각자 업무를 나눠서 코드를 개발하거나 문서를 작성한다. 이렇게 만든 코드, 문서를 한 곳에서 통합하여 저장, 수정 할 수 있고, 변경된 기록까지 버전 별로 관리하는 것을 Configuration Management(형상 관리) 혹은 Version Management(버전 관리)라고 한다. 관리 방식에 따라 중앙집중관리식, 분산관리식으로 나눌 수 있는데 각각 대표적으로 사용되는 도구는 SVN, Git이다.

## Central Version Control System(CVCS, 중앙집중형 방식)
Local PC에서 내가 작업한 것들을 remote repository로 바로 commit하거나, update된 것을 받는 방식이다. 단순하고 직관적이지만, 중앙 서버가 죽으면 당장 업무가 불가능하다는 점, 동일한 파일에 대해 여러 사람이 작업하고 있으면 충돌이 발생한다는 점 등의 단점이 있다.

## Division Version Control System(DVCS, 분산관리 방식)
Local PC에서 remote repo로 올리기 까지 몇 단계를 더 추가한 방식이다. 이 때 로컬 저장소라는 개념을 도입한다. 작업 공간을 개개인에게 분산시킨 다음, 거기서 나온 최종 결과물만 원격 저장소에서 합치는 방식이다. 





















