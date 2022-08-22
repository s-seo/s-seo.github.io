---
layout: default
title:  "JTD SE"
parent: Just The Docs
grand_parent: Git
nav_order: 2
date: 2022-08-22
---

Just The Docs(JTD) 테마의 경우, frontmatter가 일반적인 jekyll theme와 살짝 상이하기 때문에 search engine에 크롤링되기 위해 필요한 sitemal.xml 작성에 있어 다소 시행착오가 필요했다. 관련 과정을 남기고자 한다.

이전에 구글 html 머시기는 만들어서 추가했고, robots.txt와 sitemap.xml 도 만들어놓은 상태. 이전 과정은 [깃헙 블로그를 SE에 노출시키는 방법](https://s-seo.github.io/docs/git/googlesearch/) 를 참고할 것

다만 sitemap.xml을 구글 서치 콘솔에 등록시켜도 크롤링이 안됨. 아마 변수를 제대로 설정안해서 그런듯..? 일단 sitemap.xml 를 수정하려고 함

https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap

여기에 priority, changefreq 는 더 이상 안 읽는 변수라길래, 관련 구문을 지웠고, date 변수값만 어찌어찌 수정해서 아래와 같은 형태로 머지함

```
---
layout: null
---

<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
        xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  {% for post in site.html_pages %}
    <url>
      <loc>{{ site.url }}{{ post.url }}</loc>
      {% if post.date %}
        <lastmod>{{ post.date | date_to_xmlschema }}</lastmod>
      {% else %}
        <lastmod>{{ '2022-01-01' | date_to_xmlschema }}</lastmod>
      {% endif %}
    </url>
  {% endfor %}
</urlset>
```

이후 sitemap.xml 제출했더니 성공. 바로 성공 뜨지 않는댔는데…? 여튼 바로 구글 검색해보니 역시나 뜨진 않는다. 아마 좀 기다려보자. 여튼 구글은 성공했고 이제 네이버인데, 훨씬 간단함.

https://searchadvisor.naver.com/console/board

여기 접속해서 html 파일로 소유확인 -> 요청 -> 사이트맵 제출

https://devinlife.com/howto%20github%20pages/register-search-engine/

빙이나 다음 등 다른 검색엔진을 사용하는 것도 고려해봤는데, 위 블로그 글 읽고 바로 접음


