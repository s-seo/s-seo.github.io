---
layout: default
title:  "[Github Page] 시작"
parent: Study
permalink: /study/GithubPageStart/
---

***

지식 정리 겸 포트폴리오를 만들고자 github blog를 시작했다. Markdown 문서 기반(다루기 쉽다)이고 로컬에서 웹호스팅을 할 때 따라오는 불편함 (24시간 컴퓨터 켜야하고, 에러 모니터링 등)이 없어 매우 유용하다. Github blog를 시작하는 좋은 가이드 글이 많아 나도 몇 개를 참고했지만 **window + 노베이스**인 사람을 위한 글은 없는 것 같아 써본다. 또 통계를 공부하다보니 자연스레 개발자 분들의 글을 많이 접하게 되었는데 이걸 왜 하는지 알려주는 글을 극히 드물다. 그만큼 꼬리를 무는 정보가 많고 다 적기에는 비효율적이기 때문이다. 그래도 난 적어도 왜 하는지, 단순한 단어의 나열으로라도 스스로 납득하고 싶어 직접 글을 작성해본다. 설명하기 전 git이 설치되어 있고 github 계정이 있다고 가정하겠다. 가장 먼저 할 것은 Ruby와 Jekyll을 설치하는 것이다.

***

# 1. Ruby

Ruby는 객체 지향 프로그래밍 언어의 한 종류다. 가독성이 좋아 파이썬과 종종 비교되지만 파이썬은 정형화된 들여쓰기를 요구하는 반면 Ruby는 정형화된 들여쓰기를 요구하지 않는다. 블로그를 만들 때 Ruby라는 언어로 만들어진 Jekyll을 주로 사용하기 때문에 Ruby를 먼저 설치해야한다. <https://rubyinstaller.org/downloads/>에 들어가 

![](https://s-seo.github.io/assets/images/post1_1.PNG) 

위에 보이는 파일 하나를 다운 받으면 된다. 이 때 되도록 버전이 2.2 이상 2.7 이하의 중간 버전을 다운받는게 좋다. 최신 버전은 호환 문제가 발생할 수 있기 때문이다. 
exe 파일은 실행해서 쭉 설치하면 되고 다 설치하면 cmd를 켜서 아래와 같은 결과가 나오는지 확인한다.

```ruby
$ ruby --version
ruby 2.6.6p146 (2020-03-31 revision 67876) [x64-mingw32]
```

***

# 2. Jekyll

Jekyll이란 github에서 Ruby로 개발한 사이트 개발 툴이다. Static website를 구축하기 매우 편리하다는 이점이 있다. Static이라는 것은 내가 만들어 놓은 사이트를 사람들이 와서 보기만 한다는 의미로 이해할 수 있다. 만약 사람들이 직접 사이트를 조정할 수 있다면 dynamic website라는 표현을 쓴다. Jekyll과 bundler 설치는 아래 한 줄이면 된다.

```ruby
$ gem install jekyll bundler
```

Gem은 분산 패키지 시스템(?)으로 Ruby에서 라이브러리 설치할 때 사용하는 도구 개념이다. 


***

# 3. Sample Blog

이제 샘플 블로그를 만들어 앞으로 블로그를 잘 만들 수 있는지 확인해보자. 

```ruby
$ jekyll new [블로그 이름]
```

위 코드를 실행해서 먼저 새로운 블로그를 생성하고

```ruby
$ cd [블로그 이름]
$ bundle exec jekyll serve
```

생성된 블로그로 change directory 한 뒤, bundle exec jekyll serve 명령어를 사용해 로컬 웹페이지를 호스팅 할 수 있다. 그럼 이제 웹브라우저를 띄워 <http://127.0.0.1:4000/>로 이동한다. 에러없이 잘 따라왔다면 아래와 같은 Jekyll의 기본 블로그 화면이 나온다.

![](https://s-seo.github.io/assets/images/post1_2.PNG) 

이렇게 만든 샘플 블로그를 github에 연동시켜 다른 사람들도 내 블로그를 볼 수 있게 만들 수 있다. 그 전에 github 블로그를 시작하는 중요한 요인 중 하나는 깔끔하고 다양한 무료 탬플릿이다. 따라서 탬플릿을 먼저 설치하고 github에 연동시키겠다. 


***

# 4. Jekyll Theme

Jeykell theme는 다른 사용자들이 이미 구축해놓은 탬플릿 모음이다. 이 블로그는 minimal-mistakes라는 테마를 적용했다.

<https://github.com/mmistakes/minimal-mistakes>

위 링크에 들어가 git repo를 clone한다. 저 분이 구축한 모든 파일을 옮기는 것이 목적이기 때문에 zip 파일을 다운받는 등 다양한 접근 방식이 있지만 clone은 기존 history를 모두 가져오기 때문에 유용하다. 주소 복사하기 귀찮으면 아래 코드를 그냥 실행하자. 

```ruby
$ git clone https://github.com/mmistakes/minimal-mistakes.git
```

clone이 끝나면 해당 폴더로 들어가 bundle 명령어를 수행한다. clone을 통해 이쁜 틀을 내 컴퓨터로 가져왔으면, bundle을 실행해서 이 이쁜 틀을 웹호스팅하기 위해 필요한 재료를 받는다. 

```ruby
$ cd minimal-mistakes
$ bundle
```

설치가 끝나면 아래 명령어로 웹호스팅한 뒤 아까처럼 로컬 주소를 확인해보자.

```ruby
$ bundle exec jekyll serve
```

아래와 같은 화면이 나오면 성공이다. 앞에서 만든 샘플 블로그와 달리 이쁘다.

![](https://s-seo.github.io/assets/images/post1_3.PNG) 


***

# 5. Github Pages

앞서 말했듯이 탬플릿 설치했으니 이제 이걸 github에 연동시킬 차례다. 먼저 github에 블로그 용 repository를 생성해야 한다. 이 때 github에서 정한 규칙이 있는데 repositary name은 [username].github.io로 정해야 블로그로 인식한다. 

![](https://s-seo.github.io/assets/images/post1_4.PNG) 

위와 같이 new repo를 생성하면 된다. Github에 저장소로 팠으니 이제 이 저장소와 내 컴퓨터의 로컬 사이트를 연동시키기만 하면 된다. 먼저 위에서 다운받은 탬플릿의 폴더명이 minimal-mistakes로 되어 있을텐데 이걸 [username].github.io 로 바꾼다. 그리고 아래 명령어를 실행해 [username].github.io 폴더를 remote repositary로 등록한다.

```ruby
$ cd [username].github.io/
$ git remote remove origin
$ git remote add origin https://github.com/[username]/[username].github.io.git
$ git push -u origin master
```

두번째 줄의 remove origin은 우리가 minimal-mistakes를 clone 시켜 가져왔기 때문에 기존의 remote origin을 제거하는 역할이다. 마지막에 push를 했으니 minimal-mistakes theme가 내 [username].github.io에 업로드된 것을 확인할 수 있다. 이제 로컬 주소가 아닌 <https://username.github.io>를 사용해서 내 블로그에 접속할 수 있다. 


***

# 6. Future Works

지금까지 window 환경에서 github pages를 구축하는 방법에 대해 알아봤다. 그러면 이제 github pages에 어떤 파일을 (Markdown) 어떻게 작성해서 (VSCode) 올릴 것인지 살펴보겠다.

***

## 7. References

<https://devinlife.com/howto/>
<https://m.blog.naver.com/hsy2569/221865301644>
<https://zoomkoding.github.io/gitblog/2019/08/15/git-blog-1.html>



