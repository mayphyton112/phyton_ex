# 논리 연산자
# 논리 연산자는 피연산자의 논리 자료형(True/False)을 이용하는 연산자로 and, or, not이 있다.

# and 연산자
# and는 '그리고' 라는 뜻을 가진다. and는 &도 되며 이는 엔퍼센트?라고 한다.
# 피연산자가 모두 True인 경우에만 결과가 True다.
# 피연산자가 하나라도 False인 경우 결과는 False로 뜬다.
# var1 = True
# var2 = True
# print(var1 and var2) #and를 기준으로 피연산자인 var1,2가 모두 True인 경우에만 True
 
# var1 = True
# var2 = False
# print(var1 and var2) #False

# var1 = False
# var2 = False
# print(var1 and var2) #True

# # or 연산자
# # or은 '또는'이라는 뜻으로, 피연산자 중 하나라도 True라면 값은 True가 된다.
# # or = |
# var1 = True
# var2 = True
# print(var1 or var2) # True

# var1 = True
# var2 = False
# print(var1 or var2) # True

# var1 = False
# var2 = False
# print(var1 or var2) # False

# # not(부정) 연산자
# # not은 '부정'이라는 뜻을 가진다. 피연산자의 현재 상태를 부정한다.
# # 피연산자가 True이면 결과로 False를, False면 True를 출력한다.

# var1 = True
# print(not var1) # False

# var1 = False
# print(not var1) # True

# num1 = 10; num2 =20; num3 =30
# result = (num1 <num3) and (num2 < num3)
# print(f'result: {result}')

# result = (num1 > num3) and (num2 < num3) #False
# print(f'result: {result}')

# result = (num1 > num3) and (num2 > num3) #False
# print(f'result: {result}')

# num1 = 10; num2 =20; num3 =30
# result = (num1 <num3) and (num2 < num3) and (num3 > num1)
# print(f'result: {result}')

# print(5 or 6) #5
# print(5 | 6)  #7

# # and, or 연산시 주의 사항
# # and 연산자는 모든 피연산자가 True인 경우에만 결과를 True로 출력한다.
# # 그렇기에 첫 번째 연산의 결과가 False이면 더 이상 연산을 실행하지 않는다.

# num1 = 10; num2 = 20
# result = (num1 < 15) and (num2 > 15) # num1 < 15-> num2 > 15 순서

# # num1 = 17; num2 = 20
# # result = (num1 < 15) and (num2 > 15) -> 첫 과정이 False라 바로 False가 출력

# # or 연산자는 피연산자 중 하나라도 True가 있다면 결과값은 True다.
# # 그렇기 때문에 True 피연산자를 만나게 되면 이후 피연산자의 연산은 무시하고 무조선 True를 출력한다.

# num1 = 10
# # print(f'num1: {num1}')
# # print(abc)

# # print((num1 > 5) or abc)

# # 어린이용 범퍼카 탑승 가능 판별하기
# # DW 놀이동산은 어린이용 범퍼카의 사용기준을 '신장이 120cm 이상이고 170cm 미만인 어린이'
# # 라고 규정하였습니다. 어린이용 범퍼카를 탑승할 수 있는지 여부를 알려주는 프로그램을 만들어봐라
# #(탑승 가능은 True, 탑승 불가능은 False를 출력한다.)

# height = int(input('어린이의 신장을 입력하세요'))
# height = (height >= 120) and (height < 170)
# print(f'result: {result}')

# # 조건식 == 삼항 연산자
# num1 = 10 # 이항 연산자 항이 둘이라 이항이라고 한다.
# num1 = 10 - 6 # 이항 연산자
# not True       # 단항 연산자

# targetscore = 90
# myscore = 95
# # myScore가 targerScore보다 크거나 같으면 합격, 그렇지 않으면 불합격
# #result = '합격' if myscore >= targetscore else '불합격' #삼항 연산자
# # if 와 else 사이에 있는 것이 조건문
# # true면 앞 내용이 담기고 False 면 뒷 내용이 담긴다.
# print(f'result-----{result}')

# 적자/흑자 판단하기
# DW 마트는 수입과 지출을 입력하면 흑자인지 적자인지 판별하는 프로그램을 도입하려고 한다.
# 마트 수익 결과를 알려주는 프로그램을 만들어라.

incoming = int(input('수입'))
outgoing = int(input('지출'))
result = '흑자' if incoming > outgoing else '적자'
print(f'result: {result}')

# 조명 장치 on/off 프로그램 만들기
currentlight = 50
targetlight = 60
result = 'Turn on' if currentlight < targetlight else 'Turn off'
print(f'result: {result}')

