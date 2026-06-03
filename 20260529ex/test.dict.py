weapons = {
    '창': 'Spear',
    '활': 'Bow',
    '검': 'Sword'
}

'''
'창'의 값을 출력하기
'도끼': 'Axe' 추가하기
'검'을 'Long Sword'로 수정하기
'활' 삭제하기
반복문으로 모든 키와 값 출력하기
'''

# weapons['창']
# print(weapons['창'])
# weapons['도끼'] = 'axe'
# print(f'weapons: {weapons}')
# weapons['검'] = 'long Sword'
# print(f'weapons: {weapons}')
# del weapons['활']
# print(f'weapons: {weapons}')

# while True:
#     print (weapons.items())
#     break

'''
아래 딕셔너리로 로그인 기능을 만들어 보세요.
사용자에게 ID와 PW를 입력받아서
로그인 성공
로그인 실패가 뜨게 만들어라
'''

accounts = {
    'kim': '1234',
    'lee': '5678',
    'park': '9999'
}

# uid = input('ID 입력: ')
# upw = input('PW 입력: ')

# if uid in accounts:
#     print(f'존재하는 아이디입니다.')
    
#     if accounts[uid] == upw:
#         print('로그인 성공')
#     else:
#         print('로그인 실패')

#딕셔너리의 값은 기본적으로  키 => 값 방향으로만 빠르게 찾을 수 있다.
#[]안에 넣을 수 있는 것은 keys()에 있는 값들 뿐이다.

#가장 점수 높은 사람 찾기
students = {
    '김철수': 85,
    '이영희': 95,
    '박민수': 88
}

print (students.items())
print (max(students.items()))



#재고관리
inventory = {
    '사과': 10,
    '바나나': 5,
    '딸기': 20
}

# products = input(f'물품 이름: ')
# if products in inventory:
#     print('존재하는 아이템입니다.')
#     print (inventory[products])
# else: print('존재하지 않습니다.')

#단어장
words = {
    'apple': '사과',
    'banana': '바나나',
    'orange': '오렌지'
}

# wordnotes = input(f'단어 입력: ')
# if wordnotes in words:
#     print('존재하는 단어입니다.')
#     print(f'{wordnotes} : {words[wordnotes]}')
#     # 특정 단어 하나를 item() 방식으로 찾을 때에는 print(f'{변수} : {dict이름[변수]}')가 된다.
# else: print('존재하지 않는 단어입니다.')


#예제 2. 평균 점수 구하기

scores = {
    '수학' : 90,
    '국어' : 86,
    '영어' : 70
}

print(scores.values())
sum(scores.values())
len(scores.values())

# aver = sum(scores.values()) / len(scores.values())
aver = sum(scores.values()) / len(scores)
#딕셔너리의 길이는 키의 개수이고 키의 개수와 값은 항상 같다.
print(aver)

#예제 4. 회원 전체 조회

#예제 5. ID 찾기