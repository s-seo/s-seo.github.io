---
layout: default
title:  "Data Structure & Algorithm"
parent: Python
permalink: /Python/PythonAlgorithm
# nav_order: 97
---

***
*자료구조와 알고리즘을 <https://programmers.co.kr/learn/courses/57>에서 수강 중이다. 본 포스팅은 이 강의에서 배운 것을 정리한 것이다.*

Data structure는 왜 필요할까? 효율성 때문이다. 예를 들어 `max`라는 함수는 리스트의 모든 원소를 탐색해서 최댓값을 도출하기 때문에 리스트 크기가 크면 그만큼 시간도 오래 걸린다. 만약 자료 구조를 알면 이 시간을 단축시킬 수 있다. 세상엔 똑똑한 사람들이 많아 이미 이러한 자료 구조를 많이 개발해놨다. 따라서 우리는 어떤 문제를 어떤 자료 구조로 풀지 판단하는 능력만 갖추면 효율적으로 문제를 해결할 수 있다. 알고리즘은 주어진 문제를 해결하기 위한 자료 구조, 연상 방법의 집합이라고 할 수 있다. 

***
# 선형 배열 (Linear Array)

프로그래밍에서는

* Array: 같은 종류의 데이터가 줄지어 늘어서 있는 것
* Linear array: 같은 종류의 데이터가 선처럼 일렬로 늘어서 있는 것

이라는 개념이 있는데 Python의 List는 이 중 Linear array에 대응되는 개념이다. 특히 리스트는 다른 종류의 데이터를 같이 배열할 수 있다는 점에서 융통성이 높다. 리스트에 적용될 수 있는 연산 중

* `.append()`, `.pop()`: 리스트의 모든 원소를 일일히 탐색하지 않아 상수 시간(O(1))에 연산이 가능하다.
* `.insert()`, `.del()`: 리스트의 모든 원소를 일일히 탐색해서 O(n)만큼의 시간이 소요된다.
* `.index()`: 원소의 인덱스를 반환하는 연산
* `sorted()`: 파이썬 내장함수로 정렬된 리스트를 반환한다.
* `.sort()`: 메서드로 해당 리스트를 정렬한다 

문자열 정렬의 경우 알파벳, 대문자 순서로 정렬한다. 문자열 길이로 정렬하고 싶다면 아래와 같이 `key`를 설정하면 된다.

```python
sorted(L, key=lambda x:len(x))
```

***

# 탐색 알고리즘

* 선형 탐색은 순차적으로 일일히 탐색하기 때문에 O(n)만큼 시간이 소요된다. 
* 이진 탐색 (binary search)는 비교가 포함되어 시간이 반씩 줄어들기 때문에 O(log n)만큼 시간이 소요된다. 하지만 리스트가 정렬되어 있어야만 가능하기 때문에 정렬이 필요한 경우 항상 효율적이라고 할 수는 없다.
* `if x in L`: 선형 탐색인 것 명심

***

# 재귀 알고리즘 (recursive algorithm)

* 재귀 함수: 하나의 함수에서 자신을 다시 호출해서 작업을 수행하는 함수
* 이진 트리, 자연수의 합을 구하는 등 매우 다양한 문제에서 재귀 알고리즘을 적용할 수 있다. 아래는 자연수의 합을 구하는 코드 예시다.

```python
def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)
```

* n이 쓰이는 모든 문제에 적용가능할 것 같다. 다만 종결 조건, trivial case를 잘 설정해주는 것이 매우 중요함. 쉽게 말하면 n=1인 경우, 즉 초기값을 설정하는 것
* 재귀 함수의 효율을 그닥 좋지 않다. O(n)이지만 함수를 호출하는데서 오는 복잡도가 무시못하기 때문에 효율이 떨어진다. Iterative한 방법이 보통은 효율이 더 좋지만 그럼에도 재귀 알고리즘을 사용하는 이유는, 알고리즘을 간단하고 이해하기 쉽게, 인간이 사고하는 방식에 유사하게 서술할 수 있다는 장점이 있기 때문이다. 
* 이진 탐색을 재귀적으로 구현하면 함수 인자에 lower, upper를 추가하면 된다.


***

# 연결 리스트 (Linked Lists)

* 추상적 자료구조란? (Abstract Data Structures) 

데이터와 일련의 연산 집합을 추상적으로 나타낸 자료 구조를 의미한다. 이 중 하나가 연결 리스트다. 본 강의에선 연결 리스트의 추상적 자료구조를 파이썬의 클래스를 기반으로 이를 구현한다. 

* 기본적인 연결 리스트 (단방향 연결 리스트, singly linked list)

**1. Node가 기본 단위이며 각 노드 내에는 Data와 Link(next)가 있다. Data는 다른 구조가 할당될 수 있다.**

**2. 연결 리스트의 맨 앞을 Head로, 맨 끝 노드를 Tail이라고 하는데 이 두가지를 알아야 한다. Head를 알아야 시작할 수 있고 Tail을 알면 끝에 뭘 붙일 때 좋고, number of nodes도 알면 좋다.**

**3. 연결 리스트의 추상적 자료구조를 만들기 위해선 두 개의 class를 사용한다. 먼저 Node class를 만든다.**

```python
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
```

그 다음은 LinkedList라는 class의 자료구조를 만든다. 

```python
class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
```

비어있는 연결 리스트를 정의하고, 이를 채워나가는 방식으로 연결 리스트의 추상적 자료구조를 구현할 수 있다.

**4. 연결리스트의 연산에는 특정 원소 참조(k번째), 리스트 순회, 길이 얻기, 원소 삽입, 원소 삭제, 두 리스트 합치기가 있다.**

* k번째 원소의 인덱스를 찾는 코드. 이걸로 리스트 순회를 하려면 비효율적. 매 리스트를 append 할 때마다 Head부터 링크를 따라 탐색하기 때문

