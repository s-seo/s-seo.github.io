---
layout: default
title:  "SE, portal 검색 노출"
parent: Git
nav_order: 6
---

***

# - Google 검색에 노출

구글 검색해서 내 사이트가 나오게 하려고 지금 일주일 넘게 시도 중이다. 방법은 `robot.txt`와 `sitemap.xml`을 만들어 Google search console에 등록하면 되는데, 구글에서 `sitemap.xml`을 인식하지 못해 계속 시도하는 중이다. 

`유형`이나 `상태`가 각각 *알 수 없음*, *오류, 가져올 수 없음 등*으로 뜨는 것이 처음 며칠 동안은 일반적이라고 했으나 나의 경우는 며칠이 지나도 해결이 안되는 것 같다. 나름대로 원인을 파악해보니 일단 나와 같은 **just-the-docs** 테마를 쓰는 사람은 `site.posts`가 아니라 `site.html_pages`로 바꿔야 한다. 

```
---
layout: null
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  {% for post in site.html_pages %}
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

아래 `lastmod`나 `changefreq`, `priority`


검색해보니 just-the-docs 테마를 쓰는 사람 중 나와 같은 문제가 발생한 사람이 있다. <https://jjuhey.github.io/docs/trouble-shooting/sitemap-missing/> 이 분이 해결한 방식대로 sitemal.xml을 다시 제출했으나 여전히 인식하지 못하는 상황이다. 



***

# - Naver





***

# - Daum



