# Sylvia Le
# 9/6/19
# File name: inputfile.py

def main():
    inputfile = open("lab2poem.txt", "r")
    hello = inputfile.read()
    print(hello)
    inputfile.close()

main()
