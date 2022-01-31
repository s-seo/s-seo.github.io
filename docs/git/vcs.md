---
layout: default
title:  "VCS to Github(Gitlab)"
parent: Git
nav_order: 1
---

***

지금 다니는 회사에선 GitLab을 쓰는데, 사실 이게 정확히 뭔지, git에 기반한 버전 관리 툴이고 github과 유사하지만 기능, 라이센스 면에서 살짝 다르다는 것은 알겠는데 왜 이걸 도입했고, 어느정도까지 활용하고 있는지 등 알려주는 사람이 없어 내가 직접 알아본 것을 정리해보려고 한다.

***

가장 근본적이고 쉬운 상황에서 시작해보자. 무언가를 작성해서 변경하고 누군가에게 공유하는 작업 중이라고 가정해보자. 아래와 같은 상황이 발생할 수 있다는 것은 다들 알고 있을 것이다.

![](https://s-seo.github.io/assets/images/post_vcs_1.PNG) 
> 출처: <https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ngyadpr&logNo=110183028824>

내가 변경한게 무조건 옳고 미래에도 이것만 보고 그 이전 기록들은 필요하지 않다면 그냥 '레알 최최최최최최최종'만 남기면 되지만, 실제로는 과거 기록들도 필요한 경우가 많다. (굳이 실무가 아니고 개인 프로젝트 할 때만 해도...) 저 기획자도 그러한 점을 알기 때문에 이런 기록을 남긴 채 '최'를 계속 덧붙이면서 해당 파일을 관리하고 있다. 근데 뭔가 체계적이지 않고, 어떤 부분이 변경되었는지 파악하기 어렵고, 동일한 파일을 여러 사람이 같이 작업할 때 작업본이 충돌되는 경우가 발생할 수 있다. 이러한 의도를 가진 채 단점을 보완하고자 나온 것이 Version Control System(VCS, 버전 관리 시스템)이다. VCS는 비단 코드에만 국한되지 않고 다른 파일에도 적용될 수 있는 개념이다. 우리가 흔히 아는 git은 2005년에 탄생했지만, VCS 자체는 1972년에 source code control system(SCSS)라는 형태로 나왔다고 볼 수 있다. 그럼 VCS가 정확히 무엇이고, 어떤 기능을 수행할 수 있는걸까?

# 1. Version Control System(VCS, 버전 관리 시스템)

개발이나 분석 프로젝트를 진행할 땐 각자 업무를 나눠서 코드를 개발하거나 문서를 작성한다. 이렇게 만든 코드, 문서를 한 곳에서 통합하여 저장, 수정 할 수 있고, 변경된 기록까지 버전 별로 관리하는 것을 Configuration Management(형상 관리) 혹은 Version Management(버전 관리)라고 한다. 관리 방식에 따라 로컬 버전 관리, 중앙집중관리식, 분산관리식으로 나눌 수 있다. 

## 1-(1). Local Version Control System
이름에서 알 수 있듯이 local PC에서 개인이 작업할 때 쓰는 VCS인데 대표적으로 Revision Control System(RCS)라는 도구가 있다. Local PC에 파일을 저장, 관리한다. 파일이 변경되는 부분을 Patch Set이라 하는데, 일종의 특정한 파일 형식으로 저장해서, 파일을 특정 시점으로 변경하고자 할 때 일련의 Patch set을 적용하는 방식으로 버전 관리를 수행한다. 

![](https://s-seo.github.io/assets/images/post_vcs_2.PNG) 
> 출처: <https://git-scm.com/book/ko/v2>

## 1-(2). Central Version Control System(CVCS, 중앙집중형 방식)
이 방식부턴 다른 작업자들과 협업을 고려한 방식이다. 파일을 관리하는 서버가 별도로 있으며 이 서버의 database를 이를 remote repository라고 한다. Local PC에서 내가 작업한 것들을 remote repository로 바로 commit하거나, update된 것을 받는 방식이다. LCVS에 비해 누가 무엇을 했고, 하고 있는지 추적이 가능하고, 개개인의 local DB를 관리할 필요 없이 하나의 서버만 관리하게 되며, 작동 방식이 단순하고 직관적이다. 그러나 중앙 서버가 죽으면 당장 업무가 불가능하다는 점, central DB가 있는 하드디스크에 문제가 생기면 모든 히스토리가 날라간다는 점, 동일한 파일에 대해 여러 사람이 작업하고 있으면 충돌이 발생한다는 점 등의 단점이 있다.

![](https://s-seo.github.io/assets/images/post_vcs_3.PNG) 
> 출처: <https://git-scm.com/book/ko/v2>

## 1-(3). Division Version Control System(DVCS, 분산관리 방식)
Local PC에서 remote repo로 올리기 까지 몇 단계를 더 추가한 방식이다. 이 때 로컬 저장소라는 개념을 도입한다. 즉, 저장소를 히스토리와 같이 로컬 저장소에 복제시킨다. 이렇게 작업 공간을 개개인에게 분산시킨 다음, 거기서 나온 최종 결과물만 원격 저장소에서 합치는 방식이다. 

![](https://s-seo.github.io/assets/images/post_vcs_4.PNG) 
> 출처: <https://git-scm.com/book/ko/v2>

이 중 DVCS의 대표적인 방식이자, 개발자의 필수적인 툴인 Git을 다루려고 한다.




# 2. Git (TBC)

## 2-(1). Git이란?

![](https://s-seo.github.io/assets/images/post_git_1.png) 
> 출처: <https://velog.io/@leobit/Git-workflow>

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

2022년 1월 기준 가장 많이 쓰이는 VCS 툴은 Git, CVS, SVN, Mercurial, Monotone 등이 있다. <https://www.softwaretestinghelp.com/version-control-software/>

- CVS: Concurrent Version System의 준말, CVCS에 기반한 툴.
- SVN: Surversion의 준말, CVCS에 기반한 툴. 
- Mercurial: Git과 마찬가지로 DVCS에 기반한 툴.

* 왜 Git이란 이름을 붙였을까? 뭔가 힙해보이기도 하고 멋지다 참. <https://hbase.tistory.com/56> 이 분의 글에서 어원을 다루고 있는데, 큰 의미는 없이 개발자 본인의 성격을 그대로 나타낸 것 같다.






## 2-(2). Git 실습

보다 더 자세하고 방대한 내용은 <https://git-scm.com/book/ko/v2>를 참고하자. 

### Git 설치

[git 설치 사이트](https://git-scm.com)에 들어가 git을 다운받는다. 거의 다 `Next`를 눌러 넘기되, terminal emulator 선택화면에서는 **Use Window's default console window**를 선택한다. git을 처음 설치하면 사용할 이름, 이메일을 등록해야 한다. cmd를 실행해서 아래 명령어를 입력하자

```
$ git config --global user.name 사용할이름
$ git config --global user.email 사용할이메일
```

### Git 명령어

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

더 많은 git 명령어는 [git 명령어](https://reddb.tistory.com/147?category=948284)를 참고하자.



# 3. Github (TBC)

Git과 Github은 무엇이 다를까? 이 질문에 답하려면 Git을 어떻게 사용하는지 부터 알아야 한다. 


Git 호스팅 서비스를 정리한 글 <https://www.git-tower.com/blog/git-hosting-services-compared/>




# 4. GitLab 

Github와 마찬가지로 Git 저장소를 호스팅하는 SaaS(Software as a Service)다. Github와의 비교는 <https://insight.infograb.net/blog/2021/02/05/gitlab-vs-github/>를 참고할 수 있는데 요약하자면, 둘은 기능 면에서는 큰 차이 없으나, 지원 서비스(언어, 비용 등)라는 실무 관점에선 GtiLab이 좀 더 우수하다는 것이다.

GitLab은 Git 서버를 직접 설치해서 사용하기 때문에 Github과 달리 서버 유짓보수 비용이 추가로 발생한다.



## Group

단어 그대로 사용자들의 모임이다. 개발 회사에 속해서 여러 프로젝트와 사원을 관리할 때 해당 사용자와 프로젝트를 group으로 묶어 관리한다.


## Project

쉽게 말하던 Git repo로 코드를 저장하고, 수정, 리뷰하는 곳이다. 모든 프로젝트는 한 사용자나 한 그룹에 속하게 되는데, 그룹에 속한 프로젝트는 해당 그룹에서 사용자들에게 부여한 권한 레벨에 따라 제어할 수 있는 정도가 다르다. 내가 회사에 처음 입사했다면 당장 나한테 그룹에 속한 모든 프로젝트를 관리하게 맡기고 싶진 않기에 낮은 권한을 부여하는 것이 그 예시다.



