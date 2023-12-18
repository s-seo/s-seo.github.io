---
layout: default
title:  "[Github Page][JTD] Custom"
parent: Study
permalink: /study/JustTheDocsCustom
last_edit_time_format: 2023-12-14
---

Just The Docs(JTD) 테마가 search 기능도 있고, 여러모로 UI가 깔끔해서 적용했지만, 좁은 width가 맘에 들지 않아 직접 css 파일을 수정했고, 이를 포함해 몇가지 customizing한 내용을 기록한다.

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

![](https://s-seo.github.io/assets/images/post_justthedocslayout_1.png){: width="1000" height="800" .image-border}

- 위 화면의 빨간 박스를 수정
- 우측 상단의 박스는 config의 aux_links 부분. 적당한 이름과 링크 입력
- 좌측 하단의 박스는 nav_external_links 부분. 이걸 모두 주석 처리하면 안 보임
- 캡쳐엔 표시 안되어 있지만, 하단에 이 문서를 언제 수정했다는 정보가 표시되는데, 이걸 다루는 것이 last_edit_time_format 부분. 초 단위로는 필요 없으니 일 단위로 수정
  - 각 문서 front matter에 last_edit_time_format: 2023-12-13 이런식으로 입력하면 일단위까지 표시됨
- Footer에 'Edit this page on Github' 부분도 필요없으니 config 내 gh_edit_link: false 로 입력하면 됨


### 색깔 변경

![](https://s-seo.github.io/assets/images/post_justthedocslayout_2.png){: width="1000" height="800" .image-border}

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

![](https://s-seo.github.io/assets/images/post_justthedocslayout_3.png){: width="300" height="200" .image-border}

- 만약 side-bar가 아닌 navigation-bar 색만 변경하고 싶다면,
  - .side-bar 클래스가 아닌 .site-nav, header, footer 클래스에 스타일 적용하는 부분(세 클래스 한번에 적용하는 스타일 부분 있음)에 `background-color: ${color-you-want};` 추가하면 됨

### 사이드바 길이, 여백 조정

![](https://s-seo.github.io/assets/images/post_justthedocslayout_6.png){: width="1000" height="800" .image-border}

- 블로그를 위와 같이 넓게 보고 싶으면
  - ```css
    .side-bar {
      ...
      @include mq(lg) {
        width: calc((100% - #{$content-width}) / 2);
        ...
      }
    }

    .main {
      ...
      @include mq(lg) {
        ...
        min-width: $content-width + $nav-width;
      }
    }
  
    .site-nav,
    .site-header,
    .site-footer {
      ...
      @include mq(lg) {
        width: $nav-width*1.3;
      }
    }
  ```


### 사진 크기 조정, 테두리 부여

- _sass/custom/custom.scss 에 아래 추가

```css
.image-border {
  display: block;
  margin: auto; // 이미지를 중앙에 배치하려면 사용
  border: 1px solid #000; // 테두리 설정, 여기서는 검은색 1픽셀 테두리
}
```

- 아래와 같이 로드하면 됨

`![](){: width="1000" height="800" .image-border}`


### 사이트 타이블 (smseo blog) 스타일 변경

- 내 블로그 타이틀을 좀 더 굵게 표시하고, 박스의 정중앙에 위치하고 싶다
- 모바일에선 타이틀이 교차축에선 중앙, 주축에선 왼쪽 정렬되게 하고 싶다. 안그럼 아래와 같이 살짝 부자연스러움

![](https://s-seo.github.io/assets/images/post_justthedocslayout_5.png){: width="300" height="200" .image-border}


```css
.site-title {
  ...
  font-weight: 700;
  ...
  @include mq(lg) {
    justify-content: center;
  }
}
```
