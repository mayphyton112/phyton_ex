'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입 2.로그인 3.특정 회원정보 출력 4. 모든 회원정보 출력 99. 종료
사용자가 
'1.회원가입'을 선택하면 회원ID, 회원PW, 회원Emaill, 회원Phone 정보를 입력받아 회원가입을 진행한다.
'2.로그인'을 선택하면 회원ID, 회원PW를 입력받아  로그인 '성공' 또는 '실패'를  출력한다. 인증(Authentication)/인가(Authorization)
'3. 특정 회원 정보 출력'를 선택하면 회원ID, 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
'4. 모든 회원 정보 출력'를 선택하면 가입되어 있는  모든 회원 정보를 출력한다.
'99. 종료'를 선택하면 프로그램을 종료시킨다.

심심하면 > 특정 회원의 회원ID, 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해보자
'''
SIGN_UP = 1  #회원가입
SIGN_IN = 2  #로그인
PRINT_MY_INFO = 3
PRINT_ALL_MEMBER_INFO = 4
SYSTEM_SHUTDOWN = 99

DEV_MOD= True

members = {}    # 나중에는 database로 바뀐다.

if DEV_MOD:

    uIds = ['gildong', 'chanho', 'saeri']
    uPws = ['1234', '5678', '9012']
    uMails = ['gildong@gmail.com', 'chanho@naver.com', 'saeri@daum.net']
    uPhones = ['010-1234-5678', '010-9999-8888', '010-7777-6666']
    
    for n in range(len(uIds)):   #3회 반복 (0, 1, 2)
        members[uIds[n]] = {
            'uId': uIds[n],
            'uPw': uPws[n],
            'uMail': uMails[n],
            'uPhone': uPhones[n]
        }
#functions Start
def getSelectedMenuNum():
    selectedMenuNum = int(input('1.회원가입 2.로그인 3.나의 회원정보 출력 4. 모든 회원정보 출력 99. 종료'))
    return selectedMenuNum

def setNewNumber(uId, uPw, uMail, uPhone):
    members[uId] = {
                'uId': uId,
                'uPw': uPw,
                'uMail': uMail,
                'uPhone': uPhone
            }
    
def isNotMember(uId):
    if uId in members:
            print(f'{uId}는 이미 사용중입니다. 다시 확인하세요.')
            return False
    else:
        return True

def printALlMemberInfo(value):
    for key1, value1 in value.items():
                print(f'{key1}: {value1}')

#functions END


flag = True
while flag:

    userSelectedMenuNum= getSelectedMenuNum()

    if userSelectedMenuNum == SIGN_UP:    #1. 회원가입
        uId = uId = input('input member ID:')
        if isNotMember(uId):
            uPw = input('input member PW:')     #원래는 데이터베이스에 이것을 저장해야한다.
            uMail = input('input member EMAIL:')
            while True:
                if '@' not in uMail:
                    print('입력한 이메일 주소가 형식에 맞지 않습니다.') #이메일 주소 확인하기
                    uMail = input('input member EMAIL:')
            
                else: 
                    break

            uPhone = input('input member PHONE:')
            setNewNumber(uId, uPw, uMail, uPhone)
            print('SIGN-UP SUCESS')
        
        if DEV_MOD: print(f'members: {members}')
    
    elif userSelectedMenuNum ==SIGN_IN: #2. 로그인
        signCount = 1
        while True:
            uId = input('input member ID:')
            uPw = input('input member PW:')
    
            if uId in members:
                uInfo = members[uId]
                if uInfo['uPw'] == uPw:
                    print('SIGN_IN SUCCESS')
                else:
                    print('SIGN_IN FAIL')
                    singIncount +=1
                    if singIncount > 3:
                        print('3회 이상 틀렸어요')
                        break
    
            else: 
                print('존재하지않는 ID입니다. 다시 확인하세요')

    
    elif userSelectedMenuNum ==PRINT_MY_INFO:    #3. 나의 정보 출력
        uId = input('input member ID:')
        uPw = input('input member PW:')

        if uInfo in members[uId]:
            if uInfo['uPw'] == uPw:
                print('SIGN_IN SUCCESS')

                print('-' * 30)
                print(f'uId: {uId}')
                for key, value in uInfo.items():
                    print(f'{key}: {value}')
                print('-' * 30)

            else:
                print('SIGN_IN FAIL')
        
        else: 
            print('존재하지않는 ID입니다. 다시 확인하세요')
    
    elif userSelectedMenuNum ==PRINT_ALL_MEMBER_INFO:   #4. 모든 회원정보 출력
        for key, value in members.items():
            print(f'{key}님의 정보-----------')
            printALlMemberInfo(value)
            print('-' * 30)

    elif userSelectedMenuNum ==SYSTEM_SHUTDOWN:  #99. 종료
        flag = False
        print('Good bye')

'''
회원가입 과정이 view,  자료가 이동하는 것이 model
'''