print('회원정보를 입력하세요')

UserName= input('이름: ')
UserMail= input('메일: ')
UserID = input('아이디: ')
UserPw = input('비밀번호: ')

# print('---------------------')
# print('To.' + UserMail)
# print('▶아이디 및 비밀번호 확인')
# print(UserName + '고객님 안녕하세요')
# print(UserName + '고객님의 아이디는 아래와 같습니다.')
# print('아이디: UserID')
# print('비밀번호: UserPw')
# print('감사합니다.')
# print('Naver 담당자')
# print('---------------------' )

# userMail = 'mayphyton112@gmail.com'
# print('To mayphyton112@gmail.com')
# print('To. ' + userMail)

# print('이름:', '홍길동', "나이:", 20) #이름: 홍길동 나이: 20

# print('Hello', end='-') #2026-05-06
# print('world')

firstNum = int(input('첫번째 정수 입력:'))
secondNum = int(input('두번째 정수 입력:'))

sum = firstNum +secondNum
average = sum/2

print(f'합: {sum}')
print(f'평균: {average}')

print(f'합: {firstNum +secondNum}')
print(f'평균: {firstNum +secondNum/2}')
      
# quiz) var1, var2 변수에는 정수 10과 20이 각각 저장되어있다.
# var1과 var2의 데이터를 서로 바꾸는 프로그램을 만들고 화면에 var1과 var2의 데이터를 출력하시오.

var1 = 10
var2 = 20

print(f'var1: {var1}, var2: {var2}')

temp = var1
var1 = var2
var2 = temp
print(f'var1: {var1}, var2: {var2}')