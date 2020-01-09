# Sylvia Le
# 9/6/19
# File name: readline.py

def main():
    inputfile = open("lab2poem.txt", "r")
    poem = inputfile.readline()
    print(poem)
    poem1 = inputfile.readline()
    print(poem1)
    remain = inputfile.readlines()
    print(remain)
    inputfile.close()

main()
