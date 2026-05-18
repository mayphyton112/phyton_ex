
# data = int(input('수심을 입력하세요. '))
# temperature = 20 - (data / 10 * .7)
# print(f'temperature:{temperature}')

# #속도와 시간을 입력하면 자동자의 주행거리를 구하는 프로그램을 만들어라
# # d = speed * time

# speed = input('주행속도:')
# time = input('주행시간:')
# distance = int(speed) * int(time)
# print(f'주행거리: {distance}')

# '''
# A회사는 3대의 컴퓨터로 8시간을 일하면 하루 업무를 처리할 수 있습니다.
# 그런데 단축 근무를 하게 되어 근무 시간이 줄게 되었다면
# 몇 대의 컴퓨터가 더 필요할까

# 근무 시간을 입력하면 필요한 컴퓨터 수량을 파악하는 프로그램을 만들어라

# '''
# # 3 * 8 = 24
# # 24 / 8 = 3
# worktime = int(input('하루의 근무시간'))  #단축 근무 시간
# computer = 3 * 8 // time
# addComputer = 1 if (3 * 8 % time) > 0 else 0
# 
# totalComputer = computer + addComputer
# print(f'필요한 컴퓨터 개수: {totalComputer}')
 
# #한개에 340원 하는 마스크 X개를 구매하고 y원을 지불했을 때 거스름돈 result를 출력하리
# maskPrice = 340
# maskCnt = input(int('마스크 구매 개수'))
# total = maskPrice * maskCnt
# cash = int(input('지불금액'))
# change = cash - total
# print(f'거스름돈: {change}')

# #13시 30분 25초를 초로 나타내는 프로그램을 만드시오
# print(f'{25 + (60 * 30) + (60 * 60 * 13)}')

#학생의 국어, 영어, 수학 점수를 입력하면  총점과 평균을 출력하는 프로그램을 만들어라
# kor = int(input('국어 점수:'))
# eng = int(input('영어 점수:'))
# mat = int(input('수학 점수:'))
# totalScore = kor + eng + mat
# aver = totalScore / 3
# print(f'총점: {totalScore}')
# print(f'평균: {aver}')

# kor = input('국어 점수:')
# eng = input('영어 점수:')
# mat = input('수학 점수:')
# totalScore = int(kor + eng + mat)
# aver = totalScore / 3
# print(f'총점: {totalScore}')
# print(f'평균: {aver}')

# 밤 최저 기온과 낮 최고 기온을 입력하면 일교차를 출력하는 프로그램을 만드시오
lowTemp = int(input(f'최저기온:'))
highTemp = int(input(f'최고기온:'))
dailyTemp = highTemp - lowTemp
print(f'일교차: {dailyTemp}')

# 사용자가 길이(cm)를 입력하면 inch로 환산하는 프로그램을 만드시오(다만,1cm = 0.39inch)
cm = int(input(f'길이(cm):'))
inch = cm * 0.39
print(f'길이(inch): {inch}')