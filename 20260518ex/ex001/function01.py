# '''프로그래밍의 함수 또한 수학의 함수와 동일하게 값을 넣어주면 
# 특정 기능을 수행한 연산 결과를 출력합니다. 
# 여기서 특정 기능이란 뎃셈과 같은 비교적 간단한 연산부터 
# 네트워크 연결, 회원인증, 메일 발송과 같이 복잡하고 어려운 작업까지 모두 포함한다.
# '''

# #python에서는 함수(function)가 꽃이다.

# #함수 정의하기
# '''
# 사용자 함수를 만든다는 것은 '함수를 정의 한다'라고 한다.
# 함수를 정의할 때 def 키워드를 사용한다.
# 그리고 함수명 : 실행부를 이용한다.
# '''
# '''
# num = 10
# def 함수명():
#     실행부(함수 기능) #프로그램에서 어떤 것의 뒤에 ()이 있으면 함수다.
# '''

# def greet():
#     print('안녕하세요')
#     print('반갑습니다.')
#     print('저는 홍길동입니다.')


# '''
# 함수명 규칙
# 1. 내장함수명과 동일하면 안된다.
# 2. 첫글자는 주로 소문자로 시작한다.
# 3. 첫 글자는 숫자를 쓸 수 없다. 1greet(x), g1reet(0), greet1(0)
# 4. _를 뺀 특수문잘는 사용할 수 없다.
# 두 개 이상의 단어가 조합되는 경우 스네이크 또는 카멜 표기법을 사용한다. 
#     sendMessage(): calculateDistance():
# '''

# # 온도센서 작동 시스템 만들기
# #온도센서를 작동을 시작하고 먼추는 함수를 정의 해보자
# #함수명은 함수의 기능을 이해하기 좋도록 짓는다.

# #함수 선언
# def startTemperatureSensor():
#     print('온도센서 작동을 시작합니다.')


# def stopTemperatureSensor():
#     print('온도센서 작동을 중지합니다.')

# #함수 호출
# startTemperatureSensor()
# stopTemperatureSensor()

# '''
# 고등학교 졸업 기념으로 노트북을 하나 장만했습니다.
# 노트북 사이즈에 꼭 맞는 파우치를 하나 구매하려고 하는데 사이즈 표에 인치로만 표시되어있습니다.
# cm를 인치로 바꿔주는 함수를 만들어보자
# 1inch = 0.393701cm)
# '''

# def convertUnit():
#     lenghtCM = float(input('길이(cm) 입력:'))
#     print(f'인치: {lenghtCM * 0.393701:.2f}:inch')

# convertUnit()


# #이동거리를 계산하는 함수
# '''
# 길동이는 5시간 동안 3km/h의 속도로 등산을 했습니다.
# 길동이가 등산한 시간과 속도를 입력하면 이동한 거리를 계산해주는 프로그램을 함수를 이용해 만들어봅시다.
# '''

# def calculateDistance():
#     print(f'이동거리: {hourData * speedData}km')

# hourData = float(input('이동시간: '))
# speedData = float(input('이동속도: '))

# calculateDistance()

#pass 키워드
# def calculateNumber():
#     pass

# #함수 내에서 또 다른 함수 호출
# def fun1():
#     print('fun1() CALLED')

# def fun2():
#     print('fun2() CALLED')

# def fun3():
#     fun1()
#     fun2()
#     print(f'fun3() CALLED')

# fun3()
# '''
# print('fun1() CALLED')
# print('fun2() CALLED')
# print(f'fun3() CALLED')
# '''
#재귀함수  이런것이 있다고만 알고있어도 괜찮다.
# def fun4():
#     print('fun4() CALLED')
#     fun4()

# fun4()

# def factorial(n):
#     if n == 1:          # 종료 조건
#         return 1
    
#     return n * factorial(n - 1)   # 재귀 호출

# print(factorial(5))

#다국어 인사말 프로그램을 함수로 만들어라
'''
사용자가 출신국가를 선택하면 해당하는 국가으이 인사말이 출력되는 프로그램을 함수를 이용해 만들어보자
1. 한국  2.USA  3. Japan
'''

# def introKor():
#     print('안녕하세요')

# def introEng():
#     print('Hello')

# def introJap():
#     print('こんにちは')
# selectedMenuNum = int(input('Where are you from? 1. 한국  2.USA  3. Japan'))

# if selectedMenuNum ==1:
#     introKor()

# elif selectedMenuNum ==2:
#     introEng()

# elif selectedMenuNum ==3:
#     introJap()

#함수를 사용해 계산기 프로그램 만들기 
'''
사용자가 숫자 2개를 입력하고 연산자를 선택하면 연산결과가 출력되는 프로그램을 함수를 이용해서 만들어보자
'''

def add():
    print(f'덧셈 결과: {inputNumber1 + inputNumber2}')
def sub():
     print(f'뺄셈 결과: {inputNumber1 - inputNumber2}')
def mul():
     print(f'곱셈 결과: {inputNumber1 * inputNumber2}')
def div():
    print(f'나눗셈 결과: {inputNumber1 / inputNumber2}')


def calculator():
    if selectedOperator == 1:
        add()
    
    elif selectedOperator ==2:
        sub()
    
    elif selectedOperator ==3:
        mul()
    
    elif selectedOperator ==4:
        div()

inputNumber1 = float(input('숫자 입력'))
selectedOperator = int(input('연산자를 선택하라. 1.덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈'))
inputNumber2= float(input('숫자 입력'))

calculator()
