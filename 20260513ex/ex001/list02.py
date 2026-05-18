# 리스트 정렬
'''
sort()함수는 리스트의 아이템을 정렬하는 데 사용합니다.
reversre  옵션이 False면 오름차순(ASC), True면 내림차순(DESC)으로 정렬합니다.
'''
# numbers = [5, 1, 3, 4, 2, 6]
# print(f'numbers: {numbers}') # [5, 1, 3, 4, 2, 6]

# #오름차순(ASC)
# numbers.sort()       # == numbers.sort(reverse=False)
# print(f'numbers: {numbers}') # [1, 2, 3, 4, 5, 6]

# numbers. sort(reverse=True)
# print(f'numbers: {numbers}') # [6, 5, 4, 3, 2, 1]

# korean = ['다', '가', '마', '하', '카']
# print(f'korean: {korean}')

# korean.sort(reverse=True)
# print(f'korean: {korean}')

# scores = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
# print(f'scores: {scores}')
# scores.sort()
# print(f'scores: {scores}')
# scores.sort(reverse=True)
# print(f'scores: {scores}')

# #회의 참석자 정렬하기
# # 다음은 회의 참석자 명단입니다. 참석자 명단을 오름차순과 내림차순으로 정렬해봅시다.
# names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
# names.sort()
# names.sort(reverse=True)
# print(f'names: {names}')

# #리스트 순서 뒤집기
# #reverse()함수를 이용하면 리스트의 아이템을 역순으로 뒤집을 수 있다.
# vegetables = ['당근', '오이','양파','감자', '고구마']
# vegetables.reverse()
# print(f'vegetables: {vegetables}')

# #리스트 슬라이싱(slicing) -> 가장 중요
# # 슬라이싱이란, 리스트에서 필요한 부분의 아이템만을 뽑아내는 것을 말한다.
# animals = ['호랑이', '사자', '곰', '여우', '늑대']
# print(f'animals: {animals}')

# '''
#           |1----------------3|
# ['호랑이', '사자', '곰', '여우', '늑대'] # ['사자']
# '''
# print(f'animals[1 : 4]: {animals}')
# print(f'animals: {animals}')

# sliceAnimals = animals[1:4]
# print(f'sliceAnimals: {sliceAnimals}')
# #일부의 데이터를 잘라내려고 한다면 1부터 구하고자하는 값에 +1을 한다.
# #[n:m] : n 인덱스 로부터 (m-1)인덱스 까지의 아이템을 슬라이싱(추출)한다.

# animals = ['호랑이', '사자', '곰', '여우', '늑대']
# print(f'{animals[:3]}')
# #index 0부터 2(3-1)까지의 아이템 슬라이싱
# print(f'{animals[3:]}')
# #index 3부터 끝까지의 아이템 슬라이싱

# #뒤에서 2개의 아이템을 슬라이싱
# print(f'{animals[len(animals)-2:]}') 

# print(f'{animals[:-1]}')
# print(f'{animals[1:-1]}')
# #                              ['호랑이', '사자', '곰', '여우', '늑대']
# print(f'{animals[::2]}') #스텝  ['호랑이', '곰', '늑대']

# #다음 리스트를 보고 답하시오
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# #1. alphabet 리스트를 역순으로 출력하시오
# alphabet.reverse()
# print(f'alaphabet: {alphabet}')

# #2  다음 요구사항에 맞게 alphabet 리스트를 슬라이싱하시오
'''
 - 인덱스 2부터 5까지의 아이템을 출력하시오.
 - 인덱스 0부터 4까지의 아이템을 출력하시오.
 - 인덱스 3부터 7까지의 아이템을 출력하시오.
 - 인덱스 5부터 끝까지의 아이템을 출력하시오.
 - 인덱스 3부터 8까지의 아이템을 출력하시오.
'''
#            0    1    2    3    4    5    6    7    8    9
#           -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# #인덱스 2부터 5까지의 아이템을 출력하시오
# print(f'{alphabet[2:6]}')
# #인덱스 0부터 4까지의 아이템을 출력하시오
# print(f'{alphabet[:5]}')
# #인덱스 3부터 7까지의 아이템을 출력하시오
# print(f'{alphabet[3:8]}')
# #인덱스 5부터 끝까지의 아이템을 출력하시오
# print(f'{alphabet[5:]}')
# #인덱스 3부터 8까지의 아이템을 출력하시오
# print(f'{alphabet[3:9]}')

# #뒤에서 4개 아이템을 출력하시오
# print(f'{alphabet[len(alphabet)-4:]}')
# print(f'{alphabet[-4:]}')
# print(f'{alphabet[:-4]}')
# print(f'{alphabet[-7:-4]}')

# #+면 a,b,c,d 이고 -면 뒤로 돌아간다. 
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# print(f'alphabet: {alphabet}')
# del alphabet[1:4]
# print(f'del alphabet: {alphabet}')

#1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
[3, 7, 1, 9, 5]
nums = [3, 7, 1, 9, 5]
nums.sort()
print(f'nums: {nums}')
print(f'{nums[4]}')

# nums = [3, 7, 1, 9, 5]
# print(f'nums: {nums}')
# print(f'{nums[3]}')

'''
2. 사용자에게 숫자 입력받아서
1부터 입력한 숫자까지 합계 출력하기 ( 5 )
'''
intdata = int(input('숫자를 입력하세요: '))
total = 0
for num in range(1, intdata + 1):
    total += num
    print(f'num: {num}')

print(f'total: {total}')

'''
3. 리스트에 있는 숫자 중 짝수만 출력하기
[1,2,3,4,5,6]
'''
# nums = [1,2,3,4,5,6]
# print(f'{nums[1::2]}')

# nums = [1,2,3,4,5,6]
# for nums in nums:
#     if nums % 2 == 0:
#         print(f'nums: {nums}')

nums = [1,2,3,4,5,6]
double_nums = [data for data in nums if data % 2 == 0]
print(double_nums)
'''
4. 리스트 숫자를 오름차순 정렬하기
[5,1,7,3]
'''
numbers = [5,1,7,3]
numbers.sort()
print(f'numbers: {numbers}')

'''
5. 리스트 숫자를 내림차순 정렬하기
[5,1,7,3]
'''
numbers = [5,1,7,3]
numbers.sort(reverse=True)
print(f'numbers: {numbers}')

'''
6. 리스트 안 숫자의 평균 구하기 [10,20,30]
'''
nums = [10,20,30]
average = sum(nums) / len(nums)
print(f'average: {average}')

'''
7. 리스트에서 가장 작은 숫자 찾기
(min() 사용 금지)
'''
nums = [10,20,30]
nums.sort()
print(f'nums: {nums}')
print(f'{nums[0]}')

'''
8. 1부터 100까지 숫자 중
3의 배수와 5의 배수 출력하기
'''
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num}: 3 과 5의 공배수')
    elif num % 3 == 0:
        print(f'{num}: 3의 배수')
    elif num % 5 == 0:
        print(f'{num}: 5의 배수')    

'''
9. 사용자가 입력한 숫자를 리스트에 저장하다가
0 입력하면 종료 후 리스트 출력하기
[입력: 3 ,입력: 7, 입력: 2 ,입력: 0]
'''
# nums = [3, 7, 2, 0]
# while True:
#    userdata= int(input('숫자 입력: '))
#    print(f'nums: {nums}')
#    break

nums = [3, 7, 2, 0]
while True:
   userdata= int(input('숫자 입력: '))
   if userdata == 0:
       print('종료')
   
   print(f'nums: {nums}')
   break
   