```python
def getAt(self, pos):
    if pos <= 0 or pos > self.nodeCount:
        return None
    i = 1
    curr = self.head # 연결리스트의 첫번째 노드 할당
    while i < pos: 
        curr = curr.next
        i += 1
    return curr
```

**5. 배열과의 비교**
- 배열: 연속한 위치에 데이터가 지정되어야함. 몇번째라고 했을 때 단번에 그 인덱스를 찾을 수 있음. **번호가 붙여진 칸에 원소들을 채워넣는 방식**
- 연결 리스트: 각 노드가 링크로 연결되어 있어 임의의 위치에 할당될 수 있다. **각 원소들을 줄줄이 엮어서 관리하는 방식**. 그러나 특정 원소를 탐색하려면 링크를 하나하나 짚어가면 찾기 때문에 선형 탐색과 유사한 시간이 소요된다. 그럼 왜 연결 리스트를 사용할까? 
- 장점: 원소들이 링크라는 고리로 연결되어 있으므로, 가운데에서 하나를 끊어 삭제(선형 배열에서는 del()이라는 O(n))한다거나, 삽입(insert(), O(n))하는 것이 선형 배열보다 효율적이다. 
- 단점: 데이터 구조 표현에 필요한 저장 공간(메모리)가 크다. 또한 k번째 원소를 찾는 문제는 선형 배열보다 비효율적이다. 특정 원소를 접근하려면 첫 노드부터 하나씩 링크를 따라가면 찾아가야한다.



**6. Node의 삽입, 삭제**

* 삽입
pos로 위치를 정하면, pos-1에 위치한 노드를 prev라고 하고, prev.next가 가리키는 노드를 newNode의 next link가 가리키도록 하고, prev.next가 newNode를 가리키도록 설정해야함. 마지막으로 nodeCount를 1 증가시킨다. 중요한건 맨 처음, 끝에 삽입하거나 빈 리스트인 경우.

```python
def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
        return False

    if pos == 1:
        newNode.next = self.head
        self.head = newNode
    else:
        if pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos -1)
        newNode.next = prev.next
        prev.next = newNode
    
    if pos == self.nodeCount + 1:
        self.tail = newNode

    self.nodeCount += 1
    return True
```

복잡도를 논하자면, 맨 앞, 뒤에 삽입하는 경우는 O(1), 중간에 삽입한다면 O(n)이다. 

* 삭제 및 반환
pos-1번째 노드를 prev, pos번째 노드를 curr라고 할 때, prev.next가 curr.next를 가리키게 하면된다. 마지막으론 nodeCount를 1 빼주면 된다. 삭제하려는 노드가 맨 앞, 뒤인 경우 또는 빈 리스트인 경우 주의할 것.

```python
def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError
    curr = None 
    if pos == 1:
        curr = self.head
        if self.nodeCount == 1:
            self.head = None
            self.tail = None
        else:
            self.head = curr.next
    else:
        prev = self.getAt(pos-1)
        curr = prev.next
        if pos == self.nodeCount:
            prev.next = None
            self.tail = prev 
        else:
            prev.next = curr.next
    self.nodeCount -= 1
    return curr.data
```

복잡도는 맨 앞에서 삭제하면 O(1), 중간, 맨 끝에서 삭제하면 O(n)이다.


**7. 두 리스트의 연결**

```python
def concat(self, L):
    self.tail.next = L.head
    if L.tail:
        self.tail = L.tail
    self.nodeCount += L.nodeCount
```

만약 array를 이용했다면 훨씬 어려웠을 것. 



**8. 새로운 메서드 (insertAfter, popAfter)**

`.getAt()` 메서드는 매번 처음부터 링크를 타고 인덱스를 찾는다는 점에서 비효율적이다. 이 점을 보완하면 연결 리스트가 더 좋을텐데 방법이 없을까? 해서 나온게 위의 메서드다.

- insertAfter: 맨 앞에 dummy node를 추가한 형태

```python
class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail
```

구조가 살짝 달라졌으니 연산도 달라져야함. 

- 리스트 순회(이건 목적이 아니니까)
```python
def traverse(self):
    result = []
    curr = self.head
    while curr.next:
        curr = curr.next
        result.append(curr.data)
    return result
```

- k번째 원소 얻기(0부터 시작하니까 `pos-1`인 경우에도 먹혀서 일반화 가능)
```python
def getAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        return None
    i = 0
    curr = self.head
    while i < pos:
        curr = curr.next
        i += 1
    return curr
```

- 원소의 삽입
```python
def insertAfter(self, prev, newNode):
    newNode.next = prev.next
    if prev.next is None:
        self.tail = newNode
    prev.next = newNode
    self.nodeCount += 1

    return True
```

더미 노드 추가함으로써 위와 같이 간단하게 삽입 코드를 짤 수 있다!! 신기해

- `insertAt()`의 구현
```python
def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
        return False
    
    if pos != 1 and pos == self.nodeCount + 1:
        prev = self.tail
    else:
        prev = self.getAt(pos - 1)
    return self.insertAfter(prev, newNode)
```

- 원소의 삭제
```python
def popAfter(self, prev):
    curr = prev.next
    if curr.next is None:
        self.tail = prev
    prev.next = curr.next
    self.nodeCount -= 1

    return curr.data
```

```python
def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError
    prev = self.getAt(pos - 1)
    
    return self.popAfter(prev)
```


- 두 리스트 연산
```python
def concat(self, L):
    self.tail.next = L.head.next
    if L.tail:
        self.tail = L.tail
    self.nodeCount += L.nodeCount
```

지금까지 앞으로 전진하는 연결 리스트 (singly linked list)만 살펴본 것. 이제 양방향 연결 리스트를 살펴보자.

**9. 양방향 연결리스트**

