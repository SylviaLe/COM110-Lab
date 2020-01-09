from random import *
def sim(n):
    doors = ['g', 'g', 'c']
    wins = 0
    loses = 0

    for i in range(n):
        shuffle(doors)
        userDoor = doors[randrange(3)]
        montyDoor = doors[randrange(3)]
        if montyDoor == 'c' or montyDoor == userDoor:
            montyDoor = doors[randrange(3)]

        if userDoor == 'c':
            loses += 1
        else:
            wins += 1
            
    print('Wins:', wins)
    print('Loses:', loses)
    print('By changing the doors, you win', round((wins/n)*100, 2), '% of the time')

def main():
    sim(100000)

main()
    
    
