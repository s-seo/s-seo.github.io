---
layout: default
title:  "OOP with Class (2)"
parent: Python
permalink: /Python/PythonOOP_2
# nav_order: 97
---


***

강의 목적: Python class에 대한 올바른 사용법과 객체 지향 프로그래밍(OOP) & typing 방법


***

# 객체지향 프로그래밍 이해

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
>출처: <https://nesoy.github.io/articles/2018-05/Object-Oriented-Programming>


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







***

# 파이썬에서 객체지향 프로그래밍하기

### - class 문법 정리 

* 파이썬 예시

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

