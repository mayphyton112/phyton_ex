# student = {
#     '이름': '홍길동',
#     '나이': 25
# }

# print(f'나이: {student["나이"]}')

# def modifyStudentAge():
#     student['나이'] += 1

# modifyStudentAge()

# print(f'나이: {student["나이"]}')

# age =25
# print(f'age: {age}')
# def modifyAge():
#     age +=1

# modifyAge()
# print(f'age: {age}')

import copy

student01 = {
    '이름': '홍길동',
    '나이': 25
}

student02 = copy.deepcopy(student01)
student01['나이'] = 100
print(student02['나이']) #25

# x = 10

# def test():
#     x = 20

# test()

# print(x)

x = 10

def test():
    x = 20
    print(x)   # 파이썬은 =을 보면 기본적으로 지역변수라고 생각한다.
               # 그렇기에 함수 안의 X=20을 보고 이것을 전역변수로 여기지 않고 지역변수로 본 것
test()
print(x)

#10 20