양쪽으로 링크를 연결해서 앞으로도, 뒤로도 진행 가능한 연결 리스트다. 구현하기 위해선 Node의 구조를 확장해야함.

```python
class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None
```

또한 리스트 처음과 끝에 dummy node를 둠으로써 이전에 얻은 효율성을 그대로 부여하자. 이렇게하면 데이터를 담은 node는 모두 같은 모양이 된다. 

```python
class DoublyLinkedList:
    def __init__(self,item):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
```

- 리스트 순회
```python
def traverse(self):
    result = []
    curr = self.head
    while curr.next.next: # 여기가 다름. 
        curr = curr.next
        result.append(curr.data)
    return result
```

- 리스트 역순회
```python
def reverse(self):
    result = []
    curr = self.tail
    while curr.prev.prev: # 여기가 다름. 
        curr = curr.prev
        result.append(curr.data)
    return result
```

- 원소의 삽입
```python
def insertAfter(self, prev, newNode):
    # 4개 링크 조정 및 nodeCount 1 더하기
    next = prev.next
    newNode.prev = prev
    newNode.next = next
    prev.next = newNode
    next.prev = newNode
    self.nodeCount += 1
    return True
```

- 특정 원소 얻어내기
```python
def getAt(self, pos):
    if pos < 0 or pos > self.nodeCount:
        return None
    
    if pos > self.nodeCount // 2:
        i = 0
        curr = self.tail
        while i < self.nodeCount - pos + 1:
            curr = curr.prev
            i += 1
    else:
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
    return curr
```

- 원소의 삽입
```python
def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
        return False
    prev = self.getAt(pos - 1)
    return self.insertAfter(prev, newNode)
```

- 연습문제
```python
def insertBefore(self, next, newNode):
    prev = next.prev
    newNode.prev = prev
    newNode.next = next
    prev.next = newNode
    next.prev = newNode
    self.nodeCount += 1
    return True
```
```python
def popAfter(self, prev):
    curr = prev.next
    next = curr.next
    prev.next = next
    next.prev = prev
    self.nodeCount -= 1

    return curr.data
```
```python
def popBefore(self, next):
    curr = next.prev
    prev = curr.prev
    next.prev = prev
    prev.next = next
    self.nodeCount -= 1

    return curr.data
```
```python
def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError
    prev = self.getAt(pos - 1)
    
    return self.popAfter(prev)
```
```python
def concat(self, L):
    L1_tail = self.tail.prev
    L2_head = L.head.next
    L1_tail.next = L2_head
    L2_head.prev = L1_tail
    self.tail = L.tail
    self.nodeCount += L.nodeCount
```

양쪽 방향 구조라 링크가 차지하는 메모리는 많아지지만 코드는 훨씬 간단해짐. Head나 Tail을 조정할 필요가 없고, `.getAt()` 메서드를 조정함으로써 맨 마지막 원소를 뽑아내는게 자동적으로 시간이 덜 걸린다.

***

# 스택

앞으로 배울 자료구조는 알고리즘 해결에 특화된 것들. 스택이란 자료를 보관할 수 있는 선형 구조인데, 넣을 때에는 한 쪽 끝에서 밀어 넣고(푸시 연산), 꺼낼 때에는 같은 쪽에서 뽑아 꺼내야 하는(팝 연산) 제약이 있다. 따라서 후입선출 (Last In First Out) 특징을 갖는 선형 구조다.

```python
S = Stack()
S.push(A)
S.push(B)
r1 = S.pop() # B
r2 = S.pop() # A
```

여기에 쓰인 함수와 메서드를 정의해야함. `r3 = S.pop()`와 같이 비어있는 스택에서 데이터 원소를 꺼내려 할 때는 stack underflow라는 에러 발생. 또는 꽉 찬 스택에 데이터 원소를 넣으려 할 때는 stack overflow라는 에러 발생.

**0. 스택 연산의 정의**
* `.size()`: 현재 스택에 들어있는 데이터 원소의 수를 구함
* `.isEmpty()`: 현재 스택이 비어 있는지를 판단
* `.push(x)`: 데이터 원소 x를 스택에 추가
* `.pop()`: 스택 맨 위 저장된 데이터 원소를 제거하고 반환
* `.peek()`: 스택 맨 위 저장된 데이터 원소를 제거하지 않고 반환


**1. 스택의 추상적 자료 구조 구현 (배열)**
```python
class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]
```


**2. 스택의 추상적 자료 구조 구현 (양방향 연결 리스트)**
```python
from doublylinkedlist import Node
from doublelinkedlist import DoublyLinkedList # 위에서 정의한 양방향 연결 리스트

class LinkedListStack:
    def __init__(self):
        self.data = DoublyLinkedList()
    
    def size(self):
        return self.data.getLength()
    
    def isEmpty(self):
        return self.size() == 0
    
    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)
    
    def pop(self):
        return self.data.popAt(self.size())
    
    def peek(self):
        return self.data.getAt(self.size()).data

```

또는 `from pythonds.basic.stack import Stack`으로 이미 만들어져있는 스택 클래스를 호출할 수 있다. 


**3. 연습문제: 수식의 괄호 유효성 검사**

수식을 왼쪽부터 한 글자씩 읽고, 여는 괄호가 있으면 스택에 푸시하고 닫는 괄호를 만나면 스택에서 팝해서 쌍을 이루는 괄호인지 검사한다. 쌍에 해당하는 딕셔너리를 하나 만들면 된다. 스택이 비어있으면 팝이 실행되지 않으니까 올바르지 않은 수식임을 확인할 수 있다. 끝까지 검사한 후 스택이 비어 있어야 올바른 수식이다.

> 스택으로 또 어떤 문제를 해결할 수 있을까?


**4. 수식의 후위 표기법 (Postfix Notation)**

