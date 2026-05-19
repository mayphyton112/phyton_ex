#지역변수 vs 전역변수
#지역변수는 함수 내부에서 선언된 변수로 함수 내부에서만 사용 가능
#전역변수는 함수 외부에서 선언된 변수로 함수 내/외부에서 사용 가능

#함수 내부에서 어떤 변수를 쓸떄 지역변수를 먼저 참조한다.

# num = 10

# def fun():
#     global num
#     num = 20              # 지역변수
#     num += 1
#     # num = num+1     #데이터 수정 num(전역변수) =10 + 1

#     print(f'num: {num}')  # 10, 전역변수 num > 20, 지역변수 num

# print(f'num: {num}')  # 10, 전역뱐수 num

# fun()

'''
global 키워드는 함수 내에서 전역변수의 값을 수정하고자 할때 반드시 명시한다.
'''

'''
웹사이트의 누적방문 횟수 프로그램
웹사이트 방문 여부를 입력받아 웹사이트의 누적 방문 횟수를 출력하자
'''

# flag = True
# totalvisitor = 0
# totalvisitor += 1
# def countvistor():
#     totalvisitor += 1

# while flag:
#     selectedMenuNum = int(input('1.웹사이트 방문  2. 종료'))

#     if selectedMenuNum == 1:
#         countvistor()
#         print(f'누적 방문 횟수: {totalvisitor}')
#     else:
#         flag = False
#         print('Good bye')
#에러가 생긴다. anboundlocal error

# flag = True
# totalvisitor = 0

# def countvistor():
#     global totalvisitor
#     totalvisitor += 1

# while flag:
#     selectedMenuNum = int(input('1.웹사이트 방문  2. 종료'))

#     if selectedMenuNum == 1:
#         countvistor()
#         print(f'누적 방문 횟수: {totalvisitor}')
#     else:
#         flag = False
#         print('Good bye')

# 매개변수(매우 중요)
# 매개: 둘 사이에서 양편의 '관계를 맺어' 준다.
# 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출한다.
# 이때 함수를 정의하는쪽을 함수 정의부(선언부), 함수를 호출하는 쪽을 호출부라고 한다.
# 함수를 호출할때 데이터를 넘겨줄 수 있는데 이 데이터를 '인수'라고한다
# 함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장하고 매개변수는 지역변수의 일종이다.

# def greet():
#     print(f'홍길동님 안녕하세요')

# greet()

# def greet(name, age):
#     # name = '홍길동' or '박찬호', or '박세리)
#     print(f'{name} 안녕하세요. 나이는 {age}입니다.')

# greet('홍길동', 25)
# greet('박찬호', 20)
# greet('박세리', 30)

#매개변수에는 아무거나 넣을 수 있다.

#매개변수가 두 개 이상인 경우 호출부에서 전달하는 인수의 개수와 순서에 맞춰 선언한다.
#즉 순차적으로 전달하는 것, 그리고 전달했어도 안 써도 상관은 없다.
#선언부에서 2개를 만들었는데 호출부에서 1개만 만들면 에러가 뜬다. -postional argument
#선언부와 호출부의 쌍을 맞춰야함

#호출부에서 인수를 전달하는 것을 외부에서 주입한다고 해서 인젝션이라고 한다.
def forecastWeather(temp, humi, rain):
    print('날씨 예보입니다.')
    print(f'(최고 온도: {temp}도)')
    print(f'(평균 습도: {humi}%)')
    print(f'(비올 확률: {rain}%)')
   
#forecastweather()

# printScoresForStudent(10, 20, 100)
# score1 = 10, score2 = 20, score = 100
# def printScoresForStudent(score1, score2, score3):
#     totalScore = score1 + score2 + score3
#     averageScore = totalScore / 3
#     print(f'총합: {totalScore}')
#     print(f'평균: {averageScore}')

# def printScoresForStudent(subject, *scores): # *(가변인자) = all              # 리스트(list)-> 튜플(tuple)
    
#     print(f'scores type: {type(scores)}')   #tuple
#     print(f'scores length: {len(scores)}')  # 4

#     totalScore = 0 #초기화
#     for score in scores:
#         totalScore += score

#     print(f'{subject} 과목총합: {totalScore}')
#     averageScore = totalScore/len(score)
#     print(f'평균: {totalScore /len(scores)}')


#     # totalScore = score1 + score2 + score3
#     # averageScore = totalScore / 3
#     # print(f'총합: {totalScore}')
#     # print(f'평균: {averageScore}')

