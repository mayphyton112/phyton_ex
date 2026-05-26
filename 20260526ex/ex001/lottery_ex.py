import random

userNums = []
randNums = []
collect = []

def setUNumbers(ns): #setter 어떠한 데이터를 세팅한다. set + UserNumbers C
    global userNums
    userNums = ns

def getUNumbers(): #getter 어떠한 데이터를 가져온다. get + UserNumbers R
    return userNums

# setter, getter의 기본 형태


def setRNumbers():
    global randNums
    randNums = random.sample(range(1, 46),6)

def getRNumbers():
    return randNums

def compareNumbers():
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)
    return collect 
