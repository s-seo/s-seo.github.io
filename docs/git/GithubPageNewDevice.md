---
layout: default
title:  "새로운 장치에서 시작"
parent: Git
permalink: /Git/GithubPageNewDevice/
nav_order: 4
date: 2022-08-17
last_modified_date: 2022-08-17
---

***

# Github blog 로컬 웹페이지 호스팅 및 깃헙 커밋

github.io 레포의 HTTPS 주소를 복사한 뒤, cmd에서 아래 명령어를 입력한다.

```
$ cd 원하는 경로
$ git clone 복사한 주소
```

해당 폴더를 열면 내가 github에 커밋시킨 파일이 다 로컬로 복사된 것을 확인할 수 있다. [Ruby를 설치하고, jekyll을 다운받는 것](https://s-seo.github.io/blog/first-post/)은 블로그 재료를 만들기 위함인데 이미 그 재료는 만들어서 github에 업로드했으니 따로 설치할 필요는 없다. 다만 작업의 편리성을 위해선 로컬 웹페이지 호스팅이 필요하고, 이룰 위해선 Ruby와 jekyll이 필요하다. 따라서 로컬에서 작업하고자 한다면 아래 명령문을 실행해서 내 jekyll theme에 필요한 gems를 설치한다.

```
$ bundle # 또는 bundle install
```

포스트를 새로 만들거나 수정한게 있으면 아래 명령어를 입력하는 작업이면 github blog 관리에 충분하다.

```
$ git add 파일명 또는 .
$ git commit -m '메시지'
$ git push -u origin master
```


***

# Trouble shooting - 한글 경로 에러

포맷을 한지 일주일 정도 지났는데, 이제 슬슬 포스트를 본격적으로 쓰다보니 포스트 수정 사항을 깃헙에 바로 푸쉬하는게 번거로워 다시 로컬 웹페이지 호스팅을 돌리려고 시도했다. 근데 이걸로 거의 하루를...! 그것도 면접 전날을 통째로 날려먹었다. 결과적으로 해결법은 **경로를 잘 살펴보는 것**이다. 이 문제를 해결하려고 노력하면서 `jekyll`이나 `bundle`에 대해 배운 것도 있어 정리해본다. 먼저 `$ bundle install`을 실행하면

> *There was an error parsing `Gemfile`: There are no gemspecs at C:/Users/baoro/OneDrive/바탕 화면/Blog/s-seo.github.io. Bundler cannot continue.*

이와 같은 에러 메시지가 뜨는데, 이 경우는 `Gemfile`에 `gemspec`을 지운 뒤 `gem "minimal-mistakes-jekyll"`을 추가하면 해결된다. [Minimal-mistakes 공식문서](https://github.com/mmistakes/minimal-mistakes)에는 이후 `$ bundle`을 실행한 뒤 `_config.yml` 파일에 `theme: minimal-mistakes-jekyll`를 추가하면 된다고 나와있다. 보통은 이제 `$ jekyll serve`를 실행하면 `jekyll`이 내장하고 있는 서버를 동작시키고 이를 로컬 PC에서 확인할 수 있다. 이걸 좀 더 업그레이드 시킨 것이 `$ bundle exec jekyll serve`인데 bundler는 Ruby에서 필요한 gem을 관리, 추적할 수 있어 디버깅(?)에 유용한 기능을 가지고 있다. 이 경우 뜨는 에러는 3가지 경우가 있는데 먼저,

- `Invalid CP949 character`

이건 윈도우 OS에서 jekyll을 사용할 때 UTF-8 인코딩을 사용한다면 발생할 수 있는 에러다. 일종의 OS와 콘솔창의 호환 문제라고 생각할 수 있는데 cmd에 [`$ chcp 65001`을 입력](https://aisiunme.github.io/jekyll/2018/07/25/troubleshooting-in-jekyll-serve/)하면 cmd 화면이 `Active code page: 65001`로 넘어가면서 `$ jekyll serve`를 실행시킬 수 있다. 또는 한글이 쓰인 파일을 직접 경로를 역추적해서 찾아낸 뒤 수정하는 [방법](https://min9nim.github.io/2018/08/jekyll-sass/)도 있다.


- `you don't have kramdown-parser-gfm`

이건 Gemfile에 `gem "kramdown-parser-gfm"`을 추가하면 된다. 에러 메시지에도 나와있듯이 해당 gem을 설치하면 해결되는 문제다. 그럼 Gemfile이 아래와 같아질 것이다.

```
source "https://rubygems.org"

gem "minimal-mistakes-jekyll"
gem "kramdown-parser-gfm"
```

- `Internal Error: Invalid UTF-8`

여튼 위 프로세스를 마치면 로컬 웹페이지를 호스팅할 수 있다는건데, 내 경우에는 

```
$ bundle exec jekyll serve
```

를 실행하면

> *Conversion error: Jekyll::Converters::Scss encountered an error while converting 'assets/css/main.scss': Internal Error: Invalid UTF-8*


위와 같은 에러가 떴다. `Internal Error: Invalid UTF-8`이라는 에러는 구글링해도 안나와서 머리를 꽁꽁 싸맸는데, 예전에도 이런 스트레스, 짜증을 경험한 적이 떠올랐고 그 때 문제의 원인은 폴더 경로에 한글이 들어가 있었다는 점이 생각났다. 이번에 포맷하면서 시작하자맞 자동적으로 Onedrive를 사용하게 됐는데 경로에도 Onedrive가 들어갔고, Onedrive에서 사용하는 Desktop은 `바탕화면`이라는 한글로 경로에 포함되어 있었다. 이 점이 문제가 되어 듣도보도 못한 에러를 발생시킨 것이다. 그래서 `바탕화면`-`속성`-`위치`에 들어가서 경로를 `기본값 복원`으로 되돌렸고, 이 때 리디렉션이 이뤄지면서 기존 파일을 새로운 경로에 복사시킨다. 시간 좀 걸리는데, 막상 복사가 다 안돼도 어차피 Onedrive 경로는 남아있으니 다시 돌아가서 복사해주면 된다. 처음엔 파일 날라간 줄 알고 진짜 울뻔했다ㅠㅠ 마지막으로 확실하게 하기 위해 `제어판`-`프로그램 제거`에서 `Microsoft Onedrive`를 제거해주면 된다. 이제 다시 cmd에서 바뀐 경로로 들어가 `$ bundle exec jekyll serve`를 실행하면 로컬 웹페이지이 호스팅되는 것을 확인할 수 있다. 정말 너무 허무하지만 열심히 노력한 시간이었다.. 내 하루ㅠ
