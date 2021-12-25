---
layout: default
title:  "New Theme"
parent: Github
nav_order: 3
---


개인 블로그를 관리하는데 사용할 수 있는 테마가 넘쳐난다면 당연히 고민이 될 것이다. 완전 까리한 테마를 골라 어렵게 설치하면 뭔가 해냈다는 느낌이 꽤나 좋다. 처음엔 minimal-mistakes로 입문하고 이후에 minima를 거쳐 just-the-docs라는 테마에 한동안 정착했는데, 어느순간부터 page build and deployment error가 뜨면서 블로그 관리가 안되는 문제가 발생하고 있다. 

> /usr/local/lib/ruby/2.7.0/rubygems/dependency.rb:311:in `to_specs': Could not find 'just-the-docs' (>= 0) among 157 total gem(s) (Gem::MissingSpecError)
> Checked in 'GEM_PATH=/github/home/.gem/ruby/2.7.0:/usr/local/lib/ruby/gems/2.7.0:/usr/local/bundle', execute `gem env` for more information

이런 에러 메시지인데 gem spec에 just-the-docs에 필요한 dependency를 명시해야 하는 것 같지만 당최 무슨 말인지 모르겠다. 이참에 원래 시도했던 simplex로 갈아탈까 고민 중인데 일단 just-the-docs 테마 에러 trouble shooting해보고 안되면 다른 테마로 갈아타자. 다음 테마는 무조건

- layout를 확장할 수 있어야함
- 한국어, latex, code 문법 깔끔한지

위주로 고르려고 한다. 그리고 한 1~2년 정도 깃헙 페이지 운영해보니 트래픽 거의 없는 것 같다. 면접관들만 볼텐데 타이틀도 그냥 `대충 아는 것은 내 자존심이 허락못해서 만든 페이지` 이런걸로 할거다. 이렇게라도 낙을 찾는 내 자신이 기특하다.


# New Theme

여기서부터 할 얘기가 많은데 github page를 시작한다면 가장 자주 접하면서 모르는 개념이 jekyll, gem 같은 것들이다. 

- jekyll


- gem


jekyll theme는 대부분 git repo에 원본 소스가 저장되어 있어서 해당 repo를 folk해서 그대로 가져와 사용해도 되고, 아니면 default jekyll theme에서 직접 gemfile 수정해서 원하는 테마를 다운로드 받는 방법도 있다. 

