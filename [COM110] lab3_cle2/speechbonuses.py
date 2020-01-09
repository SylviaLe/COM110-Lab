def main():
    obama = open("ObamaSpeech2012.txt", "r", encoding = "utf-8")
    romney = open("RomneySpeech2012.txt", "r", encoding = "utf-8")

    obamatxt = obama.read().lower()
    obamaWord = obamatxt.split()

    romntxt = romney.read().lower()
    romnWord = romntxt.split()

    count1 = obamaWord.count("economy")
    count2 = romnWord.count("economy")

    posEcon1 = obamatxt.find("economy")
    posEcon2= romntxt.find("economy")
    if posEcon1 < posEcon2:
        print("Obama mentions economy earlier")
    else:
        print("Romney mentions economy earlier")

    freObama = count1/len(obamaWord)
    freRomn = count2/len(romnWord)
    if freObama > freRomn:
        print("Obama mentions economy more frequently")
    else:
        print("Romney mentions economy more frequently")

    newObama = open("NewObamaSpeech2012.txt", "w", encoding = "utf-8")
    newObamatxt1 = obamatxt.replace("america", "Vietnam").replace("united states", "Vietnam").replace("united states of america", "Vietnam")
    print(newObamatxt1)
    newObama.write(newObamatxt1)
    newObama.close()


main()
