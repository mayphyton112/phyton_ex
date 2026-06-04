import urllib.request
import datetime
import json

SERVICE_KEY = 'a00117c4fc97bdb98b11c010b63d2ad04391c07791cdc79958af46b88b37ed89'

def getRequestURL(url):
    req = urllib.request.Request(url)

    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print(f'[{datetime.datetime.now()}]REQUEST COMMUNICATION SUCCESS') #앞에 시간적기가 관례
            return res.read().decode('utf-8')
        
    except Exception as e:
         print(f'[{datetime.datetime.now()}]REQUEST COMMUNICATION FAIL')
         print(f'e: {e}')
         return None


def getTourismStatesItem(yyyymm, nat_cd, ed_cd):
    serviceURL = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    parameters = "?"
    parameters += "_type=json&"
    parameters += "serviceKey=" + SERVICE_KEY + '&' #공백이 있으면 안된다.
    parameters += "YM=" + yyyymm + '&'
    parameters += "NAT_CD=" + nat_cd + '&'
    parameters += "ED_CD=" + ed_cd

    url = serviceURL + parameters
    # print(f'url: {url}')
    res = getRequestURL(url) #None or not None
    if res == None:
        return None
    else:
        return json.loads(res)
        # json.loads()는 JSON 형식의 문자열을 파이썬 애플리케이션에서 쉽게 사용할 수 있도록 변환
        # Json 형식의 문자열(str) -----> dic 객체


def getTourismStatesService(nat_cd, ed_cd, nStartYear, nEndYear):
    
    jsonResult = []
    result = []
    natName = ''
    isDataEnd = 0
    dataEND = f'{str(nEndYear)}{str(12)}' #202012


# 24  10
    #2025 ~ 2026 : 1 ~ 12, 1 ~ 5
    # 2026년의 데이터는 내년에 수집될 가능성이 높다. 
    for year in range(nStartYear, nEndYear + 1):  #년
        for month in range(1, 13):                #월
            if isDataEnd == 1:
                break

            yyyymm = f'{str(year)}{str(month):0>2}'  #2020 ~ 2021 : 202003(o) 202003(x) 전자의 경우로 맞춰야 한다. 빈공간을 채워 오른쪽 정렬을 해라 
            # print(f'yyyymm: {yyyymm}')
            jsonData = getTourismStatesItem(yyyymm, nat_cd, ed_cd)
            # print(f'jsonData: {jsonData}')
            if jsonData['response']['header']['resultMsg'] == 'OK':

                # 데이터 끝 확인
                if jsonData['response']['body']['items'] == '':
                    isDataEnd = 1 # 데이터 끝 확인용 flag 변수
                    dataEND = f'{str(year)}{str(month-1):0>2}'
                    print('DATA END')
                    break
                
                #json data 확인
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace(' ', '') #중 국 -> #중국
                num = jsonData['response']['body']['items']['item']['num']
                ed = jsonData['response']['body']['items']['item']['ed']
                # print(f'[{natName}] [{num}] [{ed}]')

                jsonResult.append({
                    'nat_name': natName,
                    'nat_cd': nat_cd,
                    'yyyymm': yyyymm,
                    'visit_cnt': num,
                })
    
    return (jsonResult, natName, ed, dataEND)

def main():

    jsonResult = []
    natName = ''

    print('----------------------------------------')
    print('-------국내 입국한 외국인 통계 데이터 ------')
    print('----------------------------------------')

    nat_cd = input('국가 코드 입력[중국(112), 일본(130), 미국(275)]:').strip()
    nStartYear = int(input('데이터 수집 시작 년도: '))
    nEndYear = int(input('데이터 수집 끝 년도: '))
    ed_cd = 'E' # E: 입국 D: 출국

    jsonResult, natName, ed, dataEND = getTourismStatesService(nat_cd, ed_cd, nStartYear, nEndYear)
    # print(f'jsonResult: {jsonResult}')
    # print(f'natName: {natName}')
    # print(f'ed: {ed}')
    # print(f'dataEnd: {dataEND}')
    
    if natName == '':
        print('데이터 수집오류! 서버 담당자한테 문의하세요')
    else:
        print('데이터 수집 성공')
        with open(f'./{natName}_{ed}_{nStartYear}_{dataEND}.json', 'w', encoding='utf-8') as f:
            jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            f.write(jsonFile)



if __name__ == '__main__':
    main()
