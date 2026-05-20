#단위환산 프로그램
'''
mm단위의 길이를 입력하면 cm, m, inch, ft등으로 단위가
변환되어 출력되는 함수가 포함된 프로그램을 만들어보자
'''

# def convertUnit(lenMm):
    
#     unitDic = {}

#     unitDic ['cm'] = lenMm * .1
#     unitDic ['m'] = lenMm * .001
#     unitDic ['inch'] = lenMm * .03937
#     unitDic ['ft'] = lenMm * .003281

#     return unitDic

# def printlength(lengths):
#     for len in lengths.keys():
#         print(f'{len}: {lengths[len]}{len}') #cm: 10cm

# inputMmData = int(input('길이(mm)를 입력하라'))
# resultData = convertUnit(inputMmData)
# printlength(resultData)

'''
DW마트는 고객 감사의 일환으로 '오늘의 할인' 이벤트를  진행할 계획입니다.
아래의 상품 가격표를 참고해 '오늘의 할인율'을 입력하면 할인된 가격이 출력되는
프로그램을 만들어보자
쌀: 9,000
상추: 1,900
고추: 2,900
마늘: 8,900
통닭: 5,600
햄: 6,000
치즈: 3,900
'''

# standardPrice = {
#     '쌀'  : '9000', int 에는 숫자 중간에 , 가 들어가면 안된다.
#     '상추': '1900',
#     '고추': '2900',
#     '마늘': '8900',
#     '통닭': '5600',
#     '햄'  : '6000',
#     '치즈': '3900'
# }

# def getDiscoutPrice(rate): #할인율을 dcprice에 넣어 그 값을  반환한다.
#     dcPrice = {}

#     for goodsName in standardPrice.keys():
#         disPrice = int(standardPrice[goodsName]) * (1-(rate / 100))
#         dcPrice[goodsName] = disPrice

#     return dcPrice

# def printPrice(priceList):
#     for goodsName, goodsPrice in priceList.items():
#         print(f'{goodsName}\t: {standardPrice[goodsName]}원---> {inputRateData}%DC({goodsPrice}원)')

# inputRateData = int(input('오늘의 할인률: '))

# discountPrice = getDiscoutPrice(inputRateData)

# printPrice(discountPrice)

# #영어 사전 만들기
# englishDictionary = {
#     'apple': '사과',
#     'chair': '의자',
#     'doll': '인형',
#     'book': '책',
#     'piano': '피아노',
#     'clock': '시계'

# }

# def printWord(engWord):
#     print(f'{engWord}: {englishDictionary[engWord]}')

# printWord(input('찾고자하는 영어단어:'))