# # 90, 80, 70
# printScoresForStudent(90, 80, 70)

# # score = int(input('학생 점수 입력:'))
# # printScoresForStudent(score)        #되긴한다.

# printScoresForStudent('국어', 90, 80, 70)


'''
선생님이 몇 명일지 모르는 학생의 점수를 입력한다.
이때 학생 점수의 총합과 평균을 구하는 함수를 만들고 이를 이용하는 프로그램을 만들어보자
'''
# flag = True
# studentScores = []

# def printScoresForStudent(scores):  #scores = [,,,,,,,]
#     if len(scores) == 0:
#       print('학생수가 0명이라 총점과 평균을 구할 수 없습니다.')
   
#     else:
#         flag = False

#     for score in scores:
#         totalScore += score
    
#     average = totalScore / len(scores)
#     print(f'총점: {{totalScore}}')
#     print(f'평점: {average}')
    

# while flag:
#     selectedMenuNum = input(f'1. 학생 점수 입력 2.종료')
#     if selectedMenuNum == 1:
#         score = int(input('학생 점수 입력: '))
#         studentScores.append(score)
#     else:
#         flag = False
#         break

# printScoresForStudent(studentScores)


#SMS 와  MMS 구별하기

'''
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다. 그런데 100자를 
넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 단문과 장문을 구별해서 돈을 부
과하는 프로그램을 만들어봅시다. 
'''

# def sendUserMessage(str):
#    strlength = len(str)
#    print(f'사용자가 입력한 문자 길이: {strlength}')

#    if strlength <= 100:
#        print(f'SMS 발송완료')
#        print('50원 부과')
#    else:
#        print(f'MMS 발송 완료')
#        print(f'100원 부과')


# inputData= input('문자입력:')
# sendUserMessage(inputData)


# def sendUserMessage(message):  #refactoring
   
#    strlength = len(message)
   
#    if strlength <= 100:
#        messageType = 'SMS'
#        price = 50

#    else:
#        messageType = 'MMS'
#        price = 100
    
#    print(f'사용자가 입력한 문자 길이: {strlength}')
#    print(f'{messageType}발송 완료')
#    print(f'{price}원 부과')

# inputData= input('문자입력:')

# sendUserMessage(inputData)

#딕셔너리 방식도 가능하다.

# def sendUserMessage(message):
#     length = len(message)

#     info= {
#         True: ('SMS, 50'),
#         False: ('MMS', 100)
#     }

#     messageType, price = info[length <= 100]

#     print(f'{messageType} 발송')
#     print(f'{price}원 부과')

# 인수와 매개변수의 순서가 일치하지 않을 경우
# def printMemberInfo(name, email, major, grade): #변수는 명사 함수는 동사+목적어로 작성하는것이 원칙
#     print(f'name\t: {name}')
#     print(f'email\t: {email}')
#     print(f'major\t: {major}')
#     print(f'grade\t: {grade}')
#     print('- * 10')

# printMemberInfo('Hong Gildong', "gildong@gmail,com", 'art', 1)
# printMemberInfo("gildong@gmail,com",'Hong Gildong', 'art', 1) #값이 바뀐다.
# printMemberInfo(email = "gildong@gmail,com",name ='Hong Gildong', major = 'art', grade = 1)
#대상을 지정해 오류를 없앤다. 주로 세로로 나열하는 방식을 많이 사용한다.
#원래 위 방식은 없다. 함수의 원래 룰을 따르는것이 좋다.

# def printMemberInfo(info): #변수는 명사 함수는 동사+목적어로 작성하는것이 원칙
#     print(f'name: {info['name']}')
#     print(f'email: {info['email']}')
#     print(f'major: {['major']}')
#     print(f'grade: {['grade']}')
#     print('- '* 10)



# printMemberInfo({
#         'name': 'Hong gildong',
#         'email': 'gildong@gmail.com',   #anymous dict
#         'major':  'art',
#         'grade':  1
#     })
    
# #매개변수의 기본값 설정
# #직업 급여 지급 프로그램을 만들어보자
# def setSalary(name, pay=200):
#     print(f'{name}의 급여 {pay}원 지급')

# setSalary('박찬호', 400)
# setSalary('박세리', 600)
# setSalary('박용택')


# [].sort() # reverse = False
# []. sort(reverse=True)

