# split
# 쪼갠다는 뜻으로 많이 쓰이는 기능중 하나이다.

names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
print(f'names: {names}')
print(f'names type: {type(names)}')

str = "박찬호 이승엽 박세리 박지성 이순철 선동열 손흥민 김연아" #기초 데이터 타입
#str.split(" ")=> 문자열을 공백이라는 구분자에 따라 자른다.
splitedStr = str.split(" - ")
print(f'splitedStr: {splitedStr}')
print(f'splitedStr type: {type(splitedStr)}')

splitedStr = tuple(splitedStr)
print(f'splitedStr: {splitedStr}')
print(f'splitedstr type: {type(splitedStr)}')

member = "이고은/20/대전 중구/010-1234-5678/goeun@gmail.com"
memberList = member. split("/")
print(f'memberList: {memberList}')
print(f'이름: {memberList[0]}')
print(f'연락처: {memberList[3]}')

#할당(대입) 연산
num = 10

#구조분해할당
# [1, 2] > a = 1, b = 2
#