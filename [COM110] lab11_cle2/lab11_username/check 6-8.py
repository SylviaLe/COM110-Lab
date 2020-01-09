def main():
    twoDListbyCol = []
    for row in range(4):
        twoDListbyCol.append([])
        for col in range(4):
            twoDListbyCol[row].append(col)
    print(twoDListbyCol)
    print('----------------------')

    twoDListbyRow = []
    for row in range(4):
        twoDListbyRow.append([])
        for col in range(4):
            twoDListbyRow[row].append(row)
    print(twoDListbyRow)
    print('----------------------')

    multiples = []
    for row in range(4):
        multiples.append([])
        for col in range(4):
            multiples[row].append(row*col)
    print(multiples)
    print('----------------------')

##    twoDnumList = []
##    for row in range(4):
##        twoDnumList.append([])
##        for col in range(4):
##            twoDnumList[row].append(row*4)
##    for sub in range(4):
##        for col in range(4):
##            twoDnumList[sub][col] += col
##    for sub in range(4):
##        for col in range(4):
##            twoDnumList[sub][col] += 1
##    print(twoDnumList)

    twoDnumList = []
    for row in range(4):
        twoDnumList.append([])
        for col in range(4):
            twoDnumList[row].append(((row*4)+col)+1)
    print(twoDnumList)
    print('----------------------')
        
main()
