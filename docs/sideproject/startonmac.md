---
layout: default
title:  "Mac에서 개발환경 구축"
parent: Side Projects
nav_order: 1
date: 2022-08-22
---

사이드 프로젝트를 진행하기 전, 정말 백지 상태의 노트북에서 각종 프로그래밍 툴을 설치하는 과정을 기록해서 나중에 새로운 기기에서 다시 시작할 때 참고하조자 함


맥에서 하고자 하는 것
1. 데이터 파이프라인 구축하여 실시간 데이터 수집
2. 수집한 데이터로 이상 탐지 모델링
3. 깃헙 블로그 관리



Python3 설치

python으로 코딩할 것 이므로 Python3를 설치했고
GitHub blog를 관리할 것이기 때문에 Git을 먼저 설치, 그리고 GitHub을 설치

맥에 git을 설치하기 위해 Homebrew 설치 (https://brew.sh/)
homebrew로 git 설치 (https://git-scm.com/download/mac)

로컬에서 깃헙 페이지 사용을 하려면, 당연히 로컬에서 깃헙 페이지를 관리하는데 필요한 재료들을 다운 받아야 함. 그게 jekyll 이고, jekyll을 쓰려면 ruby가 필요함

만약 내가 로컬 환경에서 깃헙 페이지는 안 사용하고, 깃헙에 push해서 웹 상에서만 보길 원하면 jekyll, ruby 등은 설치할 필요가 없음

일단 vscode로 내 원래 깃헙 페이지 레포를 클론해서 로컬에 옮긴 다음, 이 클론을 로컬 환경에서 띄워야 함

1. 맥에 내장된 ruby 2.6.3 은 버림 (있어도 보안상 이유로 jekyll 설치가 안됨)
2. rbenv라는 ruby version 관리자 설치해서 시스템 루비가 아닌 외부 루비를 설치해서 jekyll 환경 구축 가능
3. Brew 를 사용해 rbenv, ruby-build 설치
4. rbenv install [루비 버전]
5. 설치한 env 속 루비를 local에 안착시켜야함: rbenv local [루비 버전]
6. Jekyll은?
7. Jekyll의 dependecies가 있음. 블로그 테마마다 다름. 이 dependencies는 Gemfile에 모아서 관리하고 있음. 그럼 Gemfile에 있는 dependencies를 한번에 다운로드하면 편하겠네? 그 다운로드 해주는 패키지가 bundler임. 
8. Gem install bundler
9. Bundler 패키지의 bundle 명령어를 사용해서 Gemfile 내 dependencies를 다운로드 할 수 있음
10. 이 때 Gemfile은 Jekyll 사이트 디렉토리에 있기 때문에 cd 로 이 디렉토리로 이동한 다음, bundle install 을 실행해야 함
11. 동일한 디렉토리에서 bundle exec Jekyll serve를 실행하면 로컬 웹페이지 호스팅 완료
12. 그럼 내가 매번 깃헙 페이지 수정할 때마다 이 짓을 반복해야하냐? 아님
13. 내가 설치한 rbenv로 이동 -> 거기서 내 jekyll 사이트 파일이 있는 로컬 디렉토리로 이동한 뒤 바로 호스팅 가능함

n번째 블로그 포스팅일 때 마다 위 작업을 반복해야 하는지?
    1.  eval "$(rbenv init - zsh)"  이 명령어를 실행하면 jekyll 명령어가 먹힘. 이게 뭐길래?
    2. evel 명령은 따옴표 안의 구문을 강제로(?) 실행하는 느낌
    3. Rbenv init - 명령어를 실행하면 초기화 스크립트가 나옴. rbenv를 사용하려면 초기화가 항상 필요하기 때문에 이 명령어를 사용해야 함
    4. 그럼 이 명령어를 터미널 킬 때 자동으로 실행하게끔 추가할 수 없을까? 
    5. 그게 환경변수 설정이고, 맥에서 환경변수 설정하는 것은 .zshrc에 아래 구문 추가하면 됨
        1. export PATH="$HOME/.rbenv/bin:$PATH"
        2. eval "$(rbenv init - zsh)"
    6. 추가하는 방법은 여기 참고 https://d-dual.tistory.com/8
    7. 추가 후 업데이트 한 내용 바로 적용하려면 source ~/.zshrc 실행하거나 그냥 터미널 끄고 다시 켜도 됨

Jekyll site scaffold in PATH

Jekyll 공식문서를 따라하면 필시 오류가 발생하니 참고..


——————————  이제 내 원래 깃헙 페이지 레포를 클론시킬 단계

1. 로컬에 클론 & vscode에 연동
2. 터미널 해당 경로에서 bundle install 로 필요한 Gem 다운
3. Gemfile에 gem: ‘jekyll-sitemap’ 추가한 뒤 다시 bundle install
4. Bundle exec Jekyll serve 로 로컬에서 웹페이지 호스팅 완료



—————————— 커밋 되는지 확인

Git 설치하고 처음에 username, email 등록안하면 git commit 에서 경고 뜸. ‘우리가 알아서 너 시스템에 등록된 user.name, user.email 가져다 쓸거다~ 이상있으면 이렇게 변경해라~’ 하는데 변경하는게 은근 귀찮음 (변경 - 커밋) 처음부터 그냥 잘 등록하는게..

다음에 push 하려고 하면, 

krafton@PUBG-bhlim2 s-seo.github.io % git push -u origin master 

fatal: cannot run /private/var/folders/bs/w1vq8wl96gb4twlddw0nss2c0000gn/T/AppTranslocation/53340CC7-69E1-4A0C-8ED1-8D812B6CE770/d/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass.sh: No such file or directory

이런 에러가 발생함. 그리고 username, password 등록하라고 뜸.
이건 내가 깃헙 레포의 hTTPS로 git clone 시켰기 때문인건데, 그냥 깃헙에서 https로 git clone, pull, push하는 경우 username, password를 입력하게끔 설정해놓았음. https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls

여기서 password는 PAT인데, 이건 따로 발급받아야 해서 귀찮다.. https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

여튼 발급받은 토큰은 아래와 같음
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

이거 그냥 터미널에 복붙하면, 붙여넣은지는 안 뜨는데, 정상적으로 Push 된다.. 깃헙 레포 가보니 커밋 내용 잘 반영된거 확인됨


