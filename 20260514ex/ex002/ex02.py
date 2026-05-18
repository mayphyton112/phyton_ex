# flag = True

# members = {}

# while flag:
#     selectedNum= int(input('1.회원가입   2.프로그램 종료'))

#     if selectedNum == 1:
#         id = input('아이디: ')
#         pw = input('비밀번호:')
#         members[id] = pw
#     elif selectedNum == 2:
#         flag = False #break를 넣으려면 플래그 변수를 잡지않고 그냥 True를 쓰면 된다. 하지만 플래그변수를 쓰는것이 바람직하다.

#         for key in members.keys():
#             print(f'ID: {key}, PW: {members[key]}')


classes =  {'python':'5학점', 
            'C/C++':'5학점', 
            'HTML5':'3학점', 
            'Java':'5학점', 
            'Javascript':'3학점'
}

# classes['HTML5'] = '5학점'
# classes['Javascript'] = '5학점'
# print(f'clases: {classes}')

for key in classes:
    if classes[key] == '3학점':
        classes[key] = '5학점'
print (classes)


# members = {
#     '2019-052001': ['박찬호', 25, 'M', '010-1234-5678', '헬스, 수영', 0],
#     '2019-042004': ['박용택', 65, 'M', '010-9012-3456', '수영', 50],
#     '2019-052003': ['박세리', 70, 'W', '010-7890-1234', '아쿠아로빅', 50],
# }

# #전체 회원정보 출력
# for key in members:
#     print(f'회원번호: {key}, 회원정보: {members [key]}')

# #전체 회원 정보 출력을 하는데, 이떄 회원의 이름과 성별만 출력하자
# for key,value in members.items():
#     # print(f'회원번호: {key}, 회원정보): {members [key]}')
#     print(f'회원번호: {key}, 회원정보(이름, 성별):{value[0]}, {value[2]}')

    
members = {
    '2019-052001': {
     '이름':'박찬호',
    '나이' : 25,
    '성별':'M',
    '연락처':'010-1234-5678',
    '이용서비스' :['헬스', '수영'],
    '할인률': 0
    },

   '2019-042004': {
    '이름':'박용택',
    '나이': 65, 
    '성별':'M', 
    '연락처':'010-9012-3456', 
    '이용서비스':'수영',
   '할인률': 50
    },
    '2019-052003': {
        '이름': '박세리',
        '나이': 70,
        '성별': 'W',
        '연락처': '010-7890-1234',
        '이용서비스': ['아쿠아로빅'],
        '할인율': 50
    }
}

# 전체 회원 정보 출력
for key in members:
    print(f'회원번호: {key}, 회원정보: {members[key]}')

print('-' * 30)

#전체 회원 정보 출력을 하는데, 이떄 회원의 '이름', '성별', 그리고 '이용서비스' 만 출력하자
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이때 회원의 '이름', '성별', '이용서비스' 그리고 이용서비스개수 만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}, {value['이용서비스']}, {len(value['이용서비스'])}')

#다음 내용에 맞춰 냉장고에 보관하고 있는 야채의 재고 관리 프로그램을 만드시오
stocks = {
    '당근'  : 10,
    '건대추': 100,
    '대파'  : 20,
    '애호박': 3,
    '부추'  : 1  
}

stocks['당근'] -= 1
stocks['건대추'] -= 10
stocks['대파'] -= 1
stocks['애호박'] -= 1
stocks['부추'] -= 1

for key, value in stocks.items():
    print(f'{key}:\t{value}개')

#refactoringVersion
incoming = {
    '당근'  : 10,
    '건대추': 100,
    '대파'  : 20,
    '애호박': 3,
    '부추'  : 1  
}

outgoing = {
    '당근'  : 1,
    '건대추': 10,
    '대파'  : 1,
    '애호박': 1,
    '부추'  : 1  
}

stocks = {item: incoming[item]-outgoing[item] for item in incoming}
for key, value in stocks.items():
    print(f'{key}:\t{value}개')

