#클래스(객체를 만들기 위한 툴(설계도 )) 문법

#붕어빵 클래스 
class FishBread: #클래스 선언
    
    #속성(attribute)
     def __init__(self, f, b):
          self.flour = f
          self.bean = b


    #기능(function, method)
    
     def makeFishBread(self):
          print('붕어빵 제조')
#붕어빵 클래스로부터 객체를 만들어보자
myFishBread = FishBread('팥', '밀가루') #클래스가 팥과 밀가루로 초기화된다.
friendFishBread = FishBread('호박', '쌀') #클래스가 팥과 밀가루로 초기화된다.
hisFishBread = FishBread('꿀', '밀가루') #클래스가 팥과 밀가루로 초기화된다.
#객체가 처음 설정될 때 넣어야할 기본 값을 넣는다.)
#참조 데이터 타입으로 객체가 가진 주소값을 가진다.

print(f'내 붕어빵의 속 내용물: {myFishBread.flour}')
print(f'내 붕어빵의 반죽:{myFishBread.bean}')

print(f'친구 붕어빵 속 내용물: {friendFishBread.flour}')
print(f'친구 붕어빵의 반죽:{myFishBread.bean}')

#계산기 클래스
class Calculator:
     #속성
     def __init__(self, n1, n2):
          self.num1 = n1
          self.num2 = n2
     #기능
     def add(self):
          print(f'add: {self.num1 + self.num2}')
     
     def sub(self):
          print(f'add: {self.num1 - self.num2}')
     
     def mul(self):
          print(f'add: {self.num1 * self.num2}')
     
     def div(self):
          print(f'add: {self.num1 / self.num2}')

myCalculator = Calculator(10, 20)
friendCalculator = Calculator(100, 200)

(myCalculator.add())
(myCalculator.sub())
(myCalculator.mul())
(myCalculator.div())

# 사람 클래스
class Human:
     #속성
     def __init__(self, height, weight): # 매개변수(왜부에서 넣은 값)는 객체안의 변수와 다르다. 매개변수에 객체안의 변수를 할당
          self.height= height
          self.weight= weight

     #기능
     def walk(self):
          print('걷자')
     
     def run(self):
          print('달리자')
     
     def printMyInfo(self):
          print(f'나의 신장: {self.height}')
          print(f'나의 몸무게: {self.weight}')


human1 = Human(188, 87)
human2 = Human(165, 49)

human1.printMyInfo()
human2.printMyInfo()

human1 = human2
human1.printMyInfo() # 165, 49


