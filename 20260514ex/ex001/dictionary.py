#딕셔너리(dictionary)
#리스트와 함께 파이썬에서 많이 사용하는 컨테이너 자료형
#리스트가 인덱스를 이용하여 아이템을 참조한다면, 딕셔너리는 인덱스 대신 key를 이용하여 아이템을 참조한다.

#딕셔너리 정의
#딕셔너리는 {}

('박찬호', '박지성', '박세리', '이승엽')
{'박찬호': 48, '박지성': 40, '이승엽': 43, '박세리': 50}
#앞에 나오는 값이 키, 콜론(:) 뒤에 나오는 것이 value 아이템 구분을 , 로 하는 것은 나머지 둘 과 같다.
#딕셔너리를 선언할 떄는 ({}), 중괄호를 사용한다.
#하나의 딕셔너리에서 키의 값은 중복되면 안된다. value는 중복되어도 된다.
ages = {'박찬호': 48, '박지성': 40, '이승엽': 43, '박세리': 50}
print(f'ages: {ages}')
print(f'ages type: {type(ages)}')

scores = {
    'c/c++': 'A',
     'Java' : 'B+',
     '네트워킹' : 'C',
     '보안': 'A+',
     '해킹': 'F',
     '시스템': 'C+'

}

print(f'scores: {scores}')

# 마지막 내용: ********************************************
#리스트, 튜플, 딕셔너리

tupleVar = [3, 3.14, 'hello']
print(f'tupleVar: {tupleVar}')

dictVar = {
    '홍길동' : 10,
    '박찬호' : '열살',
    '박세리' : 3.14,
}
print(f'dictVar: {dictVar}')
listVar1 = [1, 2, 3]
listVar2 = [1, 2, 3, listVar1]

print(f'listVar1 : {listVar1}')
print(f'listVar2 : {listVar2}')

print(listVar2[3][1])
print(type(listVar2[3]))
print(type(listVar2[3][1]))

dicts = {
    'name': '박찬호',
    'age': 20,
    'addr' : '대전 중구',
    'hobby': ['축구', '농구', '배구'],
    (1, 2, 3) : 10 #키 값은 불변하는 데이터로 한다.
}

print(dicts)

print(f'dicts: {dicts}')
'''
{'name': '박찬호','age': '20','addr' : '대전 중구','hobby': ['축구', '농구', '배구'}
'''

print(dicts['hobby'][1])

'''
nums[][]
'''

#3차원부터는 가능은 하지만 쓰지 않는 것이 좋다.

'''
-PC방 자리 관리 프로그램 

너는 PC방 사장이다.
손님이 자리에 앉으면 "사용중" 으로 바뀌고, 비어있으면 예약할 수 있다.
'''

seats = {
    1: "빈자리",
    2: "사용중",
    3: "빈자리",
    4: "사용중",
    5: "빈자리"
}

'''
프로그램 요구사항
1.현재 자리 상태를 전부 출력하기
2. 사용자에게 원하는 자리 번호 입력받기
3.예약할 자리 번호 :
4.빈자리라면 "예약 완료" 출력 해당 자리 상태를 "사용중" 으로 변경 이미 사용중이라면 이미 사용중인 자리입니다 출력
5.예약 후 전체 자리 상태 다시 출력하기
'''
#1.
# seats={1: "빈자리", 2: "사용중", 3: "빈자리", 4: "사용중", 5: "빈자리"}
# print(f'seats: {seats}')
# userinputdata = int(input('번호를 입력하세요:'))
# if seats[userinputdata] == "빈자리":
#     print("예약 완료")
#     seats[userinputdata] = "사용중"
# else: print ("이미 사용중인 자리입니다.")
# print(f'seats: {seats}')

'''
- 배달 주문 통계 프로그램 
배달 앱에서 하루 주문 데이터를 분석하려고 한다.
주어진 주문 목록
'''
orders = [
    "치킨",
    "피자",
    "치킨",
    "햄버거",
    "피자",
    "치킨"
]
'''
프로그램 요구사

1. 각 음식이 몇 번 주문됐는지 딕셔너리에 저장하기
2. 가장 많이 주문된 음식 찾기
3. 총 주문 개수 출력하기
4. 사용자가 음식 이름 입력하면
몇 번 주문됐는지 출력하기
'''

# orders_count = {"치킨": 3, "피자": 2, "햄버거": 1}
# # max_Orders = max(orders,key=orders_count.get())
# total = sum('orders_count.values()')
# print(f'총 주문개수:  {total}')
# print(f'음식이름: {orders_count}')


