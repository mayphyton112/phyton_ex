# # 컨테이너 자료형?
# # 여러 개의 데이터를 묶어 관리하는 것을 말한다.
# fruit1 =  '사과'
# fruit2 =  '포도'
# fruit3 =  '복숭아'

# fruits = ['사과', '포도','복숭아' ] #컨테이너 자료형 list
# print(f'fruits: {fruits}')  #복수로 하는 것을 권장한다.
# print(f'fruits type: {type(fruits)}')

# #파이썬에서는 컨테이너 자료형으로 리스트, 튜플, 딕셔너리가 있다
# #리스트 선언
# #fruits = ['사과', '포도','복숭아' ] 이런 식으로 정의(선언+ 초기화)를 거친다.
# #index: 아이템에 부여된 고유의 값: 0부터 시작한다.
# # ->아이템을 식별하기 위한 식별번호이다.

# # fruits = ['사과', '포도','복숭아' ]
# #             0       1      2
# print(f'fruits: {fruits[0]}') # 사과
# print(f'fruits: {fruits[1]}') # 포도
# print(f'fruits: {fruits[2]}') # 복숭아
# print(f'fruits: {fruits[3]}') # IndexError: list index out of range
# #=>list의 범위에 없는 값을 요구했기 때문

# #리스트의 길이(아이템 개수)
# cnt = len(fruits)  #3
# print(f'cnt: {cnt}')
# #리스트의 마지막 아이템의 인덱스 값의 '리스트의 길이 -1'이다.
# #ex) print(f'last data: {fruits[len(fruits)-1]})
# print(f'first data: {fruits[0]}')

# # 리스트의 전체 데이터 반복조회
# # 리스트는 반복가능한 객체에 해당한다.=>이터러블한 데이터
# for fruit in fruits:  #인덱스, 아이템
#     print(f'fruit: {fruits}')

# for idx, fruit in enumerate(fruits):
#     print(f'index: {idx}, fruits: {fruits}')

#by while문

# while i < len(fruits):

#아이템 삽입
#리스트 마지막에 삽입
fruits= ['사과', '포도','복숭아' ]
fruits.append('수박')
print(f'fruits: {fruits}')

#특정 위치에 삽입
fruits.insert(1,'멜론')
print(f'fruits: {fruits}')
'''
추가하고자 하는 아이템의 인덱스 번호, 아이템의 이름
즉 fruits= ['사과', '포도','복숭아' ]일때 멜론을 사과 뒤에 넣고 싶다면
원래 두 번째 왔던 아이템인 포도의 인덱스 값인 1과 '멜론'을 ()에넣는다.
'''

# 리스트 연결
list1 = [1,2,3]
list2 = [10,20,30]
list1.extend(list2)
#list 1의 값이 list 2뒤에 복사됨

#리스트 연결: +
list3 = list1 + list2  #새로운 메모리 공간에 만들어진다.
print(f'list3: {list3}')

#아이템 삭제
sports = ['football', 'baseball', 'volleyball', 'basketball']

#마지막 아이템 삭제하기
sports.pop()
print(f'sports: {sports}')

#특정 아이템 삭제하기
sports.pop(1)
print(f'sports: {sports}')

#pop() 비슷하게 사용할 수 있는 키워드 del
del sports[1]
print(f'sports: {sports}')

nums = [1, 2, 3, 4, 5, 6]
nums.pop(3)
deletedNum = nums.pop(3)
print(f'deletedNum: {deletedNum}')

#특정 아이템 삭제 by 아이템
langugaes = ['c/c++', 'c#', 'java', 'python']
#languages.pop(2) # ['c/c++', 'c#','python']

langugaes.remove('java')
print(f'languages: {langugaes}')

#remove()룰 이용해서 아이템을 삭제할 때 삭제하려는 아이템의 개수가 2개 이상일때?
langugaes = langugaes = ['c/c++', 'c#', 'java', 'python', 'java']
langugaes. remove('java')
print(f'languages: {langugaes}')

'''
다음은 냉장고에 있는 과일을 리스트로 나타낸 것이다.
['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
이중 과일이 아닌 당근과 토마토를 찾아 삭제하는 프로그램을 만들어봅시다.
'''
fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
print(f'fruits: {fruits}')

for item in fruits:
    if item in fruits:
        if item == '당근' or item == '토마토':
            fruits.remove(item)
print(f'fruits: {fruits}')

'''
다음은 홍길동 수험생의 2020년 공인중개사 자격증 시험 성적표입니다.
아래 합격 기준에 만족하는지 구하는 프로그램을 만들어봅시다.
-매 과목 100점을 만점으로 하여 매 과목 40점 이상
-전 과목 평균 60점 이상 득점

홍길동 수험생 성적표
부동산 개론: 55점
민법:       35점
공법:       40점
공시법:     70점
세법:       65점
중개사법:   30점
'''
scores = [55, 35, 40, 70, 65, 30]
 
total        = 0        # 총점         =>코드 컨벤션의 예
underSubject = 0        #과락과목 개수
average      = 0

for score in scores:
    if score < 40:
        underSubject +=1
    total += score

print(f'40점 미만 과목 수: {underSubject}')
average = total / len(scores)

# print(f'평균: {total/6}')         #지양하자
print(f'평균: {(total/len(scores)):.2f}') #지향하자

#합격 여부
if underSubject > 0 or average < 60:
    print(f'아쉽습니다. 다음기회에')
else:
    print(f'합격입니다.')