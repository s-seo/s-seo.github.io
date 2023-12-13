---
layout: default
title:  "[Github Page][JTD] Layout Custom"
parent: Study
permalink: /study/JustTheDocsLayout
last_edit_time_format: 2022-08-22 13:01:01
---

Just The Docs(JTD) 테마가 search 기능도 있고, 여러모로 UI가 깔끔해서 적용했지만, 좁은 width가 맘에 들지 않아 직접 css 파일을 수정했고, 이를 포함해 몇가지 customizing한 내용을 기록한다.

## layout.scss

각 클래스에 어떤 것을 지웠고(주석 처리), 추가했는지 주석으로 설명함

```
.side-bar {
  z-index: 0;
  display: flex;
  flex-wrap: wrap;
  background-color: $sidebar-color;

  @include mq(md) {
    flex-wrap: nowrap;
    position: fixed;
    width: $nav-width-md;
    height: 100%;
    flex-direction: column;
    border-right: $border $border-color;
    // align-items: flex-end; // 사이드바에 있는 항목을 임의로 정렬시키지 않고, default(여기선 중앙 정렬)로 설정
  }

  @include mq(lg) {
    // width: calc((100% - #{$nav-width + $content-width}) / 2 + #{$nav-width}); 
    width: 14%; // 사이드바의 width를 직접 값 지정하여 조정
    min-width: $nav-width;
    margin-left: 14%; // 사이드바가 너무 왼쪽에 붙어 있는 것도 눈이 피로하기 때문에 어느정도 떨어지게 만듦
  }
}
```

```
.main {
  @include mq(md) {
    position: relative;
    // max-width: $content-width; // 이걸 지움으로써 width를 default(전체 화면 넓이)로 조정
    margin-right: 14%; // 전체 화면 넓이로 조정하되, 우측, 좌측에 margin 부여
    margin-left: $nav-width-md;
  }

  @include mq(lg) {
    // margin-left: calc(
    //   (100% - #{$nav-width + $content-width}) / 2 + #{$nav-width}
    // );
    margin-left: 28%;
  }
}
```


```
.site-title {
  @include container;
  flex-grow: 1;
  display: flex;
  height: 100%;
  align-items: center;
  padding-top: $sp-3;
  padding-bottom: $sp-3;
  // color: $body-heading-color; // 기본 색깔이 너무 옅어 지우고 아래 굵기 및 사이즈 변경
  font-weight: 700;
  @include fs-5;

  @include mq(md) {
    padding-top: $sp-2;
    padding-bottom: $sp-2;
  }
}
```

## custom.scss

사진 파일 정렬하는 기능이 없어 아래 직접 클래스를 추가했다. 

```
// center align class

.center {
  display: block;
  margin: auto;
}
```

## CI Error Issue

위와 같이 layout.scss를 직접 손본 뒤 커미샇면 Github actions가 실행 안되고 에러난다. 원인은 (당연히) 내가 css나 sass 같은 페이지 스타일 관련 변수를 멋대로 조정했기 때문이다. (테스트에서 에러나는게 당연하다...) 복잡하게 생각할 것 없이 workflow에서 보이는 에러, 경고 메시지 보면서 몇몇 관련된 파일 직접 수정하면 해결된다. 그 외 bundle 문제는 yml 파일 내 bundle:2.1.4 를 설치하도록 설정했는데, 특정 버전을 직접 명시시켜주니 해결된다. 정확히는 깃헙 페이지 레포에 .github -> workflows -> ci.yml에 들어가서 `gem install bundler`가 포함되어 있는 모든 구문을 아래와 같이 변경하면 된다.

```
jekyll/builder:latest /bin/bash -c "gem install bundler:2.1.4 && chmod -R 777 /srv/jekyll && bundle _2.1.4_ install && bundle exec jekyll build && bundle exec rake search:init"
```


***

## JTD 2023-12-13 버전 커스텀 from start to end

### _config.yml 수정

- title 등 초반 정보는 알아서

![](https://s-seo.github.io/assets/images/post_justthedocslayout_1.png){: width="1000" height="800"}

- 위 화면의 빨간 박스를 수정
- 우측 상단의 박스는 config의 aux_links 부분. 적당한 이름과 링크 입력
- 좌측 하단의 박스는 nav_external_links 부분. 이걸 모두 주석 처리하면 안 보임
- 캡쳐엔 표시 안되어 있지만, 하단에 이 문서를 언제 수정했다는 정보가 표시되는데, 이걸 다루는 것이 last_edit_time_format 부분. 초 단위로는 필요 없으니 일 단위로 수정
  - 각 문서 front matter에 last_edit_time_format: 2023-12-13 이런식으로 입력하면 일단위까지 표시됨
- Footer에 'Edit this page on Github' 부분도 필요없으니 config 내 gh_edit_link: false 로 입력하면 됨


### 색깔 변경

![](https://s-seo.github.io/assets/images/post_justthedocslayout_2.png){: width="1000" height="800"}

- 사이드바 (화면 좌측) 색깔
  - -> _sass/support/_variables.scss 에 `$sidebar-color: $grey-lt-100 !default;` 추가
- 위 캡쳐의 빨간 박스에 있는 글씨의 색깔
  - 본문의 링크와 같이 a 태그가 붙었는데 본문의 링크는 그대로 보라색으로 띄우려고 함
  - -> _sass/support/_variables.scss 에 `$sidebar-color: $grey-lt-100 !default;`, `$main-link-color: $purple-000 !default;` 추가
  - -> _sass/base.scss 에 아래 코드 추가
    - ```css
      .main-content a {
        color: $main-link-color;
        text-decoration: underline;
        
        &:hover {
          color: darken($link-color, 10%);
          text-decoration: none;
        }
      }
    ```
- 가끔 아래와 같이 모바일 버전으로도 확인해주자 (F12 -> 좌측 상단 Toggle device tool bar 클릭)

![](https://s-seo.github.io/assets/images/post_justthedocslayout_3.png){: width="600" height="400"}

### 사이드바 길이, 여백 조정

![](https://s-seo.github.io/assets/images/post_justthedocslayout_4.png){: width="1000" height="800"}

- 블로그를 위와 같이 넓게 보고 싶으면
  - 


