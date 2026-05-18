#CRUD

"""
Create: 생성, 추가
Read: 조회
Update: 수정
Delete: 삭제
"""

'''
딕셔너리: {key: value}
'''

student = {
    '학번': 123456789,
    '이름': '홍길동',
    '나이': 20,
    '성별': 'M',
    '연락처': '010-1234-5678'
    }


print(f'student: {student}')
print(f'student type: {type(student)}')

#R: read
sNo = student['학번']
print(f'sNo: {sNo}')
print(f'sNo type: {type(sNo)}')
#Update
sName = student['이름']
print(f'sName: {sName}')

#Delete
del student['연락처']
print(f'student: {student}')

#keys(), values, items()
#keys(): 딕셔너리 자료형에서 키값들만 모두 뽑는다. 뽑은 키들은 리스트와 비슷한 데이터 타입이다.
keys = student.keys()
print(f'keys: {keys}')
print(f'keys type: {type(keys)}')

for key in keys: #dic_keys(['학번','이름','나이', '성별'  ])
    print(f'key: value = {key}: {student[key]}')

#values(): 딕셔너리에서 벨류값들만 모두 뽑는다. 뽑은 벨류들은 리스트와 비슷한 데이터 타입이다.
values = student.values()
print(f'values: {values}') #dict_values([1234-56789,'홍길자',20,'M'])

for value in values:
    print(f'value: {value}')
    # 둘다 타입을 보면 dickeys, 혹은 dicvalues로 리스트와 유사한 형태를 가지기에 리터블이고 for문을 사용가능

items = student. items()
print(f'items: {items}')
print(f'items: {items}')

for key, value in items:
    print(f'key: value = {key}: {value}') #구조분해할당 문법

'''
key, value = ('학번', 123456789)
'''

#구조분해할당
c= (10, 20)
a= c[0]
b= c[1]
print(f'a: {a}, b: {b}')

a= 10
b= 20

# # swapping ==> a: 20, b: 10
# temp = a
# a = b         # a: 20
# b = temp      # b: 10

# #a, b = b, a
# print(f'a: {a}, b: {b}')


#quiz) 다음은 스포츠 센터 회원 정보를 나타낸 표이다.
#파이썬으로 컨테이너 자료형으로 만드시오

# members = {
#     '2019-052001': '박찬호+25+M+010-1234-5678+헬스,수영+0'
# }

members = {
    '2019-052001': {
        '이름': '박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': ['헬스', '수영'],
        '할인률': 0
    }
}

# info = members['2019-052001']
# print(f'info: {info}')
# infos = info.split('+') # +라는 기호로 쪼개라
# print(f'infos: {infos}')

print(members['2019-052001'])
print(members['2019-052001']['이름'])
print(members['2019-052001']['나이'])
print(members['2019-052001']['할인률'])
print(members['2019-052001']['이용서비스'])






'''
데이터란?
변수
연산자
제어문(조건문, 반복문)
컨테어너형 자료구조(list, tuple, dic)
'''