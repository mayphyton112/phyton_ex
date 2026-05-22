def fun():
    print('module01의 함수가 실행됩니다.')

print(f'module01의 __name__: {__name__}') #파이썬 내장 전역변수
# print(f'module01의 __name__: module01') #파이썬 내장 전역변수

if __name__ =='__main__':
    fun()

