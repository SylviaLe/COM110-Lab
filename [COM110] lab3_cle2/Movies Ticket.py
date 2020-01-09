def price():
    adtTicket = eval(input("Please enter the standard ticket price: "))
    age = eval(input("Please enter your age: "))
    time = input("You like early or regular screening? Don't type in something weird: ")
    else:
        print()
        if age < 3:
            print("Youare a baby, so the ticket is free")
        elif age < 13 and age >3:
            kidTicket = adtTicket/2
            print("You are a child, your ticket price is half the standard, so it is $", kidTicket, sep = "")
            if time == "early" or time == "Early":
                print("And since you like to watch early, so you get a little discount. Your final price: $", (kidTicket - 1), sep = "")
        elif age > 13 and age < 60:
            print("You are an adult, your ticket price is the standard price, so it is $", adtTicket, sep ="")
            if time == "early" or time == "Early":
                print("And since you like to watch early, so you get a little discount. Your final price: $", (adtTicket - 1), sep = "")
        else:
            senTicket = adtTicket * 0.75
            print("Your ticket price is three fourth the standard price, so it is $", senTicket, sep = "")
            if time == "early" or time == "Early":
                print("And since you like to watch early, so you get a little discount. Your final price: $", (senTicket - 1), sep = "")

def movieList():
    print("The current movies at the theater are: \n IT Chapter Two \n Hustlers \n Angel has Fallen \n The Lion King \n Good Boy")

def main():
    print("Please choose an option: \n (A) List the current hot movies \n (B) Calculate ticket price \n")
    choice = input("Please type the letter of your option: ")
    if choice == "a" or choice == "A":
        movieList()
    elif choice == "b" or choice == "B":
        price()
    else:
        print("We will come up with new function later =)))")
main()

    
