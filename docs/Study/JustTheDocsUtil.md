---
layout: default
title:  "[Github Page][JTD] Utils"
parent: Study
permalink: /study/JustTheDocsUtil
date: 2022-08-22
---

Just The Docs(JTD)에서 지원하는 여러 스타일 중 자주 쓰는 것들을 모아 정리하고자 함. 마크다운 형식에서 쓰이는 문법 대부분은 여기서도 똑같이 먹히므로 (그게 깃헙 페이지 작동 방식. 더 자세히 말하면 jekyll 자체가 markdown 형식의 문서를 html로 변환해주는 역할을 하기 때문) 참고할 것

## Inline Elements

Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](another-page).

```
Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](another-page).
```

## Labels

Default label
{: .label }

Blue label
{: .label .label-blue }

Stable
{: .label .label-green }

New release
{: .label .label-purple }

Coming soon
{: .label .label-yellow }

Deprecated
{: .label .label-red }

```
Default label
{: .label }

Blue label
{: .label .label-blue }

Stable
{: .label .label-green }

New release
{: .label .label-purple }

Coming soon
{: .label .label-yellow }

Deprecated
{: .label .label-red }
```


## Tables

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

```
| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |
```

## Colors

```
test text color
{: .text-{color}-{number}}

test background color
{: .bg-{color}-[number]}
```

color에는 grey-lt, grey-dk, purple, blue, green, yellow, red가 들어갈 수 잇고,
number에는 000, 100, 200, 300이 들어갈 수 있음

## Font Size

```
test font size
{: .fs-{number}}
```

number에는 1부터 10까지 정수가 들어갈 수 있으며 1은 9px, 10은 42px라고 함

## Font Weight

```
test font weight
{: .fw-{number}}
```

number에는 300, 400, 500, 700이 들어갈 수 있음

## Text Justification

```
test text justification
{: .test-{position}}
```

position에는 left, right, center가 올 수 있음


## Inline Code

Lorem ipsum dolor sit amet, `<inline code snippet>` adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

#### Heading with `<inline code snippet>` in it.

```
Lorem ipsum dolor sit amet, `<inline code snippet>` adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

#### Heading with `<inline code snippet>` in it.
```


## Image Align

설명: `[![](이미지 주소){크기 조절}{정렬}](출처)`

```
[![](https://s-seo.github.io/assets/images/post_vcs_1.PNG){: width="20%" height="20%"}{: .center}](출처)
```

## Panel (?)

ABCDEFGHIJKLMNOPQRSTUVWXYZ
{: .fs-5 .ls-10 .bg-grey-dk-000 .text-grey-dk-300 .code-example }

ABCDEFGHIJKLMNOPQRSTUVWXYZ
{: .fs-3 .ls-10 .bg-grey-lt-200 .text-grey-dk-300 .note }

페이지 끝까지 펼쳐지는 패널도 지원해주는 것 같다. 

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
{: .fs-5 .ls-10 .bg-grey-dk-000 .text-grey-dk-300 .code-example }

A paragraph
{: .fs-3 .ls-10 .bg-grey-lt-200 .text-grey-dk-300 .note }
```


***

ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
{: .fs-5 .ls-10 .code-example }


ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz dddddd
{: .fs-5 .ls-10 .bg-grey-dk-000 .text-grey-dk-300 .code-example }

A paragraph
{: .fs-3 .ls-10 .bg-grey-lt-200 .text-grey-dk-300 .note }

```markdown
{: .note }
A paragraph
```


테마 수정 방법 (크롬 기준)

F12 -> inspect -> 우측 Styles에 마우스 오버 -> 온오프 토글이 있어 눈으로 확인 후 해당 파일, 라인에 가서 수정하면 됨 

