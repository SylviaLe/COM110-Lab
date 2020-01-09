def main():
    n = eval(input('Enter the dimension: '))
    twoDList = []
    for row in range(n):
        twoDList.append([])
        for col in range(n):
            twoDList[row].append(((row*n)+col)+1)

    for i in range(n):
        for j in range(n):
            print(twoDList[i][j], end = '\t')
        print(end = '\n')
main()
