# 반복문(for문 & while문)

#for문: ~하는 동안 ~을 하라=> 횟수에 의한 반복
'''
for 변수 in 범위:
    실행구문
'''

# 1~10까지의 정수를 출력(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for 변수 in range(시작값, 끝값, 단계) #범위를 지정하는 함수
# for 변수 in range(1, 10, 1) #범위를 지정하는 함수
#1~10까지의 변수를 하나씩 출력하라?
# for 변수 in range(1, 11, 1) #범위를 지정하는 함수 #보통 it에서는 끝나는 범위보다 1을 더한다.
# 1~n까지의 정수 range(1, (n+1), 1)
# for 변수 in range(1, 11, 1):
#     #실행구문
#     print('hello')

# for num in range(1, 11, 1):
#     print(f'{num} : hello')
#     print(f'hello')

# 0부터 10까지의 정수를 출력
# for num in range(0, 11, 1):
#     print(f'num: {num}')

# #range() 간략화
# # 1. range는 세 개의 값을 요구하는데 단계가 1인경우 단계를 생략 가능
# for num in range(0, 11):
#     print(f'num: {num}')

# # 2. 단계가 생략되고 시작이 0이면 시작도 생략가능
# for num in range(11):  # == range(0, 11, 1)
#     print(f'num: {num}')


# 2~8 사이의 짝수 출력하기
# for num in range(2, 10, 2):
#     print(f'num: {num}')

'''
num: 2
num: 4
num: 6
num: 8
'''
# for num in range(1, 16): # 짝수만 출력하라
#     if num < 10:
#         if num % 2 == 0:
#          print(f'num: {num}')

# for num in range(1, 16):
#    if num in range(2, 9, 2):
#        print(f'{num}은 2, 4, 6, 8 중 하나')
#    else:
#       print(f'{num}은 아님')   => 성립하지 않음

#사용자가 입력한 횟수만큼 '메일 발송!' 문자열 출력하기
# number = int(input(f'enter number: '))

# for user in range(number): #0 ~ 5: 0 1 2 3 4
#     print('메일발송!')

# 1~10 사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수!'출력

# for num in range(1, 11):
#     if num % 3 == 0:
#         print('3의 배수')
#     else:
#         print(num)


# 사용자가 원하는 구구단을 입력하면 해당 구구단을 출력하라
userdata = int(input(f"구구단 입력: "))
for user in range(1, 10):
    print(f"{userdata}*{user} ={userdata * user} ")

# userdata = int(input(f"구구단 입력:"))
# for user in range(1, 10):
#     resultStr = f"{userdata}*{user} ={userdata * user} "
#     print(resultStr)


# 1~10까지의 정수의 합 출력하기
# userInputIntegar = int(input('정수 입력'))
# sum = 0
# for num in range(1, userInputIntegar + 1):
#     sum += num
# print("1부터 10까지의 합:", sum)
# print(f" 1부터 {userInputIntegar}까지의 합: {sum}")

#for문을 이용해서 1~100까지의 정수 중에서
#3~ 7의 공배수와 최소공배수를 출력하시오
# commonMultiple = (3 * 7) * int(input('곱하려는 숫자를 입력하라:'))

# minimum = 3 * 7
# for num in range(1, 101):
#     print(minimum * num)

#range함수 정리
# range(1, 11, 1) = (1,2,3,4,5,6,7,8,9,10)

# 문자열을 이용한 for문(****)

'''
지금까지 이터러블에는 range()함수를 이용한 예를 살펴보았다.
그런데 이터러블에는 다음과 같은 문자열도 이용할 수 있다.
'''

# for ch in 'Hello': 
#     print(f'ch: {ch}')
# ch에 문자가 하나씩 할당된다.


#50보다 작은 7의 배수를 출력하는 프로그램을 만들어라
# for num in range(1, 51):
#     if num % 7 ==0:
#         print(f'num: {num}')
# # while문: ~ 하는동안 =>특정 조건에 의한 반복

# num = 1

# while num <= 10:
#     print(f'num: {num}') # 이상태면 무한 루프다
#     num += 1

# while num <= 10:
#     print(f'num: {num}') # 이상태면 무한 루프다
#     num += 2

# 1~30까지의 정수 중 홀수와 짝수를 구분하여 출력하라

