fruits = {
    'summerfruits':{
        '사과' : 'apple',
        '수박' : 'watermelon',
        '자두' : 'plum'
    },
    'spiringfruits': {
        '딸기' : 'strawberry',
        '오렌지': 'orange',
        '체리' : 'cherry'
    }
    }
# print(f'fruits: {fruits}')
# ======>변수를 포함한 딕셔너리 값 전체 출력
# print(fruits)
# =======>변수를 제외한 딕셔너리의 전체값 출력

# print(fruits.keys())
# print(fruits['spiringfruits']['딸기'])
# =======>특정 값 출력-springfruit 딕셔너리 안 딸기(Strawberry)의 벨류값
# print(fruits['spiringfruit'].keys())
# =======>springfruit의 키에 해당하는 사과, 수박, 자두를 출력
# print(fruits['spiringfruit'].values())
# =======>springfruit의 벨류에 해당하는 strawberry, watermelon, plum을 출력
# print(fruits['spiringfruit'].items())
# =======>springfruit의 아이템값에 해당하는 (딸기, strawberry)의 값을 가져온다.
# print(type(fruits) =======> 딕셔너리의 타입은 dictionary이다. 


#조회
# print(f"apple : {fruits['summerfruits']['사과']}")
#특정값 조회 
# print(f'type(fruit): {type(fruits["summerfruit"])}')

#추가

# fruits['summerfruits']['포도'] = 'grape'
# print(f'summerfruits: {fruits['summerfruits']}')
'''
복합 딕셔너리에서 정보 추가하는 방법
토이프로젝트에서의 memberAccountDb[uId]['uPw'] 라는 코드와 구성이 같다.
가장 상부에 있는 딕셔너리의 이름만 앞에 쓸 수 있는 듯 하다.
가장 앞에있는 딕셔너리의 이름 + 추가하고자하는 딕셔너리의 이름 + 추가하고자 하는 정보의 키와 벨류값
'''

#수정
# fruits['summerfruits']['수박'] = 'oriental melon'
# print(fruits['summerfruits'])
'''
기본적으로는 추가와 문법 구조가 같다.
키는 불변하는 값이라 수정할 수 없다.
'''

#삭제
# del fruits['summerfruits']['자두']
# # print(f'fruits: {fruits}')
# print(f'summerfruits : {fruits['summerfruits']}')

#삭제 후 추가
# del fruits['summerfruits']['자두']
# fruits['summerfruits']['참외'] = 'oriental melon'
# print(f'summerfruits : {fruits["summerfruits"]}')

'''
우선 지우고자하는 항목을 삭제하고 다시 추가해서 딕셔너리의 새로운 키와 벨류값을 정한다.
'''

# 아이템 개수(길이) 조회
# print(f'아이템의 개수: {len(fruits)}')
# print(f'아이템의 개수: {len(fruits["summerfruits"])}')
"""
아이템의 개수 조회 길이를 나타내는 내장함수 len을 사용한다.
상위 딕셔너리의 이름 + 그 안의 딕셔너리
"""


#함수
# def hello():
#     print('안녕하세요')
# hello()

#매개변수
def hello(name):
    print(f'{name}님 안녕하세요')
hello('김태준')

def add(a, b):
    print(a + b)
add(10,20)

def sub(a, b):
    print(a - b)
sub(10, 20)

def mul(a, b):
    print(a * b)
mul(10, 20)

def div(a, b):
    print(a / b)
div(10, 20)

def quot(a, b):
    print(a // b)
quot(10, 3)

def mod(a, b):
    print(a % b)
mod(10, 2)

def pow(a, b):
    print(a**b)
pow(3, 3)

#리턴
def add(a, b):
    return(a + b)


result = add(10, 20)
print(result)

def sub(a, b):
    return(a -b)

result = sub(10 -20)