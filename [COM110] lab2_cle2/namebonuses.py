# Sylvia Le
# 9/6/19
# File name: namebonuses.py
# Usernae generator

print("Username generator \n")
def main():
    fullName = input("Please enter your first and last name: ")
    names = fullName.lower().split()
    length = len(names)
    username = ''
    for i in range(length - 1):
        initial = names[i][0]
        username =  username + initial
    lastname = names[-1]
    username = username + lastname[:6]
    print("Your Username is:", username)
   
main()
