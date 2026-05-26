#지금까지는 파이썬 셀 창에 데이터를 출력하거나 입력했다. 
# 이 방법은 데이터를 일시적으로 메모리에 보관할 뿐 영구적이진 않다

#파이썬 파일 다루기 3단계
'''
1. 파일 열기 open() 함수를 이용한다.
   파일열기에 성공하면 파일이 객체로 만들어져 메모리에 생성된다.
2. 파일 쓰기/읽기 read()/write()
3. 파일 닫기 close()함수를 이용한다.
   쓰기 또는 읽기가 끝난 파일은 close()로 연결을 해제한다.
'''

# file = open('C:/ktj/python/test.txt', 'w') # test.txt파일을 쓰기 목적으로 연다. (없으면 파일이 생성되고 있으면 그 파일로 연결된다.)
# result = file.write('Hello python') #쓰기(write)
# print(f'result: {result}') #12 ------>쓴 문자열의 길이를 반환
# file.close() # 파일 닫기(close, 외부자원 해제)

# file = open('C:/ktj/python/test.txt', 'r')
# readresult = file.read()
# print(f'readresult: {readresult}')
# print(f'readResult type> {type(readresult)}')
# file.close()

# readresult += 1
# readresult = int(readresult)


# file = open('C:/ktj/python/test.txt', 'a') #기존 내용에 추가
# file.write('\nhello')
# file.close()

# with open('C:/ktj/python/test.txt', 'a') as file:
#     for n in range(10):
#         file.write('\nhello')

# 예외 처리(보험)
#세상의 모든 프로그램은 100% 완벽할 수 없다. 

print(10 + 20)  # 30
try:
    print(10 / 1)   # 에러 - try는 예외가 생길 수 있는 곳에만 넣어야 한다-생각보다 메모리를 많이 잡아먹는다.
except Exception as e:
    print(f'e: {e}')
else:
    print('에러가 발생하지 않으면 실행되는 코드') #옵션

finally:
    print('에러가 발생하든 하지않든 무조건 실행되는 코드')

print(10 - 20)  # X
print(10 * 20)  # X



# 예외 처리  기본 문법
'''
try ~ except
'''

# file = open('C:/ktj/python/test.txt', 'a')
# file.write('\nhi')
# file.close()

'''
파이썬 파일모드 가장 많이 쓰이는것:
"w": 쓰기모드
"r": 읽기모드
"a": 추가
'''