일상적으로 사용하는 수식은 중위 표기법을 따름. `(A+B)*(C+D)`처럼 연산자가 피연산자들 사이에 위치한 것이다. 후위 표기법이란 연산자가 피연산자들 뒤에 위치한 것이다. `AB+CD+*`라고 나타낸 것이다. 중위 표현식을 후위 표현식으로 바꾸는데 스택이 응용될 수 있다. 

연산자, 괄호를 있는 순서대로 스택에 쌓은 뒤 열린 괄호에 대응되는 닫힌 괄호가 나온다면 열린 괄호가 나올 때 까지 위에 쌓인걸 pop하고 열린 괄호는 버린다.

후위 표현식의 좋은 점은 이걸 사용해서 계산을 할 수 있는데 여기에서 스택을 또 활용할 수 있다고함. 뭐가 좋은건데 그래서..?

* 연산자 우선순위 설정:
```python
prec = {
    '*':3, '/':3, '+':2, '-':2, '(':1
}
```

* 알고리즘 설계:
중위 표현식을 왼쪽부터 한 글자씩 읽어서, 
- 피연산자이면 그냥 출력
- '('이면 스택에 푸시
- ')'이면 '('이 나올 때까지 스택에서 팝, 출력
- 연산자이면 스택에서 이보다 높(거나 같)은 (peek 연산 사용) 우선순위 것들을 팝, 출력
- 그리고 이 연산자는 스택에 푸시
- 스택에 남아 있는 연산자는 모두 팝, 출력 (순환문 while not opStack.isEmpty():)

```python
def solution(S):
    opStack = ArrayStack()
    answer = ''
    for c in S:
        if c not in prec and c != ")": 
            answer += c
            continue # next for loop 

        if c == "(": 
            opStack.push(c) 
            continue 

        if c == ")": 
            while opStack.peek() != '(':
                answer += opStack.pop() 
            opStack.pop() # 열린 괄호일 때 while 문이 멈추니 이것도 빼줌
            continue 

        if c in prec and c!='(': 
            while opStack.size() > 0 and prec[opStack.peek()] >= prec[c]: 
                answer += opStack.pop() 
            opStack.push(c) 
            continue 

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer 
```


**5. 후위 표기식 계산**

* 알고리즘 설계
- 후위 표현식을 왼쪽부터 한 글자씩 읽어서
- 피연산자이면 스택에 푸시
- 연산자를 만나면 스택에서 (1) 팝, (2) 팝하고 (2) 연산 (1)을 계산하고 이 결과를 스택에 푸시
- 수식의 끝에 도달하면 하나의 원소가 스택에 남아 이를 팝하면 계산 결과가 됨

```python
def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)
    
    return tokens
```
```python
def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for c in tokenList:
        if c == '(':
            opStack.push(c)
        elif c == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        else:
            if c in prec:
                if opStack.isEmpty():
                    opStack.push(c)
                elif prec[opStack.peek()] >= prec[c]:
                    while not opStack.isEmpty() and prec[opStack.peek()] >= prec[c]:
                        postfixList.append(opStack.pop())
                    opStack.push(c)
                else:
                    opStack.push(c)
            else:
                postfixList.append(c)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList
```
```python
def postfixEval(tokenList):
    valStack = ArrayStack()
    for c in tokenList:
        if c == '+':
            first_popdata = valStack.pop()
            second_popdata = valStack.pop()
            temp = first_popdata + second_popdata
            valStack.push(temp)
        elif c == '-':
            first_popdata = valStack.pop()
            second_popdata = valStack.pop()
            temp = second_popdata - first_popdata
            valStack.push(temp)
        elif c == '*':
            first_popdata = valStack.pop()
            second_popdata = valStack.pop()
            temp = first_popdata * second_popdata
            valStack.push(temp)
        elif c == '/':
            first_popdata = valStack.pop()
            second_popdata = valStack.pop()
            temp = second_popdata / first_popdata
            valStack.push(temp)
        else:
            valStack.push(c)
    answer = valStack.pop()
    return answer
```
```python
def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
```

***

# 큐 (Queues)

스택과 비슷하지만 대칭적인 성격을 갖는다. 큐는 자료를 보관할 수 있는 선형 구조인데, 넣을 때에는 한 쪽 끝에서 밀어 넣어야 하고(인큐, enqueue 연산) 꺼낼 때에는 반대 쪽에서 뽑아 꺼내야 하는(디큐, dequeue 연산) 제약이 있다. 선입선출 (First In First Out) 특징을 갖는 선형 자료 구조다.

```python
Q = Queue()
Q.enqueue(A)
Q.enqueue(B)
r1 = Q.dequeue() # A
r2 = Q.dequeue() # B
```

* 큐에 가해질 수 있는 연산
- `size()`: 현재 큐에 들어 있는 원소의 개수를 반환
- `isEmpty()`: 현재 큐가 비어있는지
- `enqueue(X)`: 데이터 x를 큐에 추가
- `dequeue()`: 큐의 맨 앞에 저장된 원소 제거 및 반환
- `peek()`: 큐의 맨 앞에 저장된 원소를 반환

큐를 추상적 자료구조로 구현하는 두가지 방법이 있는데,

- 배열을 이용한 구현: 파이썬 리스트와 메서드를 사용. O(1)의 연산 복잡도를 갖는다. `dequeue`의 경우 큐의 길이에 비례하는 복잡도를 갖는데, 맨 앞을 빼면 그 뒤에 있던걸 맨 앞으로 당겨오고 이걸 매 원소마다 반복하는 작업이 이뤄지기 때문이다. 이 부분이 비효율적이기 때문에 양방향 연결 리스트를 사용한다.

```python
class ArrayQueue:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)
    
    def dequeue(self):
        return self.data.pop(0)
    
    def peek(self):
        return self.data[0]
```

- 연결 리스트 이용한 구현: 양방향 연결 리스트 사용
```python
class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.data.getLength() == 0

    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.data.nodeCount+1 ,node)

    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data
```


