# Sylvia Le
# 9/6/19
# File name: Pizza.py
# This programs prompt users to input the pizza price for both size, calculate and compare the price per square inch

import math
print("This program will calculate and compare the price per square inch of pizza at Two Wives \n")
def main():
    priceSmall = eval(input("Enter the price of the small size pizza (8 inches): "))
    priceBig = eval(input("Enter the price of the large size pizza (14 inches): "))

    const = math.pi 
    areaSmall = (4**2) * const
    areaBig = (7**2) * const

    aveSmall = round((priceSmall/areaSmall), 2)
    aveBig = round((priceBig/areaBig), 2)

    print("The price of square inch for 8\" pizza is $", aveSmall, "/si", " whereas the price of square inch for 14\" pizza is $", aveBig, "/si", sep = "")

main()