#데이터 반환(return)
#데이터 반환이란, 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환할 수 있습니다.
#이때 사용하는 키워드가 return이다.
#덧셈 연산 함수를 만들어 결과를 출력하는 프로그램을 만들어보자

# def printResult(value):
#     print(f'result: {value}')

# def adfunction(n1, n2):
#     sum = n1 + n2          #30
#     # print(f'결괏값: {sum}')
#     printResult(sum)
#     return sum  #호출부로 다시 값을 돌린다.

# result = adfunction(10, 20)
# print(f'result: {result}')
#adfunction은 계산과 출력 두 가지의 기능을 하고있다.

# 호출, 계산, 재할당
# 선언부에서 호출부로 다시 데이터를 돌리는 키워드가 return
# 필요하면 반환된 값을 받고 필요없으면 받지 않으면 된다.

# def printResult(value):
#     print(f'result: {value}')

# def adfunction(n1, n2):
#     sum = n1 + n2          #30
#     # print(f'결괏값: {sum}')
#     printResult(sum)
#     return sum  #호출부로 다시 값을 돌린다. 방송과 같은 느낌이다. 

# adfunction(10, 20)

# def fun1():
#     print('1' *  4)
#     return              #함수를 종결시키는 의미도 있다.
#     print('2' *  4)
#     print('3' *  4)
# fun1()

#기능이 많을떄는 return을 쓰는 경우도 있다. 

# DEV_MODE = True # 테스트하는데 쓴다.

# def fun1():
#     print('2' *  4)
#     if DEV_MODE ==True:            #함수를 종결시키는 의미도 있다.
#         print('1' *  4)
#         return
#     print('3' *  4)
# fun1()


#별탑 만들기
# def increaseStart(limitStarCount):
#     print('*')
#     print('*'  * 2)
#     print('*' *  3)
#     print('*' *  4)
#     print('*' *  5)
#     print('*' *  6)
#     print('*' *  7)
#     for n in range(1,8):
#         print('*' * n)
#         if n == limitStarCount:
#             break

# increaseStart(5)

'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입 2.로그인 3.특정 회원정보 출력 4. 모든 회원정보 출력 99. 종료
사용자가 
'1.회원가입'을 선택하면 회원ID, 회원PW, 회원Emaill, 회원Phone 정보를 입력받아 회원가입을 진행한다.
'2.로그인'을 선택하면 회원ID, 회원PW를 입력받아  로그인 '성공' 또는 '실패'를  출력한다.
'3. 특정 회원 정보 출력'를 선택하면 회원ID, 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
'4. 모든 회원 정보 출력'를 선택하면 가입되어 있는  모든 회원 정보를 출력한다.
'99. 종료'를 선택하면 프로그램을 종료시킨다.

심심하면 > 특정 회원의 회원ID, 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해보자
'''
flag = True
while flag:
   userData = int(input(f'1.회원가입 2.로그인 3.특정 회원정보 출력 4. 모든 회원정보 출력 99. 종료'))
   if userData == 1: 
    input('[id, pw, email, phone]을 입력하세요: ')
    print('회원가입이 완료되었습니다.')
   
#    members = [
#       {'id': 'kim48', 'pw': 'pass2'},
#       {'id': 'lee578', 'pw': 'pass3'},
#       {'id': 'hong123', 'pw': 'pass4'},
#    ]

   if userData == 2:
    user_id = input('id 입력:')
    user_pw = input('pw 입력:')
   
    login_success = False
    for member in members:
       if member['id'] ==user_id and member['pw'] ==user_pw:
          login_success = True
          break

    if login_success:
       print('로그인 성공')
    else:
       print('로그인 실패')
   
   if userData == 3: 
       
    members =[ 
      {'이름': '이성규',
       '나이':  25,
       '성별': 'M',
       '연락처': '010-1234-5638',
       'id': 'kim48',
       'pw': 'pass2'
       },
       
       {'이름': '김성근',
       '나이':  30,
       '성별': 'M',
       '연락처': '010-1278-8903',
       'id': 'lee578',
       'pw': 'pass3'
       },
       
       {'이름': '이성태',
       '나이':  28,
       '성별': 'M',
       '연락처': '010-1278-7890',
       'id': 'hong123',
       'pw': 'pass4'
       },
   ]
   user_id = input('id 입력:')
   user_pw = input('pw 입력:')
   if user_id and user_pw: True
   print('members')

def opperateProgram():
        pass
flag +=1