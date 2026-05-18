'''
tuple이란 리스트와 비슷하게 데이터를 묶어 처리하는 컨테이너 자료형이다.
다만 튜플에 포함된 아이템은 수정할 수 없다.
데이터 수정을 막아야 할 경우 리스트 보단 튜플이 더 안전할 수 있다.
선언방법은 리스트와 같으나 []가 아닌 ()를 사용한다.
'''
fruits = ('사과', '포도', '수박', '참외','배')
fruits     #아이템 출력
type(fruits) # tuple 타입으로 나온다.

# fruits = ('사과', '포도', '수박', '참외','배', '자두', '복숭아', '바나나')
# print(f'fruits: {fruits}')
# print(f'fruits type: {type(fruits)}')

#튜플 조회하기
'''
튜플은 아이템의 수정이 불가능하기에 아이템의 삽입, 삭제, 정렬 등의 기능은 없고
조회하는 기능을 주로 사용한다.
'''
fruits = ('사과', '포도', '수박', '참외','배', '자두', '복숭아', '바나나')
print(f'{fruits[3]}') #참외

# 튜플에서 인덱스가 홀수인 아이템 조회하기
sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')

for idx, item in enumerate(sports):
    if idx % 2 ==1:
        print(f'idx: {idx}, item: {item}')

#특정 아이템의 인덱스 조회
#튜플 내 특정 아이템의 인덱스를 확인할 떄는 index()함수를 이용한다.
fruits = ('사과', '포도', '수박', '참외','배', '자두', '복숭아', '바나나')
print(f'idx: {fruits.index('바나나')}')

#튜플에서 사용자가 선수 이름을 입력하면 이름에 해당하는 인덱스를 출력해보자
names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')

# inputData = input('선수이름 입력:')
# print(f'이름: {inputData}, 인덱스: {names.index(inputData)}')

#튜플 안의 아이켐 유/무 확인하기
# in과 not in 키워드를 사용하면 튜플 안에 특정 아이템의 존재 유/무를 확인할 수 있습니다.
colors = ('Red', 'Orange', 'Yellow', 'Green','Blue', 'Indigo', 'Purple')
print(f'{'Green' in colors}')

if 'Green' in colors:
    print('colors 에는 Green이 있습니다.')
else:
    print('colors 에는 Green이 없습니다.')

if 'Green' not in colors:
    print('colors 에는 Green이 없습니다.')
else:
    print('colors 에는 Green이 있습니다.')

#학점 경고 프로그램 만들기
'''
Scores는 1학기 성적을 튜플로 나타낸 것입니다. F학점이 있으면 '경고'를 출력하는 프로그램을 만들어라
scores = ('A', 'A+', 'B', 'B-', 'F')
'''

scores = ('A', 'A+', 'B', 'B-', 'F')
if 'F' in scores:
    print('경고')
else:
    print('경고 없음')  

scores = ('A', 'A+', 'B', 'B-', 'F')
fCnt= scores.count('F')
print(f'F학점 개수: {fCnt}')

#튜플 결합
#at list
nums1 = [10, 20, 30]
nums2 = [1, 2, 3]

#첫번째
# nums1.extend(nums2)
# print(f'nums1: {nums1}')

#두번째
result = nums1 + nums2
print(f'nums1: {nums1}')
print(f'nums2: {nums2}')
print(f'result: {result}')

#at tuple
nums1 = (1, 2, 3)
nums2 = (10, 20, 30)

# nums1.exten(nums2)
result = nums1 + nums2
print(f'nums1: {nums1}')
print(f'nums2: {nums2}')
print(f'result: {result}')

num1 = 10
num2 = num1
print(f'num1: {num1}')
print(f'num2: {num2}')


num1 = 100
print(f'num1---: {num1}')  #100
print(f'num2---: {num2}') #10


nums1 = [1,2,3]
nums2 = nums1
print(f'num1: {num1}')
print(f'num2: {num2}')

# nums1[0] = 100
# print(f'nums1+++: {nums1}')
# print(f'nums2+++: {nums2}')


#깊은 복사
nums1 = [1,2,3]
nums2 = [0,0,0]

for idx, num in enumerate(nums1):
    nums2[idx] = num

print(f'nums1: {nums1}')
print(f'nums2: {nums2}')

nums1[0] = 100
print(f'nums1: {nums1}')
print(f'nums2: {nums2}')



# idx = 0
# num = 1

print('deep copy ---------------------------------')

import copy

a = [1, 2, 3, 4, 5]
# b = copy.deepcopy(a)
b = a.copy()

b[0] = 100

print(f'a : {a}')
print(f'b : {b}')

#슬라이싱
animals = ('호랑이', '사자','곰', '여우', '늑대')
print(f'animals: {animals}')
print(f'animals[:3]: {animals[:3]}')
print(f'animals[1:4]: {animals[1:4]}')
print(f'animals[:-2]: {animals[:-2]}')
print(f'animals[:-2]: {animals[1:-2]}')
print(f'animals[:-2]: {animals[-3:-1]}')

#슬라이싱 연습하기
'''
fruits 튜플에서 주어진 요구사항에 맞게 슬라이싱해봅시다.
fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
 - 인덱스 2부터 4까지의 아이템을 출력하시오.
 - 인덱스 0부터 3까지의 아이템을 출력하시오.
 - 인덱스 3부터 끝까지의 아이템을 출력하시오.
'''
#           0          1
fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
print(f'fruits:[2:5]: {fruits[2:5]}')
print(f'fruits:[0:4]: {fruits[0:4]}')
print(f'fruits:[3:]: {fruits[3:]}')

#리스트와 튜플간 변환(형변화, casting)
'''
불가피하게 튜플의 아이템을 수정하려면 리스트로 변환해야 합니다.
또한 리스트로 선언된 데이 터를 수정이 안 되게 하려면 튜플로 변환해야 합니다.
다음은 데이터 변환을 통해 리스트와 튜플을 변환하고 있습니다.
'''


colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# # Orange => 오렌지
# colors[1] = '오렌지'
colors = list(colors)  
print(f'color type: {type(colors)}')

colors[1] = '오렌지'     
print(f'colors: {colors}')      #리스트

colors = tuple(colors)          #튜플
print(f'colors: {colors}')

#튜플 정렬
# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# colors.list(colors)
# colors.sort()
# print(f'colors: {colors}')

# colors = tuple(colors)
# print(f'colors: {colors}')

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

cs = tuple(sorted(colors)) #오름차순으로만 정리가 된다. 
print(f'cs: {cs}')





