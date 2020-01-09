# Sylvia Le
# 8/30/19
# COM110 Lab 1
# eagergreeter.py
#
# This program will print out "Hi!" over and over

def main():
   for i in range(20):
      print("Programming is fun!")
      
def hi():
   name = input("Enter your name: ")
   for k in range(20):
      print("Hi,", name, ". Nice to meet you!")

def birthday():
   number = eval(input("Pick a number: "))
   name = input("What's your name again? ")
   for j in range(number):
      print(j,". " "Happy Birthday,", name, "!", sep = "")

 
main()
hi()
birthday()

                 

