# 비교 연산자
'''
a == b  a와 b는 같다. => True or False  #Boolean type
a != b  a와 b는 같다. => True or False
a > b  a와 b는 같다. => True or False
a >= b  a와 b는 같다. => True or False
a < b  a와 b는 같다. => True or False
a <= b  a와 b는 같다. => True or False
'''

# num1 = 10; num2 = 20

# print(num1 == num2) #False
# print(num1 != num2) #True
# print(num1 > num2) #False
# print(num1 >= num2) #False
# print(num1 < num2) #True
# print(num1 <= num2) #True

# #범퍼카 탑승 가능 판별
# '''
# DW 놀이동산에서 범퍼카는 신장이 120cm 이상인 어린이만 탑승할 수 있습니다.
# 사용자가 신장을 입력하면 범퍼카를 탑승할 수 있는지 여부를 출력하는 프로그램을 만들어라.
# True : 탑승가능, False : 탑승 불가능
# '''
# height = int(input('어린의 신장을 입력하세요'))
# print(height >= 120)

# # 문자 vs 문자 비교 => 아스키 코드
# print('a' == 'b')  #False 97 == 98
# print('a' < 'b')  #True   97 < 98
# print('a' > 'b')  #False 97 > 98

# # 문자열 비교
# str1 = 'hello'
# str2 = 'hello'

# print(str1 == str2) #True
# print(str1 != str2) #False
# print(str1 > str2) #False
# print(str1 > str2) #False

num4 = 'p'
num5 = 'y'
print (num4 > num5)

str1 = 'Hello'
str2 = 'phthon'
print(f'str1 != str2 : {str1 != str2}')
