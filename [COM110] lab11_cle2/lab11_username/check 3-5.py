def main():
    twoDnumList = [ [1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16] ]
    print(twoDnumList[2][3])
    print('------------')
    for i in range(len(twoDnumList)):
        for j in range(len(twoDnumList[i])):
            print(twoDnumList[i][j], end = '\t')
        print('\n', end = '')

main()
