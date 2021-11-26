---
layout: default
title:  "Confluence"
parent: Engineering
nav_order: 97
---

크래프톤 입사하고 처음 접해보는 시스템, 프로그램이 많았는데 그 중 하나는 위키(도메인이 wiki로 시작함)였다. 위키라고 하면 흔히 위키백과를 떠올리게 되는데, 크래프톤에서는 이 위키라는 것에다가 모든 보고서, 가이드 등의 문서를 작성, 수정, 보관, 공유하고 있다. 그래서 내가 아는 위키 개념(개방적, 누구라도 수정 가능)과 회사 문서(기밀, 폐쇄성)이 매우 상충되어서 혼란스러웠는데, 이 참에 제대로 정리해보려고 한다.



### 위키

* 위키는 불특정 다수가 협업을 통해 직접 내용과 구조를 수정할 수 있는 웹사이트를 일컫는다

* a hypertext publication collaboratively edited and managed by its own audience directly using a web browser.
* Wikis are enabled by wiki software
* Wikipedia는 wiki-based website 중 가장 크고 잘 알려진 것.



### 위키 소프트웨어 (wiki software, wiki engine)

* 위키 소프트웨어(wiki software)는 웹 브라우저를 사용하여 사용자들 여럿이서 웹 페이지를 만들고 편집할 수 있게 하는 소프트웨어이다. 여러 tools(Confluence, Nuclino, MediaWiki etc.)를 아우르는 범용적인 개념이다. 
* a form of a content management system
* is created without any defined owner or leader
* have little inherent structure
* allow content to be written using a simplified markup language and sometimes edited with the help of a rich-text editor
* 위키 대부분은 협동적으로 개발하는 자유-오픈 소스 소프트웨어다. 즉, R이나 Python처럼 자유롭게 배포하고 발전시키는 소프트웨어인셈. 내가 헷갈렸던 부분은 위키가 하나의 회사라고 생각했던 점이었다. 위키는 회사가 아니라 특정 스타일의 웹사이트를 일컫는다.



### Confluence

- 위키 소프트웨어(a web-based corporate wiki)의 한 종류다. [(wiki hosting services)](https://en.wikipedia.org/wiki/Comparison_of_wiki_hosting_services) 
- Atlassian이라는 회사에서 만든 자바 기반의 상용 위키 소프트웨어다. 크래프톤에서는 Atlassian의 Confluence 라이선스를 구매해서 직접 운영하는 서버에 설치하여 사용하고 있는 것 같다. Jira라는 project and issue tracking 소프트웨어도 Atlassian에서 개발, 판매하고 있는데 이것과 연동(자주 쓰는 기능)시켜 협업할 수 있다.
- Wiki-style이지만, WYSIWYG(What You See Is What You Get)에 가까운 에디터를 제공한다. 



### Why Confluence?

다른 관점에서 접근해보자. 비즈니스가 확장될수록 정보는 쌓여가는데 어떻게 잘 정리할 것인가? 단순히 Google Drive, Dropbox와 같은 cloud storage에 저장은 할 수 있겠지만 공유, 활용, 분석하기엔 번거로울 것이다. 그래서 knowledge sharing tool이란 것이 필요한데 그 중 대표적인 것이 Atlassian Confluence다. Confluence는 2004년에 출시된 online collaboration tool인데, 대부분의 wiki처럼 

* Allows users to collaboratively create, organize, and edit content online
* Related pages can be linked together using internal links

등의 기능을 제공한다. 하지만 

* overengineered, complex, and slow to be used effectively

라는 비판을 받고 있기도 하다. 이에 Nuclino와 같은 대안이 나옴.



### How Confluence?

