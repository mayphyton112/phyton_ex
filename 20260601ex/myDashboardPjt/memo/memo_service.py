import session
import os
import json 
from memo import config as memo_config
import config as root_config
class MemoService:
    def __init__(self):
        self.memos = {}
        self.init_database()
    
    def init_database(self):
        #현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')
        
        #프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')
        
        # db/accounts.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'memos.json')
        print(f'self.dbFile: {self.dbFile}')
        #C:\ktj\python\python_ex\20260601ex\myDashboardPjt\db\memos.json

        #파일 존재여부 확인
        if not os.path.exists(self.dbFile): #init data base
            self.save_memos(self.memos)
            # self.save_members({}) 이것도 되긴한다.
        else:
            self.members = self.load_memos()
        
        #앱의 데이터를 JSON 파일에 저장하는 것
    def save_memos(self, memos):  #위에 코딩하려는 내용을 밑으로 뻈다.
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(memos, f, ensure_ascii=False, indent=4) #기존 내용을 지우고 새로  적는 내용으로 덮어씌운다.
    
    def isMYMemos(self):
        allMemos = self.load_memos()
        if session.getSignInedMemberId() in allMemos:
            return True
        return False

        #JSON 파일을 읽어 앱으로 데이터를 가져오는 것
    def load_memos(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
             #로드는 내용을 파이썬에 맞게 가져오는 것
            return json.load(f)
        
    def isMYMemos(self):
        allMemos = self.load_memos()
        if session.getSignInedMemberId() in allMemos:
            return True
        return False

    def run(self):
        
        if session.getSignInedMemberId() == '':
            print('PLEASE SIGN IN')
            return #종료함수
        
        flag = True
        while flag:
            if not self.isMYMemos():
                self.memos[session.getSignInedMemberId()] = []
                self.save_memos(self.memos)

            menuNum = int(input('1. write     2. read     3. update      4. delete     99. system_out '))
            if menuNum == memo_config.WRITE:
                newMemo = input('Write new memo:')

                self.memos = self.load_memos()
                myMemos= self.memos[session.getSignInedMemberId()]
                myMemos.insert(0, newMemo)

                self.save_memos(self.memos)
                print('WRITE SUCCESS')

                if root_config.DEV_MOD:
                    print(f'self.load_memos: {self.load_memos}')

            elif menuNum == memo_config.READ:
                self.memos = self.load_memos() #dict
                myMemos = self.memos[session.getSignInedMemberId()] #list
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx+1}] {memo}')

            elif menuNum == memo_config.UPDATE:
                self.memos = self.load_memos() #dict
                myMemos = self.memos[session.getSignInedMemberId()] #list
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx+1}]{memo}')
                selectedNumber = int(input('Please select the number to modify:'))
                memo = input('Edit memo:')
                myMemos[selectedNumber-1] = memo
                print('MODIFY SUCCESS')

                if root_config.DEV_MOD:
                    print(f'self.load_memos(): {self.load_memos}')


            elif menuNum == memo_config.DELETE:
                self.memos = self.load_memos() #dict
                myMemos = self.memos[session.getSignInedMemberId()] #list
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx+1}]{memo}')
                    
                selectedNumber = int(input('Please select the number to delete:'))
                myMemos.pop(selectedNumber-1)
                self.save_memos(self.memos)

                if root_config.DEV_MOD:
                    print(f'self.load_memos: {self.load_memos}')
            
            elif menuNum == memo_config.SERVICE_OUT:
                flag = False


if __name__ == '__main__':
    memoservice = MemoService()
    memoservice.run()