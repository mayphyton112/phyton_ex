import config
from member import member_service
from bank import bank_service
from memo import memo_service
from todo import todo_service
def main():
    flag = True
    while flag:
        menuNum = int(input('1. MEMBER  2. BANK  3. MEMO  4. TODO  99.SYSTEM-OUT' ))
        if menuNum == config.MEMBER_SERVICE:
            # MemberService = member_service.MemberService()
            # MemberService.run()
            member_service.MemberService().run()
        
        elif menuNum == config.BANK_SERVICE:
            # BankService=bank_service.BankService()
            # BankService.run()
            bank_service.BankService().run()
            
        elif menuNum == config.MEMO_SERVICE:
            memo_service.MemoService().run()
        elif menuNum == config.TODO_SERVICE:
            todo_service.TodoService().run()
        elif menuNum == config.SYSTEM_OUT:
            flag = False


#컨트롤러는 이것이 끝이다.
        

if __name__ == "__main__":
    main()
#app.py가 controller의 역할을 한다. 비지니스 로직이 들어가면 안됨