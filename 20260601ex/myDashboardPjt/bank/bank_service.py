import config as root_config
from bank import config as bank_config
import session
import os
import json
import uuid

class BankService:
    def __init__(self):
        self.accounts = {}
        self.init_database()

    def init_database(self):
        #현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')
        
        #프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')
        
        # db/accounts.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'members.json')
        print(f'self.dbFile: {self.dbFile}')
        #C:\ktj\python\python_ex\20260601ex\myDashboardPjt\db\accounts.json


        #파일 존재여부 확인
        if not os.path.exists(self.dbFile): #init data base
            self.save_accounts(self.accounts)
            # self.save_members({}) 이것도 되긴한다.
        else:
            self.members = self.load_accounts()
        
        #JSON 파일 저장
    def save_accounts(self, accounts):  #위에 코딩하려는 내용을 밑으로 뻈다.
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(accounts, f, ensure_ascii=False, indent=4) #기존 내용을 지우고 새로  적는 내용으로 덮어씌운다.

    def load_accounts(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
             #로드는 내용을 파이썬에 맞게 가져오는 것
            return json.load(f)
        
    def isMYAccounts(self):
        allAccounts = self.load_accounts()
        if session.getSignInedMemberId() in allAccounts:
            return True
        return False

    
    def run(self):

        if session.getSignInedMemberId() == '':
            print('PLEASE SIGN IN')
            return #종료함수
        
        
        flag = True
        while flag:

            if self.isMYAccount():
                menuNum = int(input('1.ACCOUNT_LIST 2.NEW_ACCOUNT 99.SERVICE OUT '))
            else:
                print('No account yet')
                menuNum = int(input('3.DEPOSIT 4.WITHDRAWL 99.SERVICE OUT '))

            if menuNum == bank_config.ACCOUNT_LIST:
                pass
            elif menuNum == bank_config.NEW_ACCOUNT:
                self.accounts = self.load_accounts()
                if session.getSignInedMemberId() not in self.accounts:
                    self.accounts[session.getSignInedMemberId()] = {}

                myAccounts = self.accounts[session.getSignInedMemberId()]
                myAccounts[str(uuid.uuid4())] = {
                    'balance' : 0, #잔고
                    'histories': [], #입출금내역

                }

                self.save_accounts(self.accounts)
                print('NEW-ACCOUNT-CREATED')

                if root_config.DEV_MOD:
                    print(f'self.load_accounts : {self.load_accounts()}')
            
            elif menuNum == bank_config.DEPOSIT:
                pass
            elif menuNum == bank_config.WITHDRAWL:
                pass
            elif menuNum == bank_config.SERVICE_OUT:
                flag = False


if __name__ == '__main__':
    bankservice = BankService()
    bankservice.run()