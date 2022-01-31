---
layout: default
title:  "SE, portal 검색 노출"
parent: Git
nav_order: 6
---

***

검색 엔진이나 포털에 어떤 키워드를 검색했을 때 관련 내 블로그 포스트가 검색되고 싶어하는 상황을 가정하자.

***

# Google 검색에 노출

깃헙과 구글은 독립적인 회사다. 깃헙 페이지로 작성한 글을 구글에서 검색이 되게 하려면 이 둘을 연결지어야 하는데, 그 역할을 하는 것이 `sitemap.xml`과 `robots.txt`다. 

## sitemap.xml

웹크롤링 봇이 *크롤링할 수 있는* 웹사이트의 접근 가능한 페이지 목록이다. 아래와 같은 기능을 한다. (출처: <https://sanghyuk.dev/blog/2/>)

- 웹사이트의 웹페이지를 계층별로 구분지어 웹사이트의 전체 구조를 보여주며, 검색엔진의 크롤링 로봇들이 크롤링 작업에 유용

- sitemap.xml 파일을 사용하면 사이트 및 콘텐츠 구조를 Google 및 기타 검색엔진에 손쉽게 제출 가능

- 검색엔진에 크롤링해야하는 URL을 알려줌으로써 색인을 생성하는 방법과 색인을 생성하는 방법을 제어

jekyll theme를 사용해 웹사이트를 만들었다면 ruby 기반으로 만들어진 것이기 때문에 `gem install jekyll-sitemap`을 실행하여 플러그인을 사용해 `sitemap.xml`을 생성할 수 있다. 다만 jekyll 기반의 github pages를 만든 것이라면 해당 플러그인을 사용할 수 없어 수동으로 `sitemap.xml`을 만들어야 한다. jekyll theme 기반의 깃헙 페이지는 대부분 아래와 같이 작성하면 대부분 인식되는 것 같다. 깃헙 repo의 root 경로 (config와 동일한 경로)에 아래의 내용으로 `sitemap.xml`을 만든다. 

```
---
layout: null
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  {% for post in site.posts %}
    <url>
      <loc>{{ site.url }}{{ post.url }}</loc>
      {% if post.lastmod == null %}
        <lastmod>{{ post.date | date_to_xmlschema }}</lastmod>
      {% else %}
        <lastmod>{{ post.lastmod | date_to_xmlschema }}</lastmod>
      {% endif %}

      {% if post.sitemap.changefreq == null %}
        <changefreq>weekly</changefreq>
      {% else %}
        <changefreq>{{ post.sitemap.changefreq }}</changefreq>
      {% endif %}

      {% if post.sitemap.priority == null %}
          <priority>0.5</priority>
      {% else %}
        <priority>{{ post.sitemap.priority }}</priority>
      {% endif %}

    </url>
  {% endfor %}
</urlset>
```

sitemap에는 해당 url에 대한 부가적인 정보를 설정할 수 있는 옵션도 제공한다. `lastmod`, `changefreq`, `priority`가 그 옵션인데, `lastmod`는 마지막으로 수정한 시간, `changefreq`는 해당 포스트이 변경 주기, `priority`는 해당 포스트의 우선 순위 정도로만 이해하면 된다. 각 docs의 YAML에 아래와 같이 sitemap 옵션을 추가하면 자동으로 인식한다. YAML은 jekyll theme마다 다르니까 아래 형식을 무조건적으로 복붙하면 에러가 발생할 수 있다. 

```
---
layout: post
title:  "제목"
date:   2016-03-14 12:00:00 
lastmod : 2016-03-15 12:00:00
sitemap :
  changefreq : daily
  priority : 1.0
---
```

Page build가 되면 `[username].github.io/sitemap.xml`으로 접속해서 [sitemap.xml](https://s-seo.github.io/sitemap.xml)와 같은 화면이 나오면 성공이다. 




## robots.txt

웹크롤링 봇이 웹사이트에 방문해서 크롤링할 때 참고하는 정책을 명시해놓은 파일이다. 이 파일에서 위에 기울인 말과 같이 크롤링 할 수 있다는 정책을 표시한다. 보통 아래와 같이 작성해서 `sitemap.xml`과 같은 경로에 업로드한다. 

```
User-agent: *
Allow: /

Sitemap: http://[uername].github.io/sitemap.xml
```


## Google Search Console

내 블로그 repo에 검색 엔진 등록에 필요한 파일을 다 업로드했다면, 이제 이것들을 제출할 차례다. [Google Search Console]<https://developers.google.com/search#?modal_active=none>에 접속하여 
`속성추가` - `URL 접두어` - 내 블로그 주소 입력한다. 이 때 html로 인증하는 방식을 선택해서 다운받은 html 파일을 깃헙 페이지 repo에 푸쉬한 뒤 인증된 것을 확인하다. 다음으로 `색인` - `Sitemaps` - 새 사이트맵 추가에 `sitemap.xml`을 입력해서 제출하면 된다.







## sitemap.xml 인식 오류

구글 검색해서 내 사이트가 나오게 하려고 지금 일주일 넘게 시도 중이다. 방법은 `robot.txt`와 `sitemap.xml`을 만들어 Google search console에 등록하면 되는데, 구글에서 `sitemap.xml`을 인식하지 못해 계속 시도하는 중이다. 지금(2022-01-01) 이 상태다.

![](https://s-seo.github.io/assets/images/post_googlesearch_1.png) 

`유형`이나 `상태`가 각각 *알 수 없음*, *오류, 가져올 수 없음 등*으로 뜨는 것이 처음 며칠 동안은 일반적이라고 했으나 나의 경우는 며칠이 지나도 해결이 안되는 것 같다. 해결 방법을 찾다가 나와 같은 **just-the-docs** 테마를 쓰는 사람([jjuhey](https://jjuhey.github.io/docs/trouble-shooting/sitemap-missing/))을 찾았는데, `site.posts`가 아니라 `site.html_pages`로 바꿨어야 했다. 또 `lastmod`나 `changefreq`, `priority`는 크게 중요하지 않은 것 같다. 저 분이 해결한 방식인 [sitemap2.xml](https://jjuhey.github.io/sitemap2.xml)을 보면 `lastmod`와 `changefreq`가 xml에 들어가지만, 이 분의 docs에는 sitemap의 하위 인자로서 저 값이 (모든 문서에) 들어가지는 않는다. `lastmod`는 거의 모든 문서에 들어가 있는 것 같긴한데 `changefreq`가 없는데 무슨 소용... 그리고 어차피 `null`값이면 default 값을 넣게끔 설정이 되어있다. 따라서 이 부분은 문제가 되지 않는 것 같고, 그나마 고친 부분이 있다면 `config`의 `url`에서 quotation mark를 제거한 것..? 왜냐면 sitemap.xml에서 `site.url`이 들어가는데 여기에 쌍따옴표가 있으면 제대로 인식이 안되기 때문이다. 이런 부분들을 고쳤는데도 여전히 인식하지 못하는 상황이다.ㅠㅠ 어차피 구글에서 크롤링 봇으로 url을 인식하는데 길게는 몇 달이 걸린다고는 하니... 이쯤해두고 기다려보기로 했다. 만약 몇 달이 지나도 인식이 안됐을 경우,

- 모든 docs에 sitemap 하위 인자로 `lastmod`, `priority`를 넣어보거나
- sitemap.xml을 for loop로 돌리는게 아니라 <https://www.xml-sitemaps.com/>에서 직접 sitemap.xml을 따서 제출해보는 방식

을 시도해보자. 아래는 여러 sitemap.xml 주소다.

- <https://github.com/JinyongJeong/JinyongJeong.github.io/blob/master/sitemap.xml>

- <https://github.com/wayhome25/wayhome25.github.io/blob/master/sitemap.xml>

- <https://github.com/JJuhey/jjuhey.github.io/blob/master/sitemap2.xml>

- <https://github.com/swift-man/swift-man.github.io/blob/main/sitemap.xml>




***

# Naver

Naver와 다음에 등록하려면 RSS feed를 아래와 같이 작성해서 root 디렉토리에 `feed.xml` 파일을 생성한다. 

```
---
layout: null
---
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{{ site.title | xml_escape }}</title>
    <description>{{ site.description | xml_escape }}</description>
    <link>{{ site.url }}{{ site.baseurl }}/</link>
    <atom:link href="{{ "/feed.xml" | prepend: site.baseurl | prepend: site.url }}" rel="self" type="application/rss+xml"/>
    <pubDate>{{ site.time | date_to_rfc822 }}</pubDate>
    <lastBuildDate>{{ site.time | date_to_rfc822 }}</lastBuildDate>
    <generator>Jekyll v{{ jekyll.version }}</generator>
    {% for post in site.posts limit:30 %}
      <item>
        <title>{{ post.title | xml_escape }}</title>
        <description>{{ post.content | xml_escape }}</description>
        <pubDate>{{ post.date | date_to_rfc822 }}</pubDate>
        <link>{{ post.url | prepend: site.baseurl | prepend: site.url }}</link>
        <guid isPermaLink="true">{{ post.url | prepend: site.baseurl | prepend: site.url }}</guid>
        {% for tag in post.tags %}
        <category>{{ tag | xml_escape }}</category>
        {% endfor %}
        {% for cat in post.categories %}
        <category>{{ cat | xml_escape }}</category>
        {% endfor %}
      </item>
    {% endfor %}
  </channel>
</rss>
```

[네이버 웹마스터 도구](https://searchadvisor.naver.com/)에 접속해서 깃헙 블로그 주소를 등록하는데 search console과 마찬가지로 `사이트 소유 확인`을 위해 html을 다운받아 root 경로에 업로드한다. 다음으로 RSS feed를 제출해야 하는데, `요청` - `RSS 제출` - `[github pages url]/feed.xml`을 입력한다. 또한 `요청` - `사이트맵 제출` - `[github pages url]/sitemap.xml`을 입력한다.


***

# Daum

[다음 검색 등록](https://register.search.daum.net/index.daum)에 접속해서 `등록` - `블로그 RSS 등록` - `블로그 URL`에 깃헙 블로그 url을 입력하면 된다.

