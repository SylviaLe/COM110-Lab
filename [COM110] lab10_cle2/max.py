def maxNum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        temMax = maxNum(numList[1:])
        if numList[0] > temMax:
            return numList[0]
        else:
            return temMax
