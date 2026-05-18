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
# 이 이유는 deepcopy로 데이터까지 복사해왔기에 student02는 01과 같은 값을 가지게 되는데 그렇기에 01이 바뀌어도 02의 값은 여전하다.
# 하면 같은 데이터를 가리키는 것이 아니라,
# 아예 새로운 데이터를 따로 복사해서 가지게 됩니다.


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