---
layout: default
title:  "포스트 작성"
parent: Git
nav_order: 2
---

***

이번 글에서는 *블로그 포스트 작성 원리와 어떻게 포스트를 작성할 것인지*에 대해 다룬다. 원리는 알아야 응용을 할 수 있기 때문에 작동 방식을 간단하게 적는데 생각보다 재밌다.

***

# 1. Github pages 원리

![](https://s-seo.github.io/assets/images/post2_1.PNG) 
> 출처 : <https://devinlife.com/howto%20github%20pages/github-blog-intro/>

Github pages의 대략적인 관계도를 나타낸 것으로, 블로거 A가 Template/Contents에서 작업한 것을 github에 연동시키는 과정 (git push, git pull)이 있고 작업한 것은 웹사이트에서 보여주는 역할을 Jekyll이 담당한다. Local computer와 github pages에 모두 Jekyll이 그려져 있는데, 전자는 우리가 직접 깔았고, 후자는 github에 원래 깔려져 있기 때문이다. Local에서 작업한 것은 나만 볼 수 있고, github에서 작성한 블로거는 여러 방문자들이 볼 수 있다는 것도 확인할 수 있다. 

그럼 Jekyll이 뭐길래 저런 역할을 하는걸까? Jekyll은 static websites generator라는 Ruby 기반의 프로그램이다. Markdown 파일을 인풋으로 이를 html 파일로 변환시켜 웹사이트를 구축하는 역할을 맡는다. Markdown 파일은 텍스트 파일 포맷 중 하나인데 문법이 다루기 쉬워 (html 보단) 접근성이 좋다. Static website란 사람들이 웹사이트에 접속했을 때 보는게 동일한 경우를 일컫는다. 반대로 dynamic websites란 사용자의 요청에 의해 보여지는게 다른 사이트를 의미한다. Dynamic websites의 github pages를 계획한다면 Django가 있다.

***

# 2. 포스트 작성 방식 : 이론(?)

여기까지 잘 이해했다면 결국 포스트를 작성하기 위해선 md (markdown) 파일을 작성해서 이걸 github에 올리면 된다. 그러면 블로그 글을 작성할 수 있는 두가지 방법을 생각해볼 수 있다.

1. Github에서 직접 포스트를 작성하고 이를 github.io에서 확인
2. 로컬에서 포스트를 작성한 뒤 github에 push하고 이를 github.io에서 확인

첫번째 방법의 단점은 github에서 md 파일을 작성하기 매우 불편하다는 것이다. 이미 너무나 편리한 markdown editor가 많기 때문에 필요성이 없긴하다. 두번째 방법의 단점은 전체 프로세스가 많아서 너무 번거롭고 작업 효율이 떨어진다. 수정 사항이 생길 때마다 업로드하고 사이트에 반영되는 것을 확인하기까지 적어도 수 분은 소요된다. 그래서 우리가 사용할 방식은 **로컬에서 작업한 것을 바로 로컬 웹사이트로 띄워 *실시간*으로 확인하는 방식**이다. 작성하고 싶은 포스트가 생길 때 마다 아래 두 줄만 하면 된다. 아직 실행하지는 말자.

```ruby
$ cd [블로그 repo 저장 위치]
$ bundle exec jekyll serve
```

이러면 localhost:4000 주소가 뜨고 여기로 접속한다면 markdown 파일을 작성, 수정하고 이를 저장했을 때 변동 사항이 바로 웹사이트에 적용되어서 나타나는 것을 확인할 수 있다. 이 때 주의해야 할 점이 있다.


### - Posts 폴더

우리가 작성한 md를 Jekyll이 읽으려면 몇가지 포맷을 갖춰야한다. 그 중 하나는 블로그 주소에 _posts 라는 폴더에 포스트 파일을 저장해야 한다는 것이다.

```ruby
$ cd [블로그 repo 저장 위치]
$ mkdir _posts
$ cd _posts
```


### - YFM (YAML Front Matter) Format

Markdown 파일을 작성할 때 상단에 아래와 같은 내용을 입력해야 한다.

```
---
title:  "Window 환경에서 github.io 시작하기"
excerpt: "흔히 알고 있는 github 블로그를 window 환경에서 만들어보자"

categories:
  - Blog
tags:
  - Blog
---
```

이는 포스트의 신상 정보로써 YFM이라고 한다. 제목, 부제목, 카테고리, 태그 등 다양한 변수를 설정할 수 있다. 


### - 파일명

Markdown 파일을 작성할 때 파일명도 정해진 양식이 있다. *year-month-dat-tilte.md*로 작성해야 한다. ex) *2021-02-18-firstpost.md*


