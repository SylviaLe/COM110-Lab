from random import randrange
def main():
    list =[]
    for i in range(6):
        x = randrange(10)
        if x in list:
            x = randrange(10)
        list.append(x)
    print(list)

main()
        
