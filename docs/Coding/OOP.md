---
layout: default
title:  "객체 지향 프로그래밍 및 클래스 문법"
parent: Coding
nav_order: 97
---

최근 컴퓨터에 알 수 없는 에러가 뜨기도 하고 예전보다 확실히 느려진 것 같다고 느껴 1년만에 포맷했다. 그러면서 Python, VSC 등 여러 개발 환경 셋팅을 다시 하는 중인데 향후 개발 공부를 위해서라도 관련 프로세스를 정리하고자 한다.


> 상황: 처음 사용하는 컴퓨터에서 내가 개발 프로젝트 하나를 시작하려고 한다. 

코드 에디터에는 여러 종류가 있는데(VSC, PyCharm, Beam 등) 여기선 VSC를 사용한다.



## 설치 프로그램

1. [Python 3.7](https://nitr0.tistory.com/263)
2. [ANACONDA (3.7)](https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe)   
3. [Visual Studio Code](https://code.visualstudio.com/)



## 개발 환경 세팅 프로세스

1. `ctrl`+`shift`+`x`를 눌러 market place로 이동해서 아래 extensions을 설치함
   - python extension
   - 한국어 (선택)
   - material icon, material theme (디자인)
2. VSC에서 `ctrl`+`j`를 눌러 터미널 켜서 `$ python` 잘 실행되는지, `$ pip` 잘 설치되었는지 확인
   - 만약 터미널이 powershell이라면 가상환경 보는데 불편함이 있으므로 cmd로 바꿔주는게 좋다.  `ctrl`+`Shift`+`p`를 눌러 `select default profile`에서 `cmd`를 선택한다.
3. Linter와 Formatter를 설정한다. 각각 문법, 포맷을 알려주거나, 다듬어주는 툴이다. 
   - 먼저 `ctrl`+`,`를 눌러 Settings로 들어간 뒤, `format`으로 들어가 `Editor: Default Formatter`에서 `Python`을 설정한다. 또 `Editor: Format on Save`로 체크한다. 
   - Interpreter를 설정해야 하는데,   `ctrl`+`Shift`+`p`를 눌러 `Python: Select Interpreter`에서 적당한 것을 선택한다. 가상환경을 생성했었다면 그에 해당하는 interpreter가 있을텐데 그걸 선택하면 된다. Interpreter는 곧 파이썬이라고 생각했는데 이 부분은 좀 더 이해가 필요하다. 
   - Formatting은 VSCode에서 파일을 저장할 때 자동적으로 format 시켜주는 기능. 코드를 이쁘게, 보기좋게 알아서 다듬어 주는거라 생각하면 된다. `ctrl`+`,`로 Settings에 들어가서 `Python Formatting Provider`를 검색하고 `black`을 선택하면 된다.
   - Linter는 문법 체크, 즉 디버그하는 기능이다. 파이썬은 컴파일러가 아닌 인터프리터 언어이기 때문에 디버그가 어렵다. `ctrl`+`Shift`+`p`를 누르고 `select linter`를 검색한 뒤, `flake8`로 설정하면 된다. 설치가 필요하면 문구가 뜰텐데 클릭해서 설치하면 된다. 해당 폴더에 `.vscode` 폴더가 생성된 것을 확인할 수 있다.
4. 프로젝트 폴더 생성

```
$ cd 경로
$ mkdir 폴더명
$ cd 폴더명
```

5. 가상환경 생성
   1. venv, pipenv 등의 가상환경이 있지만 conda를 제일 많이 쓰고 이미 Anaconda가 설치되어 있기 때문에 conda를 사용하여 가상환경을 설정하겠다. 가상환경이란 한 컴퓨터에서 여러 프로젝트를 작업할 때 파이썬 패키지의 의존성이 충돌하지 않도록 관리하는 툴이다. 가상환경을 생성하면 환경변수 그룹이 만들어지고 그룹마다 지정된 경로에 패키지를 설치해서 참조한다. 패키지 버전 관리가 생각보다 까다로운데 가상환경으로 이를 효율적으로 관리할 수 있는 것.

      - Anaconda는 파이썬의 여러 배포판 중 한 종류이다. 데이터 사이언스를 위한 여러 패키지를 포함하고 있어 한번에 설치가 가능하다는 이점이 있다.
      - Jupyter Notebook은 오픈 소스 web API다. 이름에서 알 수 있듯이 일종의 문서인데, 코딩에 특화된 것이라 생각하면 편하다. 특히 실시간으로 데이터 조작, 시각화 및 공유가 편리하다는 특징이 있다.

   2. 아나콘다를 설치하면 "base"라는 가상환경이 자동적으로 생성된다. 여기는 일종의 허브로 두고 뭘 설치하거나 그러진 말자... 내가 그래서 여러모로 골치가 아팠다ㅠ

   3. 먼저 `$ conda update conda`를 실행해서 최신 버전의 conda로 업데이트해준다.

   4. `$ conda create --name 가상환경이름 python=파이썬버전` 명령어를 실행하여 가상환경을 생성한다. `$ conda env list`를 실행해 생성된 가상환경 목록을 확인할 수 있다.

   5. `$ conda activate 가상환경이름`를 실행해 생성한 가상환경으로 들어갈 수 있다. 그럼 (base)가 (가상환경이름)으로 바뀐다. 

   6. 해당 가상환경을 주피터 노트북과 연동할 수 있다. (사실 VSC에서 작업하기 때문에 이 과정이 반드시 필요한건 아니지만, 나중을 위해) 이를 위해 ipykernel이라는 라이브러리를 설치해야한다. 해당 가상환경 안에서 `$ conda install ipykernel`을 실행한다. `$ conda list`를 실행하면 해당 가상환경 안에서 설치된 라이브러리 목록을 확인할 수 있다.

   7. ipykernel을 설치했으면 이를 가상환경과 연동시켜야 한다. `python -m ipykernel install --user --name 가상환경이름 --display-name "[가상환경이름]"`을 실행한다. 이는 주피터 노트북에서 사용할 커널의 가상환경 이름을 `[가상환경이름]`으로 설정하는 것이다. 

   8. `$ conda deactivate`을 실행해 base로 돌아간 뒤 `$ jupyter notebook`을 입력해 주피터 노트북을 실행한다. `new`를 클릭해 가상환경이름이 부여된 커널을 통해 특정 작업을 수행할 수 있다. 
   
   * (0826) 막상 이렇게 작업을 해보려니까 에러가 좀 생겼는데, anaconda prompt에서 가상환경에 들어간 상태에서 주피터 노트북을 실행하느냐 vs base 환경에서 주피터 노트북을 실행하느냐 이 차이와, 기본 Python 3 커널을 쓸 것인지 vs 해당 가상환경 커널을 쓸 것인지에 따라 헷갈렸다. 결론적으론 해당 **가상환경에 들어간 상태**에서 아무 커널을 사용하면 패키지 설치, 사용에 문제 없는 것 같다. base 환경에서 주피터 노트북을 실행한 뒤, 아무 커널에 들어가서 패키지를 import하면 
   
   > Original error was: DLL load failed: 지정된 모듈을 찾을 수 없습니다.

   이런 에러가 뜨는데, 이는 아나콘다를 환경변수에 추가하지 않아서 발생하는 에러다. 근데 설치할 때 아나콘다를 환경변수에 추가한다고 설정했는데?라는 생각이 들면 <https://conda.io/activation>을 참고하자. 환경변수 개념은, 특히 윈도우에서, 아직 익숙하지 않아서 관련된 문제가 있다는 것만 알고 제대로 이해하지 못했다. 다만 가상환경에서 작업한다면 pandas, numpy와 같은 패키지를 다시 anaconda prompt에서 설치해야 하는 것 같다. 만약 base에서 쓰던 패키지를 그대로 쓰고 싶다면 그냥 requirements.txt로 빼내서 다운받는 방법이 있을텐데.. 뭔가 더 직관적인 방법이 있을테지만 일단 보류! 발생 가능한 상황과 그 결과에 대해 정리하면 다음과 같다,

   - base 환경 + python3 커널: 그냥 일반적인 사용환경. 내가 평소 작업하던 환경이니까 패키지도 그대로 있음.
   - baes 환경 + 가상환경 커널: 마찬가지로 평소 작업하는 패키지 그대로 있다.
   - 가상환경 + python3 커널: 내가 anaconda prompt에서 직접 설치한 패키지만 있다. 아나콘다에서 제공해주는 패키지들 설치 안되어 있음.
   - 가상환경 + 가상환경 커널: 위와 똑같다.

   * 여튼 이렇게 가상환경 상에서 작업하면 좋은 점은 내가 생각했을 때,

      - 가상환경이 설치된 dir를 default로 사용한다
      - 해당 가상환경에 설치된 라이브러리를 사용할 수 있다. 매번 다시 설치할 필요가 없는 것
      - 주피터 노트북에서 ipynb 파일이 아닌 프로젝트를 실행하는 개념이 되는 것 



   9. conda 명령어는 아래와 같다.

      - `$ conda --version`: 아나콘다 버전 확인
      - `$ conda info`: 설치된 아나콘다 정보 조회
      - `$ conda env list`: 가상환경 리스트 조회
      - `$ conda info --envs`: 현재 사용중인 가상환경 확인
      - `$ conda update -n base conda`: conda 업데이트
      - `$ conda create --name 가상환경이름 python=파이썬버전`: 특정 파이썬 버전의 가상환경 생성
      - `$ conda create -clone 원본_가상환경_이름 -n 새_가상환경이름`: 가상환경 복제
      - `$ conda activate 가상환경이름`: 가상환경 활성화
      - `$ conda deactivate`: 현재 사용중인 가상환경 비활성화
      - `$ conda env remove --name 가상환경이름`: 가상환경 삭제

   10. 가상환경에서 패키지 설치, 업데이트, 삭제. 
   
   * (0826) 이 때 한가지 유의할 점은 패키지 설치, 업데이트, 제거는 anaconda prompt에서 해야한다. 나는 뭣도 모르고 주피터 노트북에서 작업하다가 계속 설치가 안돼서 짜증났었다... 또 패키지 설치 등을 할 때 굳이 어떤 경로로 이동하지 않아도 된다. 그냥 기본 경로에서 작업해도 된다. 그 경로에 해당하는 폴더 안에 저장하는게 아니라 가상환경(?)에서 작업해서 그런가..?

   * (0826) pandas와 같이 `proceed? [y/n]`을 묻지 않는 경우라면 주피터 노트북에서 `!pip install 패키지`로 패키지 설치해도 문제 없는 것 같다.

       ```
       $ conda activate 가상환경
       $ conda install 패키지이름
       $ conda update 패키지이름
       $ conda remove 패키지이름
       ```

   11. 특정 가상환경에서 패키지 설치, 삭제

       ```
       conda install -n 가상환경이름 패키지이름
       conda remove -n 가상환경이름 패키지이름
       ```

   12. 주피터 노트북 명령어

       - 주피터 노트북 실행

         ```
         $ conda activate 가상환경이름
         $ conda install jupyter
         $ jupyter notebook
         ```

       - `$ jupyter kernelspec list`: 주피터의 kernel list 확인

       - 주피터 노트북에 커널 추가

         ```
         $ conda activate 가상환경이름
         $ conda install ipykernel
         $ python -m ipykernel install --user --name 가상환경이름 --display-name "[가상환경이름]"
         ```

       - `$ jupyter kernelspec uninstall 가상환경이름`: 주피터 노트북 커널 제거

6. 가상환경을 생성했으니 여기서 패키지를 설치하고 코드 작성하면 된다. 그럼 패키지를 설치하는 방법은? `pip`를 사용한다. `pip` 명령어는 아래와 같다. 가상환경 안에 들어가 있는 상태에서 하자! 안그러면 이 강의 듣는 이유가 없다...

   - `$ pip --version`: 설치된 pip 버전을 확인
   - `$ pip install pip --upgrade`: pip 업그레이드
   - `$ pip install "패키지~=3.0.0"`: 3.0.0 버전의 패키지 설치
   - `$ pip install 패키지`: 패키지 설치
   - `$ pip freeze`: 설치된 패키지 확인
   - `$ pip freeze > requirements.txt`: 설치된 패키지를 txt 파일로 출력. 추가로 txt 위에 주석으로 파이썬 버전을 명시해줘도 좋다.
   - `$ pip install -r requirements.txt`: requirements.txt에 입력된 패키지를 설치







여기서 부턴 post 나눠도 될 듯



강의 목적: Python class에 대한 올바른 사용법과 객체 지향 프로그래밍(OOP) & typing 방법



## 객체지향 프로그래밍 이해

[파이썬 공식문서](https://docs.python.org/3/) 참고

### - Decorator 패턴

함수에 첨가하는 것으로 이해하면 된다. 기존의 함수를 변형해서 새로운 함수를 만들어내는게 더 효율적인 경우가 있다. 공통적으로 변형시켜야 하는 함수가 너무 많을 때 이 방법을 주로 사용한다. 이 때 `@`를 변형하고자 하는 함수 위에 붙여줌으로써 decorator 패턴을 완성시킬 수 있다.

```python
def copyright(func):
    
    def new_func():
        print("@ ssm")
        func()
        
    return new_func

@copyright # 이게 없으면 smile = copyright(smile)로 재정의를 해줘야함. 이 구문과 같은 역할이라고 생각하면 됨
def smile():
    print("😊")

smile()
```

### - 객체지향 프로그래밍

![](https://s-seo.github.io/assets/images/post_oop_1.PNG) 
출처: <https://nesoy.github.io/articles/2018-05/Object-Oriented-Programming>


Data를 추상화시켜 상태(atrributes)와 행위(methods)를 가진 객체(object)로 만들고 그 객체들 간의 유기적인 상호작용을 통해 로직(흐름)을 구성하는 프로그래밍 방법이다. 즉 프로그램을 **실제 세상에 가깝게** 모델링하는 기법이라고 할 수 있다.

### - Class

어떤 문제를 해결하기 위한 데이터를 만들기 위해 OOP 원칙에 따라 집단(현실 세계)에 속하는 속성과 행위를 변수와 메서드로 정의한 것. *OOP 원칙에 따라 만든 설계도*다.

### - Instance (object)

class에서 정의한 것(설계도)을 토대로 실제 메모리 상에 할당된 것(실제 사물, object)으로 실제 프로그램에서 사용되는 데이터다. 하나의 class로 만들어진 여러 instance(object)는 각각 **독립적**이다. *설계도 결과물*이다.

### - OOP 원칙

- **캡슐화(encapsulation)**: 객체의 속성과 행위(methods)를 하나로 묶고, 구현된 일부를 외부에 감추어 은닉한다.
- **추상화(abstraction)**: 불필요한 정보는 숨기고 중요한 정보만을 표현함으로써 공통의 속성이나 행위를 하나로 묶어 이름을 붙이는 것
- **상속(Inheritance)**: 부모 class의 속성과 행위를 그대로 상속받고 행위의 일부분을 수정해야 할 경우 상속받은 자식 class에서 해당 행위만 다시 수정하여 사용가능해야 한다. 또한 자식 class에서 추가적으로 속성이나 행위를 정의할 수 있게 한다.
- **다형성(Polymorphism)**: 여러 형태를 가질 수 있도록 한다. 즉, 객체를 부품화할 수 있도록 한다.
  - A 공장에서 만든 타이어를 B 공장, C 회사에서도 사용할 수 있어야 하고 이 타이어는 탱크 타이터 개발의 재료로 사용될 수도 있다.

이러한 4가지 원칙을 지킨 프로그래밍을 OOP라고 하며 OOP를 지원하는 언어 중 하나가 파이썬이다. Java, C++, Lust, Go 등 수많은 언어에서도 지원함. 그만큼 중요하고, 효율성있고 생산성 높은 프로그래밍 기법이다.









## 파이썬에서 객체지향 프로그래밍하기

### - class 문법 정리 

```python
class Cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

cal1 = Cal(1, 2) # 클래스의 인스턴스(결과물)
print(cal1.a)
print(cal1.b)
print(cal1.add())

cal1.a = 7
print(cal1.add()) # 외부에서 namespace를 수정할 수 있음
```

* `__init__`

`Cal`이라는 클래스를 정의했고, `Cal()`을 호출하여 인스턴스를 생성한다. 이 때 `Cal()`을 생성자하고 한다. 좀 더 구체적으로, 생성자를 호출하면 `Cal.__new__()`라는 매직 메서드가 호출되어 인스턴스가 할당되고, 그 다음에 `Cal.__init()` 메서드가 인스턴스를 초기화한다. `__init__` 메서드는 생성자 함수라고 하며, 인스턴스가 만들어질 때(할당될 때) 인스턴스를 초기화하는 역할을 한다. 매직 메서드 중 하나이며, 다른 이름으로 바뀔 수 없다.

* attribute

인스턴스는 데이터와 메서드로 구성되는데 이를 묶어 attribute라고 한다. 이 중 메서드는 함수인데 메서드의 첫번째 파라미터는 호출된 인스턴스 자신(self)다. 



### - 추상화

추상화는 불필요한 정보는 숨기고 중요한 정보만을 표현함으로써 공통의 속성, 값, 행위를 하나로 묶어 이름을 붙이는 것이다. 즉, 공통된 것들을 하나로 묶어 일반화하는 사고 과정이다. 실무에서 사용 방식을 논하자면, 공통된 현실 문제에 있어서 일반적인 솔루션을 만들어 새로운 현실 문제에 대응, 해결하는 것이다. 따라서 재사용성, 유지보수성을 높이는 방법이다.

```python
class Robot: # 클래스 명
    
    # 클래스 네임스페이스 안에 존재하는 변수가 있고, 이 변수는 인스턴스가 공유하는 변수다. 가장 상위에 있음
    # 이 클래스로 각 데이터를 찍어낸다 (인스턴스). 인스턴스 안에 인스턴스 변수, 메서드가 있다.
    # 클래스에서도 클래스 변수, 클래스 메서드가 있음. 여기서 데코레이터를 사용
    
    # 클래스 변수: 인스턴스들이 공유하는 변수
    population = 0
    
    # 생성자 함수. 인스턴스를 초기화시키는 함수
    def __init__(self, name, code): # self는 각각의 인스턴스를 뜻함
    	self.name = name # 인스턴스 변수
        self.code = code # 인스턴스 변수
        Robot.popultaion += 1
    
    # 인스턴스 메서드
    def say_hi(self):
        # code
        print(f"Greetings, my masters call me {self.name}.")
    
    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b
    
    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
           else:
            print(f"There are still {Robot.population} robots working.")
        
    # 클래스 메서드
    @classmethod # 이미 만들어짐. 파이썬 개발자가 만듦
    def how_many(cls): # cls는 self와 비슷하지만 다름. cls를 받는다.
        print(f"we have {cls.population} robots.")
        

siri = Robot('siri', 21039788127)
jarvis = Robot('jarvis', 2311213123)
bixby = Robot('bixby', 1234123423)

print(siri.name)
print(siri.code)
siri.say_hi()
siri.cal_add(1, 2)
siri.die()

print(Robot.population) # 3
Robot.how_many() # 3
```

* 불필요한 정보를 숨긴다는 것은, `.say_hi()`와 같은 코드가 어떻게 동작되는지를 따로 출력하지 않는다는 것이다.
* Namespace라는 개념을 잘 이해해야 하는데, 내가 이해한 것은 변수화 할 수 있는 공간이다. 인스턴스인 self에는 변수, 메서드를 할당할 수 있는 namespace가 있다. 똑같이 클래스에도 변수, 메서드를 할당할 수 있는 namespace가 있다. 
* 위 클래스를 통해 우리는 `Robot`이라는 클래스를 구현해서 **일반화(추상화) 작업**을 한 것이고, 그 결과로 시리, 자비스, 빅스비와 같은 인스턴스를 구현했다. 여기에 추가적인 로봇인 '드로이드'를 만들고 싶다면 만들어진 `Robot` 클래스를 통해 인스턴스로 찍어내기만 하면 된다. 이러한 추상화 과정이 없다면 매번 로봇을 만들때 마다 모든 과정을 처음부터 시작해야 한다. 

* 인공지능 알고리즘을 개발하는 엔지니어의 경우, 여러 모델의 성능을 비교하는 프로그램을 짠다고 해보자. 동일한 데이터 셋과 환경에서 여러 모델의 성능을 비교해야 하므로 각 모델에 대해 "데이터 셋 로드", "데이터 전처리", "손실함수 적용" 등 동일한 환경에서 동일한 기능이 수행된다. 따라서 공통된 기능을 하는 `Machine`이라는 클래스를 만들고, 이 클래스를 상속받아 각 모델의 비교 대조할 기능을 재정의하면 재사용되는 공통된 로직 위에서 모델을 비교 대조할 기능에 따라 평가할 수 있다.
* 여러 클래스를 추상화하여 하나의 추상 클래스를 설계할 때 추상화 사고가 사용되기도 한다.



### - Namespace

사전적으로는 개체를 구분할 수 있는 범위라고 정의한다. 이를 확인할 수 있는 함수는 `.__dict__`로 매직 메서드다. 공식문서에서 확인할 수 있음. Namespace를 딕셔너리 형태로 반환하는 함수다.

```python
# import Robot

print(Robot.__dict__)
print(siri.__dict__)
print(jarvis.__dict__)
```

Q: 인스턴스 멘서드가 왜 클래스 메서드에 포함되어 있는지? 

A: 파이썬의 메모리 효율을 위해 거기에 저장하고, 거기에 저장하면 인스턴스 입장에서 접속시킬 수 있다. 이 원리로 인해 클래스 변수, 클래스 메서드에 인스턴스로 접속할 수 있게끔 할 수 있는 것.

좀 더 구체적으로, 파이썬 내부적으로 연산을 도와주기 위한 형태. 클래스 메서드를 인스턴스에도 적용 가능하다. `siri.how_many() `이런 식으로. `Robot.say_hi()`를 실행하면 에러가 남. self에 인자가 안 들어갔기 때문에. 논리적으로 말이 되려면 `Robot.say_hi(siri)`를 실행하면 된다. 

* `dir()`: 접근이 가능한 메서드 리스트를 모두 나타내줌. 인스턴스, 클래스 모두에 적용 가능. 
* `__doc__`: 협업할 때 클래스에 대한 정보를 주석으로 처리하는 경우 많다.  이 주석처리 된 것만 반환하는 메서드.  `Robot.__doc__`으로 확인가능

```python
class Robot:
    """
    [Robot Class]
    Author : 서승민
    Role : ???
    """
```

* `__class__`: 인스턴스가 어떤 클래스로 만들어졌는지 반환하는 메서드

Namespace는 완벽히 이해하기 어렵다... 파이썬이 물리적으로 데이터를 어떻게 저장하고, 접근하는지 다루는 개념이라 생각하고 넘어가도 무방함.



### - Staticmethod

클래스 설계도에서 `cls`, `self`와 같은걸 사용하지 않을 수 있다면? 아래와 같은 코드가 있다면

```python
class Robot:
    # ...
    
    @staticmethod # 이게 있어야 인스턴스에도 적용가능함
    def this_is_robot_class():
        print("yes!!")

print(droid1.this_is_robot_class())
print(Robot.this_is_robot_class())
```

이처럼 굳이 인스턴스를 정의할 필요가 없는 메서드를 staticmethod라고 한다. 함수 위에 데코레이터 패턴 `@staticsmethod`를 삽입하면 인스턴스에도 적용할 수 있으며, 없다면 클래스에만 적용할 수 있다.



### - Self, Cls 이해

`self`는 인스턴스 객체다. 클래스 안에 있는 self의 주소와 인스턴스의 주소는 같기 때문에 self는 인스턴스 그 자체이다.

```python
class SelfTest:
    
    # 클래스 변수
    name = 'ssm'
    
    def __init__(self, x):
        self.x = x # 인스턴스 변수
    
    # 클래스 메서드
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")
        
    # 인스턴스 메서드
    def func2(self):
        print(f"self : {self}")
        print("class안의 self 주소 : ", id(self))
        print("func2")
        
test_obj = SelfTest(17)
test_obj.func2()
Self.Test.func1()
print('인스턴스의 주소:', id(test_obj))
```

결과를 통해 self의 주소와 인스턴스의 주소는 같다는 것을 확인할 수 있다.  또한 cls는 해당하는 클래스 자체를 가리킨다. `func1()`의 결과로 class만 나왔기 때문.  `func2()`의 결과는 class object라고 된다. 

* `test_obj.func1()`을 실행하면 어떻게 될까? 인스턴스에 클래스 메서드를 적용한거니까 뭔가 에러가 뜰 것 같지만 `SelfTest`라는 제대로 된 결과가 나온다. 이는 **파이썬이 동적이라는 특징**에 기인한 것인데 인스턴스를 통해서 `func1`을 실행해도 class namespace를 찾아가서 실행하는 것이다. 
* `print(test_obj.name)`는 어떻게 될까? 같은 원리로 클래스 변수를 찾아가서 결과를 반환한다.
* `SelfTest.func2()`는 어떨까? 에러가 나는데, 인스턴스로는 `test_obj.__class__`를 통해 해당 클래스로 접근할 수 있지만, 클래스는 해당하는 인스턴스를 확인할 수 없다. 즉 올라가는 것 돼도 아래로 탐색하는 것은 안되는 것.
* `print(SelfTest.x)`는? 이것도 같은 논리로 안됨.





### - 매직 메서드

```python
class Robot:
    # ...

    
droid1 = Robot("R2-D2")
print(dir(droid1))
```

`__xxx__`는 매직 메서드로 파이썬 내장 함수인데, 모두 각각의 역할이 있다. 

* `__str__`: 먼저 `print()` 함수는 객체를 어떻게든 사용자에게 보여주려고 객체를 문자열로 나타내는 것. `print(droid1)`와 `print(droid1.__str__())`은 같은 결과를 낸다. 이걸 커스텀 할 수 있는데, 아래와 같은 작업을 overwriting이라고 함. 상속에서 나오는 개념. 원래 있는 매직 메서드에 덮어씌웠다 생각하면 된다. 

```python
class Robot:
    def __str__(self):
        return f"{self.name} robot!!"
```

* `__call__`: **파이썬에서 모든 것은 객체**인데, 그러면 함수도 누군가로 만들어진 객체라는 것.  왜 괄호 두 개가 붙을까? 이 괄호가 실행을 의미하고, callable을 의미한다. 그냥 `droid1`을 실행하면 TypeError가 뜬다. 아래와 같이 커스텀하면, `droid1()`을 실행했을 때 에러가 안 뜬다. 객체가 함수처럼 된 것. 해당 객체에 매직 메서드가 정의되어 있기 때문에 함수로 호출되는 것이다. 즉, 함수도 어떤 클래스에 의해 만들어진 것인데, 그 클래스에는 이 `__call__`이라는 속성값이 반드시 있어 함수가 이렇게 호출된 것이다. 

```python
class Robot:
    def __call_(self):
        print("call!")
        return f"{self.name} call!!"
```



### - 상속(Inheritance)

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

```python
class Robot:
    # ...

class Siri(Robot): # 이렇게 클래스의 인자(?)로 들어가면 상속한다는 의미
    pass # 그냥 넘어가는 빈 한 줄. 아무것도 적지 않을 것임을 의미함

siri = Siri()
print(siri) # TypeError가 뜸. name이란 argument가 필요함. Robot의 생성자 함수가 name을 필요로하기 때문

siri = Siri("iphone8")
print(siri) # __str__이 실행됨
print(siri.are_you_robot())
print(siri.cal_add(18, 19))
```

2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.

```python
class Robot:
    # ...

class Siri(Robot):
    
    def __init__(): # 그대로 쓰면 오버라이팅 되어 효율성이 떨어짐.
    
    def call_me(self):
        print("네?")
        
    def cal_mul(self, a, b,):
        self.a = a
        return a * b
    
    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple!!") # 여기선 cls가 Siri를 가리킴
     
siri = Siri("iphone8")
siri.call_me()
print(siri.cal_mul(3, 5))
print(siri.a)
Siri.hello_apple()
```

3. 메서드 오버라이딩(overriding)

```python
class Robot:
    #...

class Siri(Robot):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        Siri.population += 1
    
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}. by applye.")
    
    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots. by apple"
    
siri = Siri("iphone8", 17)
siri.say_hi()
print(Siri.how_many())
```

같은 메서드를 상속받은 클래스에서 정의하면 덮어씌워 진다. 클래스메서드도 마찬가지다. 매직메서드도 다르지 않다. `super()`라는 메서드를 사용해서 초기화 가능함. 



4. super()

```python
class Siri(Robot):
    def __init(self, name, age):
        self.age = age
        super().__init__(name)
        
    def cal_flexible(self, a, b):
        super.say_hi()
        self.say_hi()
        return self.car_mul(a, b) + self.car_add(a, b) + super().cal_add(a, b)
        
print(siri.age)
print(siri.name)

siri.car_flexible(1, 3)
```

`super().__init__(name)`이 실행되면서 부모클래스 name이 넘어와지기 때문이다.  오버라이딩 한 메서드도 `super()`로 실행될까?  오버라이딩 하기 전 메서드가 실행된다. `self.say_hi()`는 오버라이딩 한 후 메서드가 실행된다. 



5. Python의 모든 클래스는 object 클래스를 상속한다: 모든 것은 객체이다.

이 문장 자체가 객체지향 프로그래밍이 무엇인지 알려주는 것이다. 파이썬이 그만큼 인간의 사고 과정을 흡수할 수 있을만큼 똑똑한 언어임을 의미한다. 

```python
class Siri(Robot):
    # ...

siri = Siri("iphone8")
print(Siri.mro()) # mro는 상속 관계를 보여주는 메서드
# __main__.Siri, __main.Robot 다음에 object 라는 클래스가 나옴
print(Robot.mro()) # object 여전히 나옴
# 즉, `class Robot(object):`가 본모습인 것. 
print(dir(object))
print(object.__name__)
print(int.mro())
print(int.__init__(8, 9))
print(int(8, 9))
```

```python
# 다중상속

class A:
    pass

class B:
    pass

class C:
    pass

class D(A, B, C):
    pass
# 다중상속은 안티-패턴을 유발함. 오버라이딩 된 메서드가 있다면 메모리 공유라는 복잡한 이슈가 발생함. 
```



### - 캡슐화(encapsulation) - private vs public

```python
class Robot:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    
ss = Robot('yss', 9)
print(ss.age)

ss.age = -999
print(ss.age) # age가 minus인게 말이 안됨. 네임스페이스가 보호받지 못한셈. 이런 경우를 막는 방법은 private이라고 함. 외부에서 접근을 금지하는 것을 의미함
ss.__age # 없다고 뜸. 

class Siri(Robot):
    def __init(self, name, age):
        super().__init(name, age) # Robot 클래스의 생성자가 실행된 셈
        print(self.name) # 초기화했으니 당연히 나옴
        self.__age = 999
        print(self.__age)
        
        
sss = Siri("ip8", 9)
sss.age
```

* `__age` 이런식으로 변수 앞에 작대기 두 개를 붙이면 private을 부여하는 것.  Underbar가 양쪽에 두 개 있으면 public으로 취급함. 한 쪽에만 있어야 private으로 은닉시켜줌. 파이썬에선 이런 식으로 코딩하지는 않는다. 동적인 것을 추구하기 때문에 암묵적으로 `_age`라고 하면 '여기 접근하지마라' 이렇게 나타내는 것. 실행은 되지만 눈치없는거지..
* 상속받는 경우,  `super()`를 실행하면 private한 것은 없어진다. 다시 정의를 해줘야 함.
* 파이썬 개발자 커뮤니티에선 underbar 한 개를 protect로 받아들이자는 논의가 있음.  효과는 없지만 그냥 암묵적인 약속



### - 캡슐화, @property, getter, setter

```python
class Robot:
    
    @property
    def agesss(self):
        return self.__age
    
    @age.setter # 해당하는 property 이름
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("Invalid age range")
        else:
            self.__age = new_age
    
droid = RObot("T2", 2)
print(droid.age)
droid.age = 77
print(droid.age)
```

* `__`로 은닉시켰는데 출력된다. `getter`라는 attribute로 age를 출력할 수는 있지만, 이를 바꾸는 setter가 없기 때문에. 변수를 메서드로 넣되 위에 `@age.setter`를 삽입해서.. 이렇게 할거면 굳이 왜 은닉하냐? 뭔가 조건을 걸어서 범위를 설정하려고..? 이렇게 네임스페이스를 보호하는건가...

* `@property()`는 속성에 접근할 수 있게 해줌
* `setter`는 파이썬은 **견고**하게 사용하기 위해 중요한 역할을 함. 견고하다는건 robust하다는 의미인듯..? 그대로 해석했나



### - 다형성(polymorphism)

같은 형태의 코드가 다른 동작을 하도록 하는 것. 객체를 부품화할 수 있다는 것

```python
class Robot:
    # ...
    
class Siri(Robot):
    def say_apple(self):
        print("hello my apple")
        
class SiriKo(Robot):
    def say_apple(self):
        print("안녕하세요")
        
class Bixby(Robot):
    def say_samsung(self):
        print("안녕하세요")

```

디자인 패턴에 가깝다. 메서드도 동일함. 같은 형태의 코드가 서로 다른 의미를 갖도록 하는 것. 한 부품을 다양하게 사용할 수 있다. 다형성을 지키는 코드는 재사용성, 유지보수성에서 효율적임.



### - 컴포지션(composition)

다른 클래스의 일부 메서드를 사용하고 싶지만 상속하고 싶지 않을 경우 사용함. 상속했을 때 문제점은,

1. 부모 클래스가 변하면 자식 클래스는 수정되어야 함. 오버라이딩 해야하는 것
2. 부모 클래스의 메서드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 높다

```python
class Bixby(Robot):
    
class BixbyCal: # 상속 없음
    def __init__(self, name, age):
        self.Robot = Robot(name, age)
        
    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)
    
```

유지보수와 견고한 소프트웨어를 만들기 위해 컴포지션을 사용함. 독립적인 함수는 아니고 일종의 기법이자 패턴에 해당함.

#### - 효율적 메모리 관리

* 객체(네임스페이스) 내에 있는 변수는 `__dict__`를 통해서 관리할 수 있음

```python
class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

wos = WithoutSlotClass("ssm", 12)
print(wos.__dict__)

wos.('hello') = 'world' # 추가안됨
wos.__dict__('hello') = 'world' # 추가됨
print(wos.__dict__)
```

* `__slots__`을 통해 변수 관리할 수 있되, 필요한 객체에 대해서만 적용함으로써 메모리 효율 높이는 것

```python
class WithSlotClass:
    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

ws = WithSlotClass('ssm', 17)
print(ws.__dict__) # 에러뜸. name 과 age 속성만 사용하도록 slots을 통해 제한시켰기 때문.
print(ws.__slots__)
```











## 파이썬에서 타이핑하기

## 배운 것을 응용하기



