from usrInfo import user, champSearch
runningON = True


def userV(user,nick):
    if user[0] == 0:
        print("\t\t\tsry i cant find " + nick + "\n\t\t\tTry it again pls")
    else:
        if len(user[1]) == 0 or user[6]== 0:
            print("\t\t\tNAME:"+user[0]+"\n\t\t\tRANK: Unranked")
        else:
            print("\t\t\tNAME:"+user[0]+"\n\t\t\tRANK:"+user[1]+" "+user[2])
            print("\t\t\tWINS:"+user[4]+"\tLOSES:"+user[5]+"\t\tWR: "+(user[6][0:5])+"%")



def menu(running):
    print(running)
    while running is True:
        print(running)
        print("\n\n0 - Exit")
        print("1 - CHECK STATUS")
        print("2 - SEARCH FOR A CHAMP INFO")
        usrChoice = int(input())
        verifyUserInput(usrChoice)





def verifyUserInput(usrChoice):
    if isinstance(usrChoice, int):
        if usrChoice == 1:
            nick = input("\t\t\tQual é o teu nick?").replace(" ", "")
            infoUser = user(nick)
            userV(infoUser, nick)
        elif usrChoice == 2:
            champName = input("\t\t\tQual é o champ?").replace(" ", "")
            infoChamp = champSearch(champName)
        elif usrChoice == 0:
            runningOFF = False
            menu(runningOFF)

    else:
        print("ONLY ACCEPT NUMBERS!")
        menu()




menu(runningON)




'''
def helper():
    print("_________________________________________________")
    print("WHICH LANE?\n")
    print("TOP/JG/MID/ADC/SUPP")
    lane = str(input("\n\nwrite ur lane: ")).upper()
    print(lane)
    if lane =='TOP' or lane =='JG' or lane =='MID' or lane =='ADC' or lane =='SUPP':
        print(1)
    else:
        print(2)

    print("_________________________________________________")
    print("WHAT YOU WANT?\n")
    print("\t\t\t1 - MINE TOP 5 MOST WR CHAMPS")
    print("\t\t\t2 - TOP 5 MOST WR CHAMPS(ATM)")
    print("\t\t\t3 - ALL CHAMPS WR")
    print("\t\t\t4 - ALL CHAMPS WR(ATM)")
    print("\t\t\t5 - SHOW LAST 5 CHAMPS AND RESULT")
    print("\t\t\t6 - BEST CHAMP TO PLAY VS")
    print("\n\t\t\t7-Back")
    want = input("\n\nSelect a number")
    print(lane+ want)
    helper()'''

