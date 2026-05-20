def convertUnit(lenMm):
    
    unitDic = {}

    unitDic ['cm'] = lenMm * .1
    unitDic ['m'] = lenMm * .001
    unitDic ['inch'] = lenMm * .03937
    unitDic ['ft'] = lenMm * .003281

    return unitDic

def printlength(lengths):
    for len in lengths.keys():
        print(f'{len}: {lengths[len]}{len}') #cm: 10cm

inputMmData = int(input('길이(mm)를 입력하라'))
resultData = convertUnit(inputMmData)
printlength(resultData)
