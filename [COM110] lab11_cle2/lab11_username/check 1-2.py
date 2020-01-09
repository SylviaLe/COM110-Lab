def getInput():
    n = eval(input("Enter a number greater than 0: "))
    if n > 0:
        print('Thank you')
    else:
        getInput()

def countDown(n):
    while n >= 0:
        print(n)
        n -= 1
    print('End.')
#getInput()
countDown(10)

