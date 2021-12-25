---
layout: default
title:  "What is Git?"
parent: Github
nav_order: 3
---

컴퓨터 포맷을 한 김에 github을 처음 시작하는 방법도 같이 정리해보려고 한다. 이전 포스팅에서는 git, github이 사용가능하다는 전제 하에 블로그를 시작하는 방법을 정리했다. Github는 버전 관리 시스템 웹호스팅을 맡은 일종의 저장소이자 서비스이며, git은 저장소에 내 resource를 버전 별로 저장, 관리해주는 시스템이다.

## Git이란

![](https://s-seo.github.io/assets/images/post_git_1.png) 
출처: <https://velog.io/@leobit/Git-workflow>

git은 형상 관리 도구(configuration management tool) 중 하나다. 다른 말로 버전 관리 시스템이라고 한다. 소프트웨어 개발에 필요한 소스코드를 효과적으로 관리할 수 있는 무료 공개 소프트웨어다. Open source contribution이 이런 것과 연관된 건가..? 여튼 기존에는 서브버전(SVN)이라는 틀이 있는데 이보다 여러 장점을 갖춘 git으로 많이 넘어온 상태다. 그럼 왜 git이 좋은지?

* 분산형 관리 시스템: 소스코드를 여러 개발 PC와 저장소에 분산해서 저장하기 때문에 한 곳에서 에러가 발생해도 다른 곳의 저장소를 이용해 복원 가능하다. 
* 빠른 속도: 사본을 로컬에서 관리하기 때문에 중앙 서버를 이용하는 SVN에 비해 상대적으로 빠름.
* 병렬 개발: 소스코드를 주고 받을 필요 없이 같은 파일을 여러 명이 동시에 작업할 수 있다. 구체적으로는 브랜치를 나눠(fork) 개발한 뒤, 나중에 merge하는 방식으로 co-developing 할 수 있다.
* 오프라인에서도 버전 관리가 가능하다. 스테이지에 올린다는게 이러한 특징을 만들어내는건가?

그럼 이렇게 버전 관리를 해주는 시스템이란 기술, 프로그램은 잘 알겠는데 이를 실제로 구현시킬 물리적인 공간이 필요하다. 이를 git 웹호스팅 시스템이라고 하며 협업하는 코드를 저장할 수 있고, push, pull request 같은 이벤트에 반응하여 자동으로 작업을 실행해주는 역할을 할 수 있다. 대표적으로 Github이 있으며 GitLab, BitBucket 등이 있다. 관련 용어를 정리해보자.

* `Repository`: 말 그대로 저장소를 의미하며, 모든 히스토리가 담겨져있다.
* `Working Tree`: 특정 시점의 저장소(?)를 의미한다.
* `Staging Area`: 저장소에 커밋하기 전 준비, 점검시키는 공간
* `Commit`: 스테이지에 올라온, 변경된 작업 상태를 저장소에 저장하는 작업
* `Branch`: 어떤 작업이 있다면 현재 작업 상태를 복사하여 저장하는 공간. 브랜치에서 작업 한 후 완전하다 싶을 때 merge한다.
* `Head`: 현재 작업 중인 브랜치를 의미함
* `Merge`: 다른 브랜치의 내용을 현재 브랜치로 가져와 합치는 작업

## Git 설치

[git 설치 사이트](https://git-scm.com)에 들어가 git을 다운받는다. 거의 다 `Next`를 눌러 넘기되, terminal emulator 선택화면에서는 **Use Window's default console window**를 선택한다. 

git을 처음 설치하면 사용할 이름, 이메일을 등록해야 한다. cmd를 실행해서 아래 명령어를 입력하자

```
$ git config --global user.name 사용할이름
$ git config --global user.email 사용할이메일
```



## Git 명령어

`$ git init`: 해당 폴더에 깃을 시작시킴. 해당 디렉토리에 ".git"이란 숨겨진 하위폴더가 생성됨

`$ git status`: 깃의 상태를 출력함. 해당 경로와 관련하여 마스터 브랜치가 존재하는지, 커밋했는지, 커밋할게 있는지. 해당 경로에 만약 깃에서 버전관리하지 않은 파일이 있다면 **Untracked files**라는 리스트로 출력됨. 이전에 커밋했으나 수정한 파일이 있다면 **modified**라고 상태가 나타남.

`$ git add`: 파일을 스테이지로 올린다. 스테이지는 생성, 수정한 파일을 올리는 공간이다. 여기에 파일을 먼저 올려야 저장소로 커밋할 수 있다. 면접 대기실이 있는 것 처럼 파일들 모아서 정렬시키는 역할로 메모리 공간, 시간적으로 효율적인 버전관리가 가능한 것. 이후 다시 `$ git status`를 입력하면 **Changes to be committed**라는 리스트가 출력된다. 개별 파일명을 입력해도 되고, `$git add .`로 모든 파일은 한번에 스테이지로 올릴 수 있다.

`$ git commit -m '메시지'` : 스테이지에 올라온 파일을 저장소로 커밋한다. **n files changed, n insertion**이라는 문구가 출력된다. 이후 `$ git status`를 입력하면 **nothing to commit, working tree clean**이라는 문구가 나와야함.

`$git log`: 커밋한 기록을 확인할 수 있다.

`$git commit -am '메시지'`: git add, commit을 동시에 한다.

`$git diff`: 파일의 수정된 부분을 나타낸다. 즉, 최신 버전의 파일과 수정한 파일의 차이점을 보여주는 것.

* git init으로 깃을 시작한 폴더 내에서 git으로 버전관리하고 싶지 않은 파일들이 있을 수 있다. 이 떄 git init이 적용된 폴더에 **.gitignore** 파일을 만들어 파일목록을 입력하면 된다. **.gitignore** 파일 자체는 버전관리에 포함되지만 파일의 목록에 해당하는 파일들은 버전관리에 포함되지 않게된다.

`$ git restore`: 수정한 파일 되돌리기. ctrl+z와 비슷한 것 같다.

`$ git restore --staged`: 스테이지에 올라간 파일을 취소한다. 

`$ git reset HEAD^^`: 최신 커밋을 취소한다. 커밋이 취소되고 unstaged 되었다는 내용이 출력된다. 여기에 `$ git restore`까지 해주면 파일을 원래 상태로 돌릴 수도 있다.

더 많은 git 명령어는 [git 명령어](https://reddb.tistory.com/147?category=948284)를 참고하면 된다.







