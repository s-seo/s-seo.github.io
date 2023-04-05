---
layout: default
title:  "OOP with Class (1)"
parent: Python
permalink: /Python/PythonOOP_1
# nav_order: 97
---




***

최근 컴퓨터에 알 수 없는 에러가 뜨기도 하고 예전보다 확실히 느려진 것 같다고 느껴 1년만에 포맷했다. 그러면서 Python, VSC 등 여러 개발 환경 셋팅을 다시 하는 중인데 향후 개발 공부를 위해서라도 관련 프로세스를 정리하고자 한다.


> **상황: 처음 사용하는 컴퓨터에서 내가 개발 프로젝트 하나를 시작하려고 한다.**

코드 에디터에는 여러 종류가 있는데(VSC, PyCharm, Beam 등) 여기선 VSC를 사용한다.


***

# 설치 프로그램

1. [Python 3.7](https://nitr0.tistory.com/263)
2. [ANACONDA (3.7)](https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe)   
3. [Visual Studio Code](https://code.visualstudio.com/)


***

# 개발 환경 세팅 프로세스

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
    - venv, pipenv 등의 가상환경이 있지만 conda를 제일 많이 쓰고 이미 Anaconda가 설치되어 있기 때문에 conda를 사용하여 가상환경을 설정하겠다. 가상환경이란 한 컴퓨터에서 여러 프로젝트를 작업할 때 파이썬 패키지의 의존성이 충돌하지 않도록 관리하는 툴이다. 가상환경을 생성하면 환경변수 그룹이 만들어지고 그룹마다 지정된 경로에 패키지를 설치해서 참조한다. 패키지 버전 관리가 생각보다 까다로운데 가상환경으로 이를 효율적으로 관리할 수 있는 것.

        - Anaconda는 파이썬의 여러 배포판 중 한 종류이다. 데이터 사이언스를 위한 여러 패키지를 포함하고 있어 한번에 설치가 가능하다는 이점이 있다.
        - Jupyter Notebook은 오픈 소스 web API다. 이름에서 알 수 있듯이 일종의 문서인데, 코딩에 특화된 것이라 생각하면 편하다. 특히 실시간으로 데이터 조작, 시각화 및 공유가 편리하다는 특징이 있다.

    - 아나콘다를 설치하면 "base"라는 가상환경이 자동적으로 생성된다. 여기는 일종의 허브로 두고 뭘 설치하거나 그러진 말자... 내가 그래서 여러모로 골치가 아팠다ㅠ

    - 먼저 `$ conda update conda`를 실행해서 최신 버전의 conda로 업데이트해준다.

    - `$ conda create --name 가상환경이름 python=파이썬버전` 명령어를 실행하여 가상환경을 생성한다. `$ conda env list`를 실행해 생성된 가상환경 목록을 확인할 수 있다.

    - `$ conda activate 가상환경이름`를 실행해 생성한 가상환경으로 들어갈 수 있다. 그럼 (base)가 (가상환경이름)으로 바뀐다. 

    - 해당 가상환경을 주피터 노트북과 연동할 수 있다. (사실 VSC에서 작업하기 때문에 이 과정이 반드시 필요한건 아니지만, 나중을 위해) 이를 위해 ipykernel이라는 라이브러리를 설치해야한다. 해당 가상환경 안에서 `$ conda install ipykernel`을 실행한다. `$ conda list`를 실행하면 해당 가상환경 안에서 설치된 라이브러리 목록을 확인할 수 있다.

    - ipykernel을 설치했으면 이를 가상환경과 연동시켜야 한다. `python -m ipykernel install --user --name 가상환경이름 --display-name "[가상환경이름]"`을 실행한다. 이는 주피터 노트북에서 사용할 커널의 가상환경 이름을 `[가상환경이름]`으로 설정하는 것이다. 

    - `$ conda deactivate`을 실행해 base로 돌아간 뒤 `$ jupyter notebook`을 입력해 주피터 노트북을 실행한다. `new`를 클릭해 가상환경이름이 부여된 커널을 통해 특정 작업을 수행할 수 있다. 
   
    ● (0826) 막상 이렇게 작업을 해보려니까 에러가 좀 생겼는데, anaconda prompt에서 가상환경에 들어간 상태에서 주피터 노트북을 실행하느냐 vs base 환경에서 주피터 노트북을 실행하느냐 이 차이와, 기본 Python 3 커널을 쓸 것인지 vs 해당 가상환경 커널을 쓸 것인지에 따라 헷갈렸다. 결론적으론 해당 **가상환경에 들어간 상태**에서 아무 커널을 사용하면 패키지 설치, 사용에 문제 없는 것 같다. base 환경에서 주피터 노트북을 실행한 뒤, 아무 커널에 들어가서 패키지를 import하면 
   
    > *Original error was: DLL load failed: 지정된 모듈을 찾을 수 없습니다.*

    이런 에러가 뜨는데, 이는 아나콘다를 환경변수에 추가하지 않아서 발생하는 에러다. 근데 설치할 때 아나콘다를 환경변수에 추가한다고 설정했는데?라는 생각이 들면 <https://conda.io/activation>을 참고하자. 환경변수 개념은, 특히 윈도우에서, 아직 익숙하지 않아서 관련된 문제가 있다는 것만 알고 제대로 이해하지 못했다. 다만 가상환경에서 작업한다면 pandas, numpy와 같은 패키지를 다시 anaconda prompt에서 설치해야 하는 것 같다. 만약 base에서 쓰던 패키지를 그대로 쓰고 싶다면 그냥 requirements.txt로 빼내서 다운받는 방법이 있을텐데.. 뭔가 더 직관적인 방법이 있을테지만 일단 보류! 발생 가능한 상황과 그 결과에 대해 정리하면 다음과 같다.

        - base 환경 + python3 커널: 그냥 일반적인 사용환경. 내가 평소 작업하던 환경이니까 패키지도 그대로 있음.
        - baes 환경 + 가상환경 커널: 마찬가지로 평소 작업하는 패키지 그대로 있다.
        - 가상환경 + python3 커널: 내가 anaconda prompt에서 직접 설치한 패키지만 있다. 아나콘다에서 제공해주는 패키지들 설치 안되어 있음.
        - 가상환경 + 가상환경 커널: 위와 똑같다.

    - 여튼 이렇게 가상환경 상에서 작업하면 좋은 점은 내가 생각했을 때,

        - 가상환경이 설치된 dir를 default로 사용한다
        - 해당 가상환경에 설치된 라이브러리를 사용할 수 있다. 매번 다시 설치할 필요가 없는 것
        - 주피터 노트북에서 ipynb 파일이 아닌 프로젝트를 실행하는 개념이 되는 것 

    - conda 명령어는 아래와 같다.

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

    - 가상환경에서 패키지 설치, 업데이트, 삭제. 

        ```
        $ conda activate 가상환경
        $ conda install 패키지이름
        $ conda update 패키지이름
        $ conda remove 패키지이름
        ```

        * (0826) 이 때 한가지 유의할 점은 패키지 설치, 업데이트, 제거는 anaconda prompt에서 해야한다. 나는 뭣도 모르고 주피터 노트북에서 작업하다가 계속 설치가 안돼서 짜증났었다... 또 패키지 설치 등을 할 때 굳이 어떤 경로로 이동하지 않아도 된다. 그냥 기본 경로에서 작업해도 된다. 그 경로에 해당하는 폴더 안에 저장하는게 아니라 가상환경(?)에서 작업해서 그런가..?

        * (0826) pandas와 같이 `proceed? [y/n]`을 묻지 않는 경우라면 주피터 노트북에서 `!pip install 패키지`로 패키지 설치해도 문제 없는 것 같다.


    - 특정 가상환경에서 패키지 설치, 삭제

        ```
        conda install -n 가상환경이름 패키지이름
        conda remove -n 가상환경이름 패키지이름
        ```

    - 주피터 노트북 명령어

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


