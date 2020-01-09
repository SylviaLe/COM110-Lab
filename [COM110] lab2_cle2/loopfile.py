# Sylvia Le
# 9/6/19
# File name: loopfile.py

def main():
    inputfile = open("lab2poem.txt", "r")
    for line in inputfile:
        print(line)
    inputfile.close()

main()