**큐의 활용**

큐가 어디에 활용될 수 있을까? 자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적으로 일어나는 경우. 

![](https://s-seo.github.io/assets/images/post_DSAG_2.PNG) 
> 출처: <https://programmers.co.kr/learn/courses/57/lessons/13859>

또는 자료를 생성하는 작업이 여러 곳에서 일어나는 경우, 자료를 이용하는 작업이 여러 곳에서 일어나는 경우, 두개 모두 해당되는 경우에 큐를 활용할 수 있다. 또한 자료를 처리하여 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야 하는 작업의 경우에도 큐를 활용할 수 있다. 이러한 처리를 구현하려면 좀 어렵다. 

* 환형 큐 (Circular Queue)

정해진 개수의 저장 공간을 빙 돌려가며 이용. 큐를 배열로 구현하면 앞에 있는 노드를 뺄 때 뒤에 노드를 댕겨서 써야하기 때문에 O(n)의 복잡도가 생긴다는 문제가 있다. 환형 큐는 이러한 문제를 완화하기 위한 방법. 

```python
Q.enqueue(A)
Q.enqueue(B)
Q.enqueue(C)
r1 = Q.dequeue() # A
Q.enqueue(D)
r2 = Q.dequeue() # B
```

rear와 front라는 개념이 있다. 큐가 가득 차면 더 이상 원소를 넣을 수 없어서 큐 길이를 알고 있어야 한다. 환형 큐에는 큐의 연산에 `isFull()`이라는 연산을 추가로 정의한다. 큐가 꽉 차있는지 논리값을 반환하는 메서드다.

* 배열로 구현한 환형 큐

```python
r1 = Q.dequeue() # A
r2 = Q.dequeue() # B, front를 전진시켜서 B를 가리키게 함
Q.enqueue(F) # rear를 뒤로 옮겨 가면서. 이게 마지막 인덱스라 해도 앞의 두 자리가 비어있다.
Q.enqueue(G) # rear를 0으로 옮겨서. 이렇게 빙글빙글 돌린다. 
```

front와 rear를 적절히 계산하여 배열을 환형으로 재활용하는 것이 환형 큐의 특징이다. 

```python
class CircularQueue:
    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1


    def size(self):
        return self.count
    
    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue empty')
        self.rear = [(self.rear + 1) % self.maxCount] ###
        self.data[self.rear] = x
        self.count += 1
    
    def dequeue(self):
        if self.size == 0:
            raise IndexError('Queue empty')
        self.front = [(self.front + 1) % self.maxCount]
        x = [self.front]
        self.count -= 1
        return x
    
    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]
```

**우선순위 큐 (Priority Queues)**

큐가 FIFO 방식을 따르지 않고 원소들의 우선순위에 따라 큐에서 빠져나오는 방식. 6, 7, 3, 2의 순서로 enqueue를 했을 때 작은 수에 우선순위를 둔다면 dequeue를 할 때 2, 3, 6, 7로 나오는 것이다. 예를 들어 운영체제의 CPU 스케줄러는 우선순위가 높은 작업을 먼저 할당해서 처리하는데 여기에 우선순위 큐가 활용된다.

* 우선순위 큐의 구현

- `Enqueue`할 때 우선순위 순서를 유지하도록

- `Dequeue`할 때 우선순위 높은 것을 선택

이 중 전자가 더 유리한데, 무작위로 입력되었다면 dequeue할 때 모든 데이터를 다 살펴봐야한다. 그래서 O(n)의 복잡도가 걸리지만 enqueue할 때 우선순위를 유지하면 모든 데이터를 다 살펴볼 필요는 없다. 

또한 우선순위 큐에는 선형 배열, 연결 리스트를 이용하여 구현할 수 있다. 이 중 어느것이 유리할지? 시간적으로 볼 때는 연결 리스트를 이용하는 것이 유리하다. 중간에 데이터 삽입하는게 빈번한데 선형 배열을 이용하면 뒤의 것들을 밀어야하기 때문에 복잡도가 크다. 그렇다고 연결 리스트는 차지하는 메모리가 크기 때문에 상대적으로 선형 배열이 공간을 덜 잡아먹는 이점이 있다. 보통은 효율성을 따지기 때문에 연결 리스트를 사용해서 구현한다.

```python
from doubliylinkedlist import Node, DoublyLinkedList

class PriorityQueue:
    def __init__(self, x):
        self.queue = DoublyLinkedList()

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr.next.data != None and newNode.data < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode) # getAt() 메서드는 안쓰는데 왜? while 루프에서 getAt 메서드는 매번 처음부터 세기 때문에 비효율적
        # 우선순위에 맞춰 enqueue하는 것만 바꾸면 된다. 나머지 메서드는 동일
```



***

# 트리(Tree)

지금까지는 1차워 자료 구조를 다뤘다면 트리는 2차원 자료 구조를 갖는다. 트리는 데이터 검색, 탐색에 아주 널리 이용됨. 

- 뿌리(root)와 이파리(leaf)로 구성됨. 

- root와 leaf는 노드(node)라 하고 노드를 잇는 간선(edge)라는 개념이 있다. 더 이상 가지 치는 노드가 없다면 leaf node라고 한다. 

- 뿌리 노드나 이파리 노드가 아닌 것은 internal node라고 한다.

- 노드 사이에는 부모-자식 관계가 있다. 

- 뿌리 쪽에 가까운 노드를 부모 노드, 이파리 쪽에 가까운 노드를 자식 노드라고 한다. 

- 같은 부모에 딸린 자식 노드 간 사이에는 sibling이라는 관계를 명명한다. 

- 부모의 부모 ... 에 대응되는 노드를 ancestor node라고 한다. 반대는 descendant node라고 한다. 

- 노드에는 수준(level)이 있는데 루트 노드는 level 0부터 시작해서 자식으로 한 칸 내려갈수록 level이 1 증가한다. 거치는 간선의 개수와 동일하다.

- 트리의 높이(height) = 최대 수준(level) + 1 이며 깊이(depth)라고도 한다.

- 부분 트리(subtree): 어느 한 노드 기준으로 그 아래 있는 노드를 잘라내면 이를 subtree라고 한다.

- 노드의 차수(degree): 자식(subtree)의 수. 아래 쪽으로 가진 간선의 개수(몇 개의 자식 노드를 갖냐)와 같다. degree가 0인 것은 리프 노드다.

- 각 노드에는 하나의 부모와 여러 개의 자식이 할당될 수 있는게 트리 구조의 특징이다.


**이진 트리(binary tree)**

모든 노드의 차수가 2 이하인 트리를 의미한다. 매우 대표적인, 간단한 트리. 

- 재귀적으로 정의 
루트 노드 + 왼쪽 서브트리 + 오른쪽 서브트리 (이 때 오른쪽 서브트리 또한 이진 트리) + 종결 조건(빈 트리이거나)

- Full Binary Tree
모든 레벨에서 노드들이 모두 채워져 있는 이진 트리. 균형이 맞춰져있기 때문에 좀 더 실험하기 좋다. 정규 분포 같은 개념.

- Complete Binary Tree
높이 k인 완전 이진 트리. 레벨 k-2까지는 모든 노드가 2개의 자식을 가진 포화 이진 트리이며 레벨 k-1에서는 왼쪽부터 노드가 순차적으로 채워져 있는 이진 트리인 경우.

![](https://s-seo.github.io/assets/images/post_DSAG_3.PNG) 
> 출처: <https://programmers.co.kr/learn/courses/57/lessons/13861>


* 이진 트리의 연산 정의
- `size()`: 현재 트리에 포함되어 있는 노드의 수
- `depth()`: 현재 트리의 깊이 또는 높이(height)
- `traversal`: 정해진 순서대로 노드를 방문해서 처리하는 연산

노드가 갖는 원소: data, left child, right child
```python
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
```

root만 가리키면 각 노드가 left, right로 연결되어 있기 때문에 다 알 수 있다.
```python
class BinaryTree:
    def __init__(self, r):
        self.root = r
```

size를 구하는 것도 재귀적인 방법으로 쉽게 구할 수 있다. 
```python
class Node:
    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

class BinaryTree:
    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0
```

depth를 구하는 것도 재귀적으로. 트리의 모든 알고리즘은 재귀적인 성질을 가지고 있다. 전체 이진 트리의 depth = left subtree의 depth와 right subtree의 depth 중 더 큰 것 + 1
```python
class Node:
    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        if l > r:
            return l + 1
        else:
            return r + 1        

class BinaryTree:
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0
```

**이진 트리의 순회 (traversal)**

* 깊이 우선 순회 (depth first traversal)

- 중위 순회 (in-order traversal): left subtree -> 자기자신 -> right subtree   
![](https://s-seo.github.io/assets/images/post_DSAG_4.PNG) 
> 출처: <https://programmers.co.kr/learn/courses/57/lessons/13863>

```python
class Node:
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

class BinaryTree:
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
```
- 전위 순회 (pre-order traversal): 나를 먼저 방문
```python
class Node:
    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal
```
- 후위 순회 (post-order traversal): 마지막에 나를 방문

![](https://s-seo.github.io/assets/images/post_DSAG_5.PNG) 
> 출처: <https://programmers.co.kr/learn/courses/57/lessons/13863>

```python
class Node:
    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal
```



* 넓이 우선 순회 (breadth first traversal)

수준이 낮은 노드를 우선으로 방문하는 방식을 말한다. 같은 수준의 노드 사이에는 부모 노드의 방문 순서에 따라 방문한다. 먼저 방문한 부모를 갖는 자식 노드를 먼저 방문함. 결론적으로 이 순회 방식에선 재귀 알고리즘이 적합하지 않음.

![](https://s-seo.github.io/assets/images/post_DSAG_6.PNG) 
> 출처: <https://programmers.co.kr/learn/courses/57/lessons/13864>

- 한 노드를 방문했을 때 나중에 방문할 노드를 순서대로 기억해야함. 그래서 **큐**를 이용해야함
- root node를 가장 먼저 큐에 넣는다.
- 이걸 꺼내면 A라는 노드가 나온다. A를 방문했으니 다음에 B, C 순서대로 큐에 푸시한다.
- 큐에서 B가 나오고 B의 자식이 있으니 D, E 순서대로 큐에 푸시한다.
- 큐에서 C가 나오고, F, G의 순서로 큐에 푸시한다. 
- 따라서 D, E, F, G의 순서의 큐가 남음.
- 다음에 D를 방문하고, H를 큐에 푸시한다.
- E가 꺼내져 방문되고
- F를 방문하고 자식인 J가 있으니 이걸 큐에 푸시한다.
- G를 뽑아서 방문하고, 자식은 없으니 G에 대한 처리는 끝
- H를 꺼내서 방문하고
- J를 꺼내서 방문하고 끝
- 큐가 비어있으면 모든 노드를 넓이 우선 순회 끝냈으므로 알고리즘을 종료한다.

```python
class BinaryTree:
    def bft(self):
        queue=ArrayQueue()
        traversal=[]
        if self.root == None:
            return traversal
        else :
            queue.enqueue(self.root)
            while not queue.isEmpty():
                output=queue.dequeue()
                traversal.append(output.data)
                if output.left:
                    queue.enqueue(output.left)
                if output.right:
                    queue.enqueue(output.right)
            return traversal
```

재귀적인 방법을 쓰는게 아니라 `class Node`가 없다. 하나씩 노드를 방문하면서 큐에 쌓는 형태의 메서드가 필요하다.

- traversal 에는 빈 리스트, q에는 빈 큐를 할당
- 빈 트리가 아니면 root node를 q에 추가 (enqueue)
- q가 비어있지 않은 동안
- q에서 원소 추출(dequeue)해서 node에 담고
- node를 방문한다. (traversal에 append 한다)
- node의 왼쪽, 오른쪽 자식 (있으면)들을 q에 추가함
- q가 빈 큐가 되면 모든 노드 방문 완료




**이진 탐색 트리 (Binary Search Trees)**

모든 노드에 대해서,

- 왼쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 작고
- 오른쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 큰 

성질을 만족하는 이진 트리를 의미한다. 이 때 중복되는 데이터 원소는 없는 것으로 가정한다. 이런 성질의 트리를 데이터 검색에 유용하게 활용할 수 있다. 한 노드를 기준으로 작거나 큰 값이 한 쪽에 치우쳐 있다는 특징. 배열을 이용한 이진 탐색과 유샤해보인다. 

그럼 이진 탐색 트리와 정렬되어 있는 이진 탐색 간 차이는? 이진 탐색 트리는 데이터 원소의 추가, 삭제가 용이하다. 반면 정렬될 배열을 이용한 이진 탐색에 비해 공간 소요가 크다는 단점이 있다. 트리는 왼쪽, 오른쪽 자식을 기록해두어야 하기 때문이다. 또한 이진 탐색 트리에서도 탐색에 걸리는 시간은 O(log n)에 비례한다. 그러나 항상 O(log n)의 복잡도를 갖진 않는다.

* 추상적 자료구조

데이터 표현: 각 노드는 (key, value)의 쌍으로. 키를 이용해서 검색 가능

연산의 정의
- `insert(key, data)`: 트리에 주어진 데이터 원소를 추가
- `remove(key)`: 특정 원소를 트리로부터 삭제
- `lookup(key)`: 특정 원소를 검색
- `inorder()`: 키의 순서대로 데이터 원소를 나열
- `min(), max()`: 최소 키, 최대 키를 갖는 원소를 각각 탐색

```python
class Node:
    def __init__(self, key, data):
        self.key = key 
        self.data = data
        self.left = None
        self.right = None

class BinSearchTree:
    def __init__(self):
        self.root = None
```

```python
class Node:
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

class BinSearchTree:
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
```

```python
class Node:
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

class BinSearchTree:
    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None
```

`lookup()`에 대해, 입력 인자는 찾으려는 대상 키이고, 리턴은 찾은 노드와 그것의 부모 노드다. 부모 노드는 원소 삭제에 필요한 요인. 각각 없으면 None으로 할당. 
```python
class Node:
    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self) # self가 부모이므로
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else: 
            return self, parent
    
class BinSearchTree:
    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None
```


`insert()`는 입력 인자는 키, 데이터 원소이고 리턴은 없는 메서드다. 
```python
class Node:
    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)        
        else:
            raise KeyError('...')

class BinSearchTree:
    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)
```

원소 삭제 과정
- 키를 이용해서 노드를 찾는다.
- 해당 키의 노드가 없으면, 삭제할 것도 없음
- 찾은 노드의 부모 노드도 알고 있어야 함
- 찾은 노드를 제거하고도 이진 탐색 트리 성질을 만족하도록 트리의 구조를 정리해야 하기 때문.

입력은 키이고, 출력은 삭제한 경우 True, 해당 키의 노드가 없는 경우 False다. 또한 고려해야 할 것이

- 삭제 되는 노드가 리프 노드인 경우: 그냥 그 노드를 없애고 부모 노드의 링크를 왼쪽인지 오른쪽인지 판단해서 None으로 대입한다.
- 자식을 하나 가지고 있는 경우: 삭제되는 노드 자리에 그 자식을 대신 배치한다. 자식이 왼, 오른쪽에 있는지, 그리고 부모 노드의 링크를 왼, 오른쪽으로 어떻게 조정할 것인지 고려해야 함
- 자식을 둘 가지고 있는 경우: 삭제되는 노드보다 바로 다음 큰 키를 가지는 노드를 찾아 그 노드를 삭제되는 노드 자리에 대신 배치하고 이 노드를 대신 삭제한다. 

이다. 

```python
class Node:
    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count
```

말단 노드의 삭제, 자식이 왼, 오른쪽에 있던 그냥 삭제하고 부모 노드만 남기면 된다. 만약 삭제되는 노드가 root node인 경우는? 이 경우는 트리 전체가 없어지게끔 만들어야 함 self.root = None

자식이 하나인 노드의 삭제. 부모 노드의 링크도 조정해야함. 삭제되는 노드가 root node인 경우는? 대신 들어오는 자식이 새로운 root가 된다.

자식이 둘인 노드의 삭제, 오른쪽 자식에서 시작해서 왼쪽으로 따라가면 삭제하려는 노드보다 한 칸 더 큰 키를 찾는다. 이런 노드를 successor라고 한다. 이것의 부모 노드도 알아야함. 이것의 링크도 조정해야 하기 때문. 나머지 잘 이해못함...


```python   
class BinSearchTree:
    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.key > node.key:
                        parent.left = None
                    else:
                        parent.right = None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
                #Node(None,None)이 아니다.
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    x = node.left
                else:
                    x = node.right
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if parent.key > node.key:
                        parent.left = x
                    else:
                        parent.right = x
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = x
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if parent.key > successor.key:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
            return True
        else:
            return False
```

이진 탐색 트리가 비효율적인 경우? 한 쪽으로 완전 치우친 이진 탐색 트리의 경우, 탐색에 있어 선형 탐색과 동등한 복잡도를 갖는다. 높이의 균형을 맞추지 못하고 한 쪽으로 치우쳐져 있기 때문. 트리의 왼, 오른쪽이 비슷한 정도로 나눠져 있어야 효율성이 극대화됨. 이진 탐색과 같은 원리. 

보다 나은 성능의 이진 탐색 트리: 높이의 균형을 유지함으로써 O(log n)의 탐색 복잡도 보장함. 이렇게 유지하려면 삽입, 삭제 연산이 보다 복잡함. (AVL tree, Red-black tree)


***

# 힙 (Heap)

이진 트리의 한 종류다. 이진 힙 (binary heap)이라고도 하는데 

- 루트 노드가 언제나 최댓값 또는 최솟값을 가진다. 각각 최대 힙, 최소 힙이라고 한다. 자식들보단 큰 키를 갖는 것
- 완전 이진 트리여야 한다.
- 재귀적으로 정의했을 때도, 즉, 어느 노드를 루트로 하는 서브트리로 모두 최대 힙인 경우
- 느슨한 정렬

![](https://s-seo.github.io/assets/images/post_DSAG_7.PNG) 
> 출처: <https://programmers.co.kr/learn/courses/57/lessons/13867>

이진 탐색 트리와 비교했을 때

- BST에선 원소들이 완전히 크기 순으로 정렬되어 있지만 힙에선 크기 순으로 정렬되어 있지 않다.
- BST에선 특정 키 값을 가지는 원소를 빠르게 검색할 수 있지만 힙은 그렇지 않다. 
- 힙은 BST에 비해 완전 이진 트리여야 한다는 부가 제약을 가지고 있다.

* 최대 힙의 추상적 자료구조

* 연산의 정의
- `__init__()`: 빈 최대 힙을 생성
- `insert(item)`: 새로운 원소를 삽입
- `remove()`: 최대 원소(루트 노드)를 반환, 삭제
- traverse, 검색은 힙에 있어 관심 있는 연산이 아님

* 배열을 이용한 이진 트리의 표현

노드 번호 m을 기준으로, 왼쪽 자식의 번호는 2*m이고, 오른쪽 자식의 번호는 2*m+1이며 부모 노드의 번호는 m//2이다. 

완전 이진 트리이므로 노드의 추가, 삭제는 마지막 노드에서만 이뤄짐. 배열에 끝에 하나 추가해서 트리 크기가 커지게끔.

왜 배열? 완전 이진 트리라는 성질을 만족하기 때문에 배열로 표현하는게 적당함.

```python
class MaxHeap:
    def __init__(self):
        seld.data = [None]
```

**최대 힙에 원소 삽입**
- 트리의 마지막 자리에 새로운 원소를 임시로 저장
- 부모 노드와 키 값을 비교하여 위로,... 이동 (부모 노드가 자식보다 큰 값을 갖는 제약 조건 만족할 때 까지)

원소 삽입의 복잡도: 원소 개수 n인 최대 힙. 몇 번의 비교를 통해 노드를 적당한 위치에 올리는지, 즉, 부모 노드와의 대소 비교 최대 회수는 log_2 n 이다. 따라서 최악 복잡도는 O(log n)의 삽입 연산. 이게 최대 힙의 장점. 이걸 remove하는데 응용할 수도 있음

```python
class MaxHeap:
    def insert(self, item):
        self.data.append(item)
        index = len(self.data) - 1

        while index > 1:
            parent = index // 2
            if self.data[index] > self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break
        
```




**최대 힙에서 원소 삭제**

- 루트 노드가 원소들 중 최댓값이기 때문에 이걸 빼냄
- 빼낸 뒤에도 완전 이진 트리여야 하므로 트리 마지막 자리 노드를 임시로 루트 노드의 자리에 배치한다
- 완전 이진 트리의 모양을 갖는 조건은 만족했다. 
- 그러나 마지막 자리에서 꺼낸 노드가 현재 노드 중 최댓값은 아닐 것. 
- 이 한계를 해결하기 위해 자식 노드들과의 키 값을 비교하고, 더 큰 값과의 자리를 바꿔서 아래로 간다. 삽입 연산과 반대
- 자식 노드가 둘 있으면 어느 쪽으로 이동할 것인지? 둘 중 더 큰 값을 기준으로.

원소 개수 n인 최대 힙에서 최대 원소 삭제의 복잡도: 자식 노드들과의 대소 비교 최대 회수는 2*log n 이다. 따라서 최악 복잡도가 O(log n)의 삭제 연산이다.

```python
class MaxHeap:
def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = 2*i
        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = 2*i+1
        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if left < len(self.data) and self.data[left] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            smallest = left
        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if  right < len(self.data) and self.data[right] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right
        if smallest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)

    def maxHeapify(self, i):
        left = 
        right = 
        smallest = i
        # 자신, 왼쪽 자식, 오른쪽 자식 중 최대를 찾음
        # 이것의 인덱스를 smallest에 담음
        if smallest != i:
        # 현재 노드와 최댓값 노드의 값을 바꾸기
        # 재귀적으로 maxheapify를 호출

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data    
```



**최대, 최소 힙의 응용**

- 우선 순위 큐(priority queue)를 구현하는데 효과적
enqueue할 때 느슨한 정렬을 이루고 있도록 함. O(log n) 연산 수반. 
dequeue할 때 최댓값 순서대로 추출. O(log n)에 비례하는 복잡도.
양방향 연결 리스트 이용한 구현 방법과 효율성 비교


- 힙 정렬(heap sort)
정렬되지 않은 원소를 아무 순서로 최대 힙에 삽입, O(log n)의 복잡도.
삽입이 끝나면, 힙이 비게 될 때까지 하나씩 삭제함, O(log n)의 복잡도.
원소들이 삭제된 순서가 원소들의 정렬 순서. 
전체 정렬 알고리즘의 복잡도는 O(n log n)이다. 

```python
def heapsort(unsorted):
    H = MaxHeap()
    for item in unsorted:
        H.insert(item)
    sorted = []
    d = H.remove()
    while d: # 힙이 아직 비어있지 않은 동안에
        sorted.append(d)
        d = H.remove()

    return sorted
```