'''
-시험 결과 분석 프로그램 
학원에서 시험 결과를 분석하려고 한다.
주어진 데이터
'''
scores = {
    "민수": 88,
    "지훈": 72,
    "수아": 95,
    "유진": 64,
    "서연": 100
}

'''
프로그램 요구사항
1.전체 학생 점수 출력하기
2.평균 점수 계산하기
3.최고 점수 학생 찾기
4.60점 이상은 합격, 미만은 불합격 출력하기
5.90점 이상 학생 수 출력하기
6.점수 높은 순으로 학생 출력 도전하기
'''
# test_scores= {"민수": 88,"지훈": 72,"수아": 95,"유진": 64,"서연": 100}
# print(f'test_scores: {test_scores}')
# total = sum(test_scores.values())

'''
딕셔너리 조회/삽입/수정/삭제
컴퓨터 프로그램에서 '조회/삽입/수정/삭제'를  CRUD라고 한다.
CRUD라는 용어는 개발자라면 반드시 알고 있어야 하며
이는 각각 Create, Read, Update, Delete를 뜻한다.
즉, 데이터를 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 하는 것을 말하며 
딕셔너리에서의 CRUD는 딕셔너리 컨테이너 자료형에 데이터를 추가, 조회, 수정, 삭제하는것을 말할 것이다.
CRUD는 프로그래밍 뿐만 아니라 데이터베이스에서도 사용되는 용어이다.
'''

#추가(Create)
dicContainer = {
    '이름': '홍길동',
    '나이': 25,
    '주소': '대전 중구',
    '취미': ['축구', '수영', '조깅'],
    '몸무게': 87.5
}
print(f'dicContainer: {dicContainer}')

dicContainer['연락처'] = '010 -1234-5678' 
print(f'dicContainer: {dicContainer}')

#조회(Read)
print(f'이름: {dicContainer['이름']}')

#수정(Update)
dicContainer['몸무게'] = 50 #87.5인 벨류가 50으로 바뀐다. 수정하고자 하는 아이템의 키 값을 바꾸고 벨류를
#새로 적어넣는다.

#삭제(Delete)
del dicContainer['몸무게']
print(f'dicContainer: {dicContainer}') #삭제된 정보는 복구되지 않는다.

# 부가 기능들
# 아이템 개수 조회
print(f'아이템 개수: {len(dicContainer)}')

# 전체키 & 벨류 조회
# 전체키
dicKeys = dicContainer.keys
print(f'dicKeys: {dicKeys}') # ['이름', '나이', '주소', '취미', '연락처']

for key in dicKeys():
    print(f'{key}: {dicContainer[key]}')

#전체 벨류값
dicValues = dicContainer.values()
print(f'dicValues: {dicValues}')

#키와 벨류를 한 번에 조회
for key, value in dicContainer.items():
    print(f'{key}: {value}')
    print(type(dicContainer.items()))

# 중간고사 성적 관리 프로그램 만들기
'''
아래 시나리오를 기반으로 딕셔너리를 이용해서 중간고사 성적 관리 프로그램을 만들어봅시다.
 -1 : 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+, 해킹은 F, 시스템은 C+)을 저장하는 
      딕셔너리를 만든다.
 -2 : 'Java'와 '시스템' 과목의 성적을 조회한다.
 -3 : 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
 -4 : 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
 -5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.
'''



scores = {
    "c/c++": 'A', 
    # "Java": "B+",
    'Java': 'B+', 
    "모바일": "C", 
    '보안': 'A+', 
    '해킹': 'F',
    '시스템': 'C+'
}

#2
# print(f"Java: {scores['Java']}")
print(f'Java: {scores['Java']}') 
print(f"시스템:{scores['시스템']}")

scores['파이썬'] = 'A'
scores['OS'] = 'A+'
print(f'scores: {scores}')

#4
scores['Java'] = 'F'
scores['시스템'] = 'A'
print(f'scores: {scores}')

# -5
creditScores = {
    'A+': 4.5,
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'F': 0.0,
}

totalScore = 0
averageScore = 0

for key in scores.keys():
    totalScore += creditScores[scores[key]]
    print(f'{key}:\t{scores[key]}')     # A+ > 4.5, A > 4.0, B+ > 3.5 ... 

print(f'totalScore: {totalScore}')      # 23.0
averageScore = totalScore / len(scores)
print(f'averageScore: {averageScore}')  # 2.875

'''
C/C++:  A       4.0
Java:   F       0.0
모바일: C        2.0
보안:   A+       4.5
해킹:   F        0.0
시스템: A        4.0
파이썬: A        4.0
OS:     A+      4.5

A+      : 4.5
A       : 4.0
B+      : 3.5
B       : 3.0
C+      : 2.5
C       : 2.0
F       : 0.0
'''