# num = 1 # 시작값을 설정한다.
# while num < 31:   #조건(끝)
    
#     if num % 2 == 0:
#         print(f'{num}은 짝수')
#     else:
#         print(f'{num}은 홀수')
            
#     num += 1 # 단계

# 구구단 3단 출력하기 by while

# calculate = int(input(f'구구단 입력: '))
# num = 1
# while num < 10:
#     print(f'{calculate} * {num} = {calculate * num}')
#     num += 1

#구구단 전체(2단 3단...9단) 출력
# timetable = int(input(f'구구단: '))
# num = 1
# while num < 10:
#     print(f'{timetable} * {num} = {timetable * num}')
#     num += 1

# timetable = int(input(f'구구단: '))
# num = int(input(f'숫자:'))
# while num < 10:
#     print(f'{timetable} * {num} = {timetable * num}')
#     num += 1

# num1 = 2
# while num1 < 10:

#     num2 = 1
#     while num2 < 10:
#         print(f'{num1} * {num2} = {num1 * num2}')
#         num2 += 1   -루프


# num =1 
# while num < 10:
#     for number in range(1, 10):
#         print(f'{num} * {number} = {num * number}')
#     num += 1

# num1 = 2
# while num1 < 10:

#     num2 = 1
    
#     while num2 < 10:
#         print(f'{num1} * {num2} = {num1 * num2}')
#         num2 += 1

#     num1 += 1      

# num1 = 1
# while num1 < 10:

#     num2 = 2
#     str = ''
#     while num2 < 10:
#         str += f'{num2} * {num1} = {num2 * num1}\t'
#         num2 += 1
    
#     print(str)
#     num1 += 1

# while문과 if문을 이용해 0~100까지 정수 중 3과 8의 공배수와 최소공배수 구하기





num =  1      #반복문의 시작(초기값)
minNum = 0    #최소 공배수

while num < 100:
    if num % 3 == 0 and num % 8 == 0:
        print(f'3과 8의 공배수: {num} ')
        
        if minNum == 0:
            minNum = num
    num += 1

print(f'3과 8의 최소 공배수: {minNum}')

# 반복문 내 실행 제어(continue, break)
# continue:
# 반복문에 continue 키워드를 사용하면 이후 실행을 생략하고 다시 반복문의 처음으로 돌아간다.
#continue를 이용해 1부터 10까지의 정수 중 홀수만 출력하는 프로그램을 만들어라
# for num in range(1, 11):
#     if num % 2 ==0:
#         continue
#     print(f'num: {num}')

#break:
#반복문에서 break 키워드를 만나면 '실행을 중단하고 반복문을 빠져' 나온다

num = 1
sum = 0 

while num < 11:
    sum += num
    if sum >= 30:
        print(f'num: {num}')
        break
    num += 1

print(f'sum: {sum}')    
'''
for문에 else 키워드를 사용하는 경우, else이하의 구문은 for문의 반복업무를 모두 완료하고 난 후 실행된다.
 for 변수 in 반복가능객체:
     # 반복 실행
 else:
     # for문이 정상적으로 끝났을 때 실행  break가 중간에 없어야지 실행
     
 for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("이건 출력 안 됨")

# 출력:
# 0, 1, 2

while-else도 동일하게 동작한다.

i = 0
while i < 5:
    if i == 3:
        break
    i += 1
else:
    print("break 없이 끝남") #break로 끝났으니 출력이 되지 않는다.

'''


# 1부터 5까지 정수를 출력하고 반복문이 끝나면 완료 메시지를 출력하자
for num in range(1, 6):
    print(f'num: {num}')

print('완료')

#pass 키워드
for num in range(1,10):
    pass

'''
삼각형의 넓이 구하기
가로와 세로 길이의 변화에 따른 삼각형의 넓이를 구하는 프로그램을 만들어보자.
단, 가로 길이는 1부터 2의 배수로 증가하고
세로 길이는 1부터 3의 배수로 증가하며, 삼각형의 넓이가 150보다 크면 프로그램을 종료한다.
'''

count = 1
maxArea = 150

while True:
   result = ((count * 2) * (count * 3))/ 2
   if result > 150: break
   print(f'삼각형의 넓이는: {result}')
   count += 1 