from config_dir.dir import config
from member import session
from db import member_db
from db import diary_db
from member import member_dumy
import copy
if config.DEV_MOD:
    member_dumy.dumyInit()
    print(f'memberDB: {member_db.memberDB}')
    print(f'diaryDB: {diary_db.diaryDB}')

flag = True

while flag:

    menuNum = '' #초기화-아무것도 없는 상태로 시작한다. 
    if session.signInedMemberId =='':
        #sign out 상태
        menuNum = int(input('1.sign-up 2.sign-in 6.write 7.read 99.end'))
    else:
        #sign in 상태
        menuNum = int(input('3.modify 5.sign-out 6.write 7.read 4.delete 99.end'))


    if menuNum == config.SIGN_UP:
        print('1.sign-up')
        uId  = input('please input new member ID:')
        uPw  = input('please input new member PW:')
        uMail  = input('please input new member MAIL:')
        uPhone  = input('please input new member PHONE:')
        

        member_db.memberDB[uId] = {
            'uId': uId,
            'uPw': uPw,
            'uMail': uMail,
            'uPhone': uPhone
        }
        print('New member sign-up success')

        if config.DEV_MOD: #디버깅 
            print(f'memberDB: {member_db.memberDB}')
        diary_db[uId] = []
        if config.DEV_MOD:
            print(f'diaryDB: {diary_db.diaryDB}') #빈 방이 만들어진 것을 확인해야한다. 

    elif menuNum == config.SIGN_IN:
        print('2.sign-in')
        uId  = input('please input member ID:')
        uPw  = input('please input member PW:')

        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('sign-in success!!')
                session.signInedMemberId = uId
            else:
                print('sign-in fail!! -- PW error')
        else:
            print('sign-in fail!! -- ID error')
        
        # if uId in member_db.memberDB and member_db.memberDB[uId]['uPw'] == uPw:
        #         print('sign-in success!!')
        # else:
        #         print('sign-in fail!! -- PW or ID error')
    

    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
        '''
        id, pw, mail, phone 이 중에서 어떤 정보들만 수정가능하게 할 것인지 정해야한다.
        id: X -아이디 새로 만드려면 계정을 바꿔야한다. 또한 이미 탈퇴한 회원의 ID라도 절대 변경 사용할 수 없다.
        그렇다면 pw, mail, phone
        pw: 절대 수정이 불가하지는 않는다. 하지만 쉽게 변경할 수는 없다.
        mail과 phone: pw보다 수정이 쉽다. 비교적 간단하게 변경 가능
        '''
        upw  = input('please input member PW:')
        uMail  = input('please input member MAIL:')
        uPhone  = input('please input member PHONE:')
        uRegDate = input('please input member RegDate')
        UModDate = input('please input member RegDate')
        

        '''
        -member_db 모듈에 있는 memberDB 딕셔너리에서 회원정보를 변경한다.
        -현재 memberDB에는 'gildong', 'chanho' 회원이 있다.
        -현재 로그인 되어있는 회원정보를 불러와 그 정보를 수정한다.
        -즉 session.signInedMemberId 에서 현재 로그인 되어있는 회원 ID를 불러와 사용하면된다.
        '''
        currentSignInedMemberID = session.signInedMemberId
        memberInfo = member_db.memberDB[currentSignInedMemberID]
        if config.DEV_MOD: print(f'memberInfo: {member_db}')

        memberInfo['uPw'] = upw
        memberInfo['uMail'] = uMail
        memberInfo['uPhone'] = uPhone

        if config.DEV_MOD: print(f'after modify: memberInfo: {memberInfo}')
    
    elif menuNum == config.MEMBER_DELETE:
        print('4.delete')
        #메뉴 변경할 때 

        '''
        현재 로그인 되어있는 회원의 ID를 session.signInedMemberId에서 가져와서
        해당하는 회원의 정보를 member_db.memberDB에 삭제한다.
        '''
        currentSignInedMemberID = session.signInedMemberId
        del member_db.memberDB[currentSignInedMemberID] #dictionary에서 삭제시 del을 사용

        print('Member info delected')
        session.signInedMemberId = '' #공백으로 초기화한다.
        if config.DEV_MOD: print(f'member_db.memberDB: {member_db.memberDB}')
        

    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False
    elif menuNum == config.SIGN_OUT:
        print('5.sign_out')
        '''
        메뉴를 변경해야한다
        로그인값을 없애야겠다.
        로그인 값은 session 모듈의 signedMemberedId 변수로 있다.
        signedMemberid 값을 ''로 초기화한다.
        '''
        print('sign_out success')
        session.signInedMemberId = ''
    
    elif menuNum == config.DIARY_WRITE:
        print('6.write')
        
        if session.signInedMemberId =='':
            print('sorry, please sing-in') #원래는 로그인 화면으로 가야하는데 지금은 불가능하다.
        else:
            while True:
                diaryTxt = input('10글자 이내의 짧은 일기를 작성하세요')
                if len(diaryTxt) > 10:
                    print(f'10글자 초과({len(diaryTxt)})')
                else:
                    diary_db.diaryDB[session.signInedMemberId].append(diaryTxt)
                    if config.DEV_MOD: print(f'diary_db.diaryDB: {diary_db.diaryDB}')
                    break
            
    elif menuNum == config.DIARY_READ:
        print('7.read')

        if session.signInedMemberId =='':
            print('sorry, please sign-in') #원래는 로그인 화면으로 가야하는데 지금은 불가능하다.
        
        else:
            currentSignInedMemberID = session.signInedMemberId
            myDiaries = diary_db.diaryDB[currentSignInedMemberID]
            
            deepCopyDiaries = copy.deepcopy(myDiaries)
            deepCopyDiaries.reverse()
            for idx, diaryTxt in enumerate(deepCopyDiaries):
                print(f'({idx+1}): {diaryTxt}')

       
