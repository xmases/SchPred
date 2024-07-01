import os
import sys
import random
from os.path import exists

#Number and code in list(list)
V, usedCodes= [], []

def create(Vnum) :
    trainCode = createCode(usedCodes)
    V.append([Vnum, trainCode])
    usedCodes.append(trainCode)

def createCode(list) :
    code = random.randint(0, 1000)
    for x in list:
        if x == code :
            createCode(list)
    return(code)

def trainInfo(Number) :
    for x in V:
        if x[0] == Number:
            print(str(x))

# Data Input Chart
# a = list(Route no correlation route code)
# a ex. = list(list(Route 1, Route Code x0x1), list() .. etc)
# Routes in order of var c
# b = Number of docks
# c = list(accesibility of docks via routes)
# c ex. = list(list(Dock no 1, acces via routes n1, acces via routes n2, etc))

def createStop(a, b, c, name, type):
    with open("stoptsdata.txt", "w") as data :
        data.write(str(a)+"."+str(b)+"."+str(c)+"."+name+"."+type)

def readstopsData() :
    print("Read Stops Data")

create("x")
trainInfo("x")
createStop([[1, "L1"]],2,[[1, 1],[2, 1]], "St1", "Train Station")