***

# 3. 포스트 작성 방식 : 실습

대략적으로 필요한 내용은 다 다뤘고, 이제 직접 글 하나를 작성해보자. 일단 어떤 편집기를 사용할 것인지에 대해 고민을 했었는데, 안그래도 요새 Kaggle와 Colab을 연동시켜 작업하는 것에 관심이 있어 Colab을 사용해서 github pages를 작성할 수 있을까 고민했었다. Colab이 일단 분석에 필요한 양질의 개발환경을 제공해줘서 코드 돌리기에 적합한 강력한 장점이 있다. 그러나 local에 remote repo 시켜서 작업할 수 있는건지 (로컬 웹호스팅시켜 포스트 편집한걸 실시간으로 확인 가능함) 아니면 오로지 드라이브에서 작업해야하는건지... 후자의 경우라면 아마 또 적합한 colab + github pages 방법이 있을 것 같아 찾아봤었는데 없는 것 같다ㅠㅠ 애초에 colab 사용 목적이 github pages와는 다르기 때문에 어쩔 수 없는 것 같다.

그래서 포스트 작성은 VSCode를 활용하기로 했다. R에서 markdown을 작성할 수 있지만 VSCode가 가독성, UI 편리성 측면에서 살짝 더 좋고, Typora는 내가 바로 봐야할 md를 만들 때는 유용하지만, 내 블로그에 형식에 맞춰 바로 볼 수 있는건 아니기 때문에 VSCode + 로컬 웹호스팅시켜서 작업하는 것이 제일 무난할 것 같다.

### - Visual Studio Code

VScode는 마이크로소프트에서 오픈소스로 개발하고 있는 소스 코드 에디터다. 비슷한 이름의 Visual Studio를 똑같이 마이크로소프트에서 개발, 운영하고 있는데 이건 IDE에 가깝고 VScode는 코드 에디터 목적에 충실하다. <https://code.visualstudio.com/>에 접속하면 바로 아래와 같은 창이 나오고 운영체제에 맞춰 다운받아 쭉쭉 실행하면 된다. 

![](https://s-seo.github.io/assets/images/post2_2.PNG) 

VSCode를 실행하면 거무튀튀한 창이 뜨고 좌측에 5개 아이콘이 있는데 이를 activity bar라고 한다. 

![](https://s-seo.github.io/assets/images/post2_3.PNG)

위 정도로 설명이 가능한데 우리가 주로 쓸 건 explorer 뿐이다... 저번 포스트에서 [username].github.io 라는 github repo를 만들고 이를 로컬에 remote하여 연동시켰었다. 해당 파일의 주소를 복사하자. 그리고 cmd에서 다음의 코드를 실행한다.

```ruby
$ cd [복사한 주소]
$ mkdir _posts
```

그럼 이제 내 로컬 저장소에 _posts라는 폴더가 생겼다. VSCode로 돌아가 _posts 폴더를 클릭하고 

![](https://s-seo.github.io/assets/images/post2_4.PNG)

위 사진의 상단에 보이는 하얀 밑줄 친 부분의 아이콘을 누르면 새로운 파일이 생성된다. 여기에 파일명은 위에서 말한 양식(year-month-day-title.md)대로 입력하고, 최상단에 YFM을 그대로 복붙하여 원하는 타이틀, 태그 등의 변수를 입력한다. 일단 아무 말이나 써보고 저장해보자. 그러면 로컬에서는 일단 내 블로그에 글이 작성된 것이다. 이걸 로컬 웹사이트 호스팅으로 확인해보자. 다시 ,cmd로 돌아가 아래 코드를 실행한다.

```ruby
$ cd [블로그 repo 저장 위치]
$ bundle exec jekyll serve
```

그런 다음 웹브라우저를 켜서 <http://127.0.0.1:4000/>에 들어가면 내 로컬 웹사이트를 확인할 수 있다.


### - Github pages

 그럼 이제 이렇게 작성한 글을 github에 올리고 github pages를 확인해보자. Cmd를 켜서 아래 코드를 실행한다.

```ruby
$ cd [블로그 repo 저장 위치]
$ git add .
$ git commit -m "첫번째 블로그 글 등록"
$ git push -u origin master
```

실행하면 [username].github.io repo에 업로드 된 것을 확인할 수 있다. 이제 블로그에 들어가면 로컬에서 만들었던 웹페이지가 그대로 구현되어 있을 것이다. 


