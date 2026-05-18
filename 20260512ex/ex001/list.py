#컨테이너 데이터 파일 -외국
#컨테이너 자료형 > 자료형
#container data type
#=>파이썬에서는 list, tuple, dictionary를 사용한다.

'''
프로그램을 개발하다보면 변수를 이용해 데이터를 하나씩 저장하기보단 여러 데이터 코드를 묶어 처리하는것이 효율적일 때가 있다.

'''

# # 리스트(list)
# fruits = ['사과', '포도', '수박', '참외', '배', '복숭아', '바나나', '자두']
# print(f'fruits: {fruits}')
# print(f'type of fruits: {type(fruits)}')

# #리스트와 데이터
# '''
# 리스트에 포함되는 데잍너는 어떤 자료형이든 상관없다
# 예를 들어 정수, 실수, 문자(열)이 하나의 리스트로 묶일 수도 있다.
# '''
# complexlist = [10, 3.14, 'a', 'hello']
# #이렇게 하나의 리스트에 다양한 데이터 타입의 데이터를 넣을 수 있는 언어는
# #python과  javascript뿐으로 java는 안된다.
# print(f'complexList: {complexlist}')
# print(f'type of complexList: {type(complexlist)}')

# # []만 있어도 리스트이다. Length 1
# member = list
# print(f'member : {member}')
# print(f'type of member : {type(member)}')

# #ex) 다음 회의 참석자 명단을 리스트로 선언하고 attendlist 변수에 담아보자
# attendList = ['이순철', '김병현', '김민우' , '김민태' ]

# #리스트의 아이템 조회
# # 특정 아이템 조회
# #리스트가 메모리에 저장될 때 아이템마다 다른값이 부여되는데 이것이 index이다.
# #0부터 시작한다.

# #          0        1      2      3        4     5       6       7
# fruits = ['사과', '포도', '수박', '참외', '배', '복숭아', '바나나', '자두']
# print(fruits[1]) #특정하길 원하는 데이터의 인덱스 번호를 적는다.
# print(f'fruits[1]: {fruits[1]}')
# print(f'fruits[0]: {fruits[0]}')
# print(f'fruits[7]: {fruits[7]}')
# # print(f'fruits[7]: {fruits[8]}') -존재하지 않는 범위의 값
# #=>index 에러가 뜬다. (IndexError: list index out of range)

# #list 길이(아이템 개수) 조회
# '''
# 리스트 길이란 리스트의 아이켐 개수를 뜻하는 것으로 len() 함수를 사용하면 알 수 있다
# 다음은 len() 함수를 이용해 리스트의 길이를 확인하는 코드이다.
# '''

# # numbers = [1,2,3,4,5]
# # print(f'nunbers: {numbers}')
# # print(f'nunbers length: {len(numbers)}')

# # numbers = [1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5]
# # # 첫 번째 데이터 조회:
# # print(f'첫번째 데이터: {numbers[0]}')

# # # 마지막 데이터 조회:
# # print(f'마지막 데이터: {numbers[len(numbers)-1]}')
# # # 마지막 데이터는 전체 길이에서 -1을 하여 조회한다.

# # #len() 함수는 문자열의 길이를 조회하는데에도 사용된다.
# # str = "hellllllllllll0"
# # print(len(str))

# #입력한 글자 수 확인하기
# '''
# 사용자로부터 메시지를 입력 받고, 입력 받은 문자열의 길이를 출력하는 프로그램을 만들어라
# '''
# # msg = input('메시지:')
# # msgLen = len(msg)
# # print(f'msgLen: {msgLen}')

# # #리스트 전체 데이터 조회
# # balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
# # print(f'balls[0]')
# # print(f'balls[1]')
# # print(f'balls[2]')
# # print(f'balls[3]')
# # print(f'balls[4]')

#리스트 또한 literal data에 해당한다.
# # for 변수 in literable data
# #for문
# # idx = 0
# # for item in balls: # item = '야구공', item = '축구공', item = '탁구공' ...
# #     print(f'item: {item}, index: {idx}')
# #     idx += 1

# # for item in enumerate(balls):  # item = '야구공', idx = 0, item = '축구공' idx = 1...
# #     print(f'item: {item}, index: {idx}')

# # # while문
# # i = 0
# # while i < len(balls):
# #     print(f'balls: [i], index: {i}')
# #     i += 1

# # #for 과 while 중에서는 for이 더 좋다.

