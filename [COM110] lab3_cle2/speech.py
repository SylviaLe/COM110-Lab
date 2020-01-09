def main():
    obama = open("ObamaSpeech2012.txt", "r", encoding = "utf-8")
    romney = open("RomneySpeech2012.txt", "r", encoding = "utf-8")
    obamaWord = obama.read().lower().split()
    romnWord = romney.read().lower().split()
    if len(obamaWord) > len(romnWord):
        print("Obama's speech is longer")
    else:
        print("Romney's speech is longer")
    randomWord = input("Enter a word you want to find in lowercase: ")
    count1 = obamaWord.count(randomWord)
    count2 = romnWord.count(randomWord)
    if count1 > count2:
        print("Obama's speech mentions", randomWord, "more times, specifically", count1, "times")
    else:
        print("Romney's speech mentions", randomWord, "more times, specifically", count2, "times")

main()
