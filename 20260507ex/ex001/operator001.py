# 나눗셈 연산자(/)
# print(10/2)   # 5.0
# print(3.14/0.5) #it에서는 .5로 쓰는 경우가 많다.

# num1 = 100
# num2 = 10
# print(f'num1/num2 = {num1/num2}')

# # 신체질량지수(bmi)구하기
# # 몸무게와 신장을 입력하면 bmi를 계산해주는
# # 프로그램을 만들어봅시다. bmi = 몸무게/신장의 제곱

# weight = float(input('몸무게(kg): '))
# height = float(input('신장(m):'))
# bmi = weight / (height * height)
# print(f'BMI: {bmi}')

# print(f'BMI: {bmi:.2f}')
      
# # 숫자 0을 어떤 수로 나누어도 결과는 항상 0이다.
# print(0/123)  #0

# # 어떤 숫자를  0으로 나눌 수 없다. 에러
# # print(10/0)


# #나머지, 몫, 거듭제곱
# #나머지(%)
# print(10 % 2) #0
# print(10 % 3) #1

# #홀짝 게임하기
# #주먹쥔 손을 상대방에게 내밀며 손 안에 동전개수가 홀수인지 짝수인지 맞추는 게임
# #손 안에 동전 개수를 입력하면 짝수는 0, 홀수는 1을 출력하는 프로그램을 만들어라
# inputData = int(input('손 안에 동전 개수를 입력하세요.'))
# result = inputData % 2
# print(result)

# # 몫(//)
# print(10 // 3) #3
# print(6 // 2) #3

# # 빵을 나누어 줄 수있는 학생수 구하기
# # 길동이는 97개의 빵을 3개씩 같은 반의 친구들에게 나누어주려고한다.
# # 최대 몇 명에게 나누어 줄 수 있는지 구하고, 남는 빵의 개수를 구하라.
# bread = 97
# breadCnt = 3
# maxFriendCnt = bread // breadCnt
# print(f'빵을 나누어 줄 수 있는 학생 수: {maxFriendCnt}')

# restBreadCnt = bread % breadCnt
# print(f'남는 빵 개수: {restBreadCnt}')

# 거듭제곱(**)
print(2**2)
print(2**3)
print(2**10)

#전염병 예상 감염자 수 구하기 
# 보건 당국은 전염병의 감염 확산 추세를 파악한 결과,
# 하루에 한 사람이 한 명씩 감염시키는 것으로 나타났습니다.
# 확진자 한 사람이 나올 경우 30일 이후에 몇 명의 감염자가 나오는지 계산하라.
man = 2
date = 30
total = man ** date
print(f'{date}일 이후 예상 감염자 수: {total}')