# #다음 리스트에서 마지막  인덱스 값을 출력하는 프로그램을 만드시오
# #            0             1            2       3         4
# sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
# lenVar = len(sports)-1  #6 - 1 => 5
# print(sports[lenVar])     #'aaaaaa'
# #마지막 index는 전체에서 -1이다. 즉 전체가 100이면 마지막 인덱스는 99인셈

# #다음 리스트에서 'phython' 문자열의 인덱스 값을 출력하는 프로그램을 만들어라
# languages=['c/c++', 'c#', 'python', 'java']
# for idx, str in enumerate(languages):
#     if str == 'python':
#         print(f'python idx: {idx}')


# targetIndex = languages.index("python") #함수의 일종
# print(f'targetIdx: {targetIndex}')

# # 아이템 기존 리스트에 삽입
# # 리스트 마지막에 삽입
# sports = ['football', 'baseball', 'volleyball' ]
# print(f'sports: {sports}')  

# sports.append('basketball')
# print(f'sports: {sports}')     #['football', 'baseball', 'volleyball', 'basketball']
# print(f'sports length: {len(sports)}')

'''
취미들을 저장할 리스트를 정의하고 사용자가 입력한 취미가 추가되는 프로그램을 만들어보자
그리고 취미의 개수를 출력하자!
'''
# hobbies = []
# hobby = input('취미 입력: ')
# hobbies.append(hobby)
# print(f'hobbies: {hobbies}')

# hobbies = []
# flag = True      #1

# while flag:
#     hobby = input('취미 입력: ')
#     hobbies.append(hobby)
#     print(f'hobbies: {hobbies}')
#     selectedMemuNumber=int(input('1.취미 추가  2. 종료'))
#     if selectedMemuNumber == 2:
#        flag = False
              
#               #2
# while True:
#     hobby = input('취미 입력: ')
#     hobbies.append(hobby)
#     print(f'hobbies: {hobbies}')
#     selectedMemuNumber=int(input('1.취미 추가  2. 종료'))
#     if selectedMemuNumber == 2:
#         print(f'총 개수: {len(hobbies)}')
#         break


# #특정 위치에 아이템 삽입하기
# #리스트의 원하는 위치에 아이템을 삽입할 때는 insert() 함수를 이용한다
# countries = ['korea', 'china', 'japan']  #['korea', 'usa', 'china', 'japan']
# countries.insert(1, 'usa') #넣을 아이템과 그 아이템의 인덱스 값
# print(f'contries: {countries}') #countries: #['korea', 'usa', 'china', 'japan']
# #데이터를 넣고 원래 해당위치에 있던 데이터는 한 칸씩 뒤로 밀리게 된다.

# 누락된 숫자 추가
# numbers == [1, 2, 3, 4, 5, 7, 8, 9]
# numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# numbers.insert(5, 6)
# print(f'numbers: {numbers}')
# numbers.append(10)
# print(f'numbers: {numbers}')
# '''
# 취미 입력: 축구
# hobbies: [축구]
# '''

# #리스트 연결하기
# #리스트에 또 다른 리스트를 연결할 때는 extend()함수를 사용
# list1 = [1, 2, 3]
# print(f'list1: {list1}') #[1,2,3]

# list2 = [10, 20, 30]
# print(f'list2: {list2}')

# list1.extend(list2) #list 1의 데이터를 복사해 list2 뒤에 붙인다.
# print(f'list1: {list1}')
# print(f'list2: {list2}')

# ----------------------------------------------------------

# 덧셈연산자도 가능
# list3 = list1 + list2
# print(f'list1: {list1}')
# print(f'list2: {list2}')
# # print(f'list3: {list3}')

#리스트 아이템 삭제하기
#리스트 마지막 아이템 삭제하기
sports = ['baseball', 'basketball', 'tennis', 'golf']
print(f'sports: {sports}')
sports.pop(1)         #basktetball이 지워진다.
print(f'sports: {sports}')

removedItem = sports.pop() #pop은 가장 마지막 데이터를 삭제하며 삭제된 아이템은 변수에 보관할 수 있다. 
print(f'sports: sports')

#pop()대신 del 키워드를 이용해 아이템을 삭제할 수 있다.
sports = ['baseball', 'basketball', 'tennis', 'golf']
del sports[2]               #삭제된 아이템은 다시 찾아서 쓸 수 없다.
print(f'sports: {sports}')

#sports 리스트에서 'volleyball'을 삭제하는 프로그램을 만들자
sports = ['baseball', 'basketball', 'tennis', 'golf']
volleyballIdx = sports.index('volleyball')
sports.pop(volleyballIdx)
print(f'sports: {sports}')