from util import util_time
from member import config as member_config
import config as root_config
import os
import json
import session

class MemberService:
    def __init__(self):  #초기화하는것은 여기서 한다.
        self.members = {}
        self.init_database()
    
    #회원 가입 기능
    def sign_up(self):
        mId = input('새 id 입력: ')
        
        # ID 중복체크를 할때 self.members를 사용한다.
        if mId in self.members:
            print('이미 사용중인 아이디입니다.')
            return #return none 인듯

        mPw = input('새 pw 입력: ')
        mMail = input('새 mail 입력: ')
        mPhone = input('새 phone 입력: ')

        newMember = {
            'mId': mId,
            'mPw': mPw,
            'mMail': mMail,
            'mPhone' : mPhone,
            'mRegDate' : util_time.getcurruentDateTime(), #현재 시간을 구하는 코드는 지금 넣지 않는 것이 좋다. ->시간을 구하는 모듈을 만든다.
            'mModDate' : util_time.getcurruentDateTime()
        }

        self.members[mId] = newMember 
        #newMember{}의 mId라는 키값의 벨류를 self.members{}에 저장한다.

        #DB(members.json)에 새 회원 정보 저장
        self.save_members(self.members)

        print('MEMBER SIGN-UP SUCCESS')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')
        #   print(f'self.members : {self.members}')

    
    #회원 로그인
    def sign_in(self):
        mId = input('Input member ID:')
        mPw = input('Input member PW:')

        self.members = self.load_members()
        if mId in self.members and self.members[mId]['mPw'] == mPw:
            print('MEMBER SIGN_IN SUCCESS')
            # session.signInedMemberId = mId
            session.setSignInedMemberId(mId)
            
            if root_config.DEV_MOD:                           
                print(f'session.signInedMemberId: {session.signInedMemberId}')
            return

        print('MEMBER SIGN_IN FAIL')
           
        
    #로그아웃 기능
    def sign_out(self):
        session.setSignInedMemberId()
        print('SIGN-OUT SUCCESS')

    #회원 수정
    def modify(self):
        mPW = input('새 pw 입력: ')
        mMail = input('새 mail 입력: ')
        mPhone = input('새 phone 입력: ')

        self.members = self.load_members()
        memberForModify = self.members[session.getSignInedMemberId()]

        memberForModify['mPw'] = mPW
        memberForModify['mMail'] = mMail
        memberForModify['mPhone'] = mPhone
        memberForModify['mModDate'] = util_time.getcurruentDateTime()

        self.save_members(self.members)
        print(f'MODIFY SUCCESS')
        
        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')

    # 회원 탈퇴 기능
    def delete(self):
        confirm = input('정말 탈퇴하겠습니까? [Y] or [N]')
        if confirm == 'Y':
            self.members = self. load_members()
            del self.members[session.getSignInedMemberId()]
            self.save_members(self.members)
            session.setSignInedMemberId()
            print('DELETE SUCCESS')

            if root_config.DEV_MOD:
                print(f'self.load_members(): {self.load_members()}')

    def run(self):
        flag = True
        #while  flag
        while flag:
        #    if session.signInedMemberId == '':

           if session.setSignInedMemberId() =='':
               menuNum = int(input('1. Sign_up 2.sign_in  99. service_out' ))
           else:
               menuNum = int(input('3. sign_out 4. modify 5. delete 99. service_out' ))
           
           if menuNum == member_config.SIGN_UP:
               self.sign_up()
           elif menuNum == member_config.SIGN_IN:
               self.sign_in()
           elif menuNum == member_config.SIGN_OUT:
               self.sign_out()
           elif menuNum == member_config.MODIFY:
               self.modify()
           elif menuNum == member_config.DELETE:
               self.delete()
           elif menuNum == member_config.SERVICE_OUT:
               flag = False
    
    def init_database(self):
        
        #현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')
        
        #프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')
        
        # db/members.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'members.json')
        print(f'self.dbFile: {self.dbFile}')
        #C:\ktj\python\python_ex\20260601ex\myDashboardPjt\db\members.json


        #파일 존재여부 확인
        if not os.path.exists(self.dbFile): #init data base
            self.save_members(self.members)
            # self.save_members({}) 이것도 되긴한다.
        else:
            self.members = self.load_members()
    
    #JSON 파일 저장
    def save_members(self, members):  #위에 코딩하려는 내용을 밑으로 뻈다.
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=4) #기존 내용을 지우고 새로  적는 내용으로 덮어씌운다.

    def load_members(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
             #로드는 내용을 파이썬에 맞게 가져오는 것
            return json.load(f)

if __name__ == '__main__':
    MemberService = MemberService()
    MemberService.run()
    #객체
