# Sylvia Le
# 9/6/19
# File name: discussionEx 2.py

def main():
    s1 = "spam"
    s2 = "ni!"
    a = s2.upper()
    b = s2 + s1 + s2
    c = (s1.capitalize() + " " + s2.capitalize()) * 3
    d1, d2 = s1.split("a")
    d = "[" + d1 + ", " + d2[0] + "]"
    e = d1 + d2[0]

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

main()
    
