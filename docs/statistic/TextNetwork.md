---
layout: default
title:  "Text Network"
parent: Statistic
# nav_order: 97
---

***

이 포스트에서는 파이썬을 사용한 텍스트 분석에 대한 전반적인 프로세스를 다루려고 한다. 내가 나중에 참고하기 위해서! 

***

# KoNLPy

텍스트 데이터를 전처리한다면 먼저 토큰화(tokenization)와 품사 태깅(POS)를 떠올릴 수 있다. 영어는 `NLTK`라는 파이썬 패키지가 있고, 한국어는 `KoNLPy`라는 패키지가 있다. 이 패키지를 통해서 사용할 수 있는 형태소 분석기는 Okt(Open Korea Text), 메캅(Mecab), 코모란(Komoran), 한나눔(Hannanum), 꼬꼬마(Kkma)가 있다. 영어와 달리 한국어 NLP에서 형태소 분석기를 사용하는 것은 단어 토큰화가 아니라 형태소 토큰화(morpheme tokenization)를 수행함을 의미힌다. 

```python
!pip install konlpy

from konlpy.tag import Okt  

okt=Okt()  
```

만약 Java를 모르는 사람이 위 코드를 실행하려고 하면 에러가 뜬다.

> *No JVM shared library file (jvm.dll) found. Try setting up the JAVA_HOME environment variable properly.*

`KoNLPy` 패키지는 JDK(JAVA), JPype1, KoNLPy의 순차적인 설치가 필요한데, 앞의 두 개를 생략했기 때문에 발생하는 에러다. 먼저 JDK 설치를 위해 [Oracle installation](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)로 가서 설치한 파이썬 비트에 맞는 JDK를 다운로드 받아 설치한다. 나의 경우는 `Windows x64` 파일은 다운받았는데, 요새는 오라클 회원가입을 해야 다운받을 수 있다. 설치가 끝나면 jdk가 설치된 경로를 복사해야 하는데, 보통

```
C:\Program Files\Java\jdk1.8.0_301\jre\bin\server
```

위와 같은 경로에 `jvm.dll` 파일이 있다. 복사한 경로를 시스템 환경변수에 추가하면 되는데, 아래와 같이 `JAVA_HOME`으로 저장한다.

![](https://s-seo.github.io/assets/images/post_text_1.PNG) 

이제 다시 커널을 restart 시켜서 `okt=Okt()`를 실행하면 다음과 같은 에러가 뜰 것이다.

> *java.nio.file.InvalidPathException: Illegal char <*> at index 55: C:\Users\baoro\Anaconda3\lib\site-packages\konlpy\java\**

위에서 언급했듯이 JPype1을 설치하지 않았기 때문에 발생한 것이다. [JPype1 installation](https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype)으로 가서 내 파이썬 버전과 윈도우 비트에 맞는 whl을 다운받는다. 나는 `JPype1-1.1.2-cp37-cp37-win_amd64.whl`로 다운받았다. 처음엔 `1.3.0`을 다운받았는데 안먹혀서 `1.1.2`로 설치했다. 이제 이 whl을 설치해야하는데, 파이썬 스크립트가 있는 폴더로 옮기고, 터미널을 열어서 아래 명령문을 입력한다

```
$ cd 옮긴 폴더 경로
$ pip install JPype1-1.1.2-cp37-cp37-win_amd64.whl
```

실행 결과 `Successfully insatlled ~`가 뜨면 된다. 이제 다시 커널을 restart 시켜서 `okt=Okt()`를 실행하면 에러 없이 잘 실행될 것이다.






***

# Text network

a corpus of documents를 network로 표현하는데,

- node : a document
- edge : similiarities between the words used in any two documents

- node : a word
- edge : the regularity with which they co-occur in documents







