import random

number=[]
number.append([1,2,3])
number.append([4,5,6])
number.append([7,8,9])

game=[]
game.append(["-","-","-"])
game.append(["-","-","-"])
game.append(["-","-","-"])


onoff = True

playercaseID_x = 0
playercaseID_y = 0

IAcaseID_x = 0
IAcaseID_y = 0

spaceEnable = 9

first = random.randint(1,2)

def playerTurn():
    global spaceEnable
    global playercaseID_x
    global playercaseID_y
    playerChoice = int(input("chose a number : "))
    
    if(playerChoice not in [1,2,3,4,5,6,7,8,9]):
        print("you need to choose a number between 1 and 9")
        playerTurn()

    else:
        for x in range(0,len(number)):
            for y in range(0,len(number[x])):
                if(playerChoice == number[x][y]):
                    playercaseID_x = x
                    playercaseID_y = y
                
        if(game[playercaseID_x][playercaseID_y]=="-"):
            game[playercaseID_x][playercaseID_y] = "X"
            spaceEnable -= 1
        else:
            print("this place is not valide")
            playerTurn()

def setIAchoice(IA_choice):
    global spaceEnable
    for x in range(0,len(number)):
        for y in range(0,len(number[x])):
            if(IA_choice == number[x][y]):
                IAcaseID_x = x
                IAcaseID_y = y

    if(game[IAcaseID_x][IAcaseID_y]=="-"):
        game[IAcaseID_x][IAcaseID_y] = "O"
        spaceEnable -= 1
        return(True)
    else:
        return(False)
            


def checkClosetoWin():
    #check IA
    for x in range(0,len(game)):
        checkIA = 0
        for y in range(0,len(game[x])):
            if(game[x][y]=="O"):
                checkIA += 1
        if checkIA > 1:
            for y in range(0,len(game[x])):
                if(game[x][y]=="-"):
                    return(number[x][y])

    for y in range(0,len(game)):
        checkIA = 0
        for x in range(0,len(game[x])):
            if(game[x][y]=="O"):
                checkIA += 1
        if checkIA > 1:
            for x in range(0,len(game[x])):
                if(game[x][y]=="-"):
                    return(number[x][y])

    check = 0
    if(game[0][0]=="O"):
        check += 1
    if(game[1][1]=="O"):
        check += 1
    if(game[2][2]=="O"):
        check += 1
    if check > 1:
        if(game[0][0]=="-"):
            return(1)
        elif(game[1][1]=="-"):
            return(5)
        elif(game[2][2]=="-"):
            return(9)
    check = 0
    if(game[2][0]=="O"):
        check += 1
    if(game[1][1]=="O"):
        check += 1
    if(game[0][2]=="O"):
        check += 1
    if check > 1:
        if(game[2][0]=="-"):
            return(7)
        elif(game[1][1]=="-"):
            return(5)
        elif(game[0][2]=="-"):
            return(3)

    #check joueur
    for x in range(0,len(game)):
        checkJoueur = 0
        for y in range(0,len(game[x])):
            if(game[x][y]=="X"):
                checkJoueur += 1
        if checkJoueur > 1:
            for y in range(0,len(game[x])):
                if(game[x][y]=="-"):
                    return(number[x][y])

    for y in range(0,len(game)):
        checkJoueur = 0
        for x in range(0,len(game[x])):
            if(game[x][y]=="X"):
                checkJoueur += 1
        if checkJoueur > 1:
            for x in range(0,len(game[x])):
                if(game[x][y]=="-"):
                    return(number[x][y])

    check = 0
    if(game[0][0]=="X"):
        check += 1
    if(game[1][1]=="X"):
        check += 1
    if(game[2][2]=="X"):
        check += 1
    if check > 1:
        if(game[0][0]=="-"):
            return(1)
        elif(game[1][1]=="-"):
            return(5)
        elif(game[2][2]=="-"):
            return(9)
    check = 0
    if(game[2][0]=="X"):
        check += 1
    if(game[1][1]=="X"):
        check += 1
    if(game[0][2]=="X"):
        check += 1
    if check > 1:
        if(game[2][0]=="-"):
            return(7)
        elif(game[1][1]=="-"):
            return(5)
        elif(game[0][2]=="-"):
            return(3)
    
    return(False)


def IAchoice():
    if spaceEnable == 9:
        setIAchoice(random.choice([1,3,7,9]))
    elif spaceEnable == 8:
        if(game[1][1]=="X"):
            setIAchoice(random.choice([1,3,7,9]))
        else:
            setIAchoice(5)
    elif spaceEnable == 7:
        verif = setIAchoice(5)
        if verif == False:
            for x in range(0,len(game)):
                for y in range(0,len(game[x])):
                    if game[x][y]=="O":
                        if(x==0)and(y==0):
                            verif = setIAchoice(random.choice([2,4]))
                            while verif == False:
                                verif == setIAchoice(random.choice([2,4]))
                        elif(x==2)and(y==0):
                            verif = setIAchoice(random.choice([4,8]))
                            while verif == False:
                                verif == setIAchoice(random.choice([4,8]))
                        elif(x==0)and(y==2):
                            verif = setIAchoice(random.choice([2,6]))
                            while verif == False:
                                verif == setIAchoice(random.choice([2,6]))
                        elif(x==2)and(y==2):
                            verif = setIAchoice(random.choice([6,8]))
                            while verif == False:
                                verif == setIAchoice(random.choice([6,8]))

    elif spaceEnable == 6:
        verif = checkClosetoWin()
        if verif!=False:
            verif = setIAchoice(verif)
        else:
            if(game[0][0]=="-")and(game[1][0]=="X")and(game[0][1]=="X"):
                setIAchoice(1)
            elif(game[0][2]=="-")and(game[0][1]=="X")and(game[1][2]=="X"):
                setIAchoice(3)
            elif(game[2][0]=="-")and(game[1][0]=="X")and(game[2][1]=="X"):
                setIAchoice(7)
            elif(game[2][2]=="-")and(game[2][1]=="X")and(game[1][2]=="X"):
                setIAchoice(9)
            elif(game[1][1]=="O"):
                verif = setIAchoice(random.choice([2,4,6,8]))
                while verif == False:
                    verif = setIAchoice(random.choice([2,4,6,8]))
            else:
                for x in range(0,len(game)):
                    for y in range(0,len(game[x])):
                        if game[x][y]=="O":
                            if(x==0)and(y==0):
                                verif = setIAchoice(random.choice([2,4]))
                                while verif == False:
                                    verif = setIAchoice(random.choice([2,4]))
                            elif(x==2)and(y==0):
                                verif = setIAchoice(random.choice([4,8]))
                                while verif == False:
                                    verif = setIAchoice(random.choice([4,8]))
                            elif(x==0)and(y==2):
                                verif = setIAchoice(random.choice([2,6]))
                                while verif == False:
                                    verif = setIAchoice(random.choice([2,6]))
                            elif(x==2)and(y==2):
                                verif = setIAchoice(random.choice([6,8]))
                                while verif == False:
                                    verif = setIAchoice(random.choice([6,8]))
                            elif(x==1)and(y==1):
                                verif = setIAchoice(random.choice([1,3,7,9]))
                                while verif == False:
                                    verif = setIAchoice(random.choice([1,3,7,9]))
    elif (spaceEnable == 5)or(spaceEnable == 4)or(spaceEnable == 3)or(spaceEnable == 2):
        verif = checkClosetoWin()
        if verif!=False:
            verif = setIAchoice(verif)
        else:
            verif = setIAchoice(random.choice([1,2,3,4,5,6,7,8,9]))
            while verif == False:
                verif = setIAchoice(random.choice([1,2,3,4,5,6,7,8,9]))

    elif spaceEnable == 1:
        for x in range(0,len(game)):
            for y in range(0,len(game[x])):
                if(game[x][y]=="-"):
                    setIAchoice(int(number[x][y]))

def winCheck():
    for x in range(0,len(number)):
        for y in range(0,len(number[x])):
            if(game[x][y] == "X"):
                if(x==0):
                    if((game[x + 1][y]=="X")and(game[x + 2][y]=="X")):
                        return("win")
                elif(x==1):
                    if((game[x + 1][y]=="X")and(game[x - 1][y]=="X")):
                        return("win")

                elif(y==0):
                    if((game[x][y + 1]=="X")and(game[x][y + 2]=="X")):
                        return("win")
                elif(y==1):
                    if((game[x][y + 1]=="X")and(game[x][y - 1]=="X")):
                        return("win")

            elif(game[x][y] == "O"):
                if(x==0):
                    if((game[x + 1][y]=="O")and(game[x + 2][y]=="O")):
                        return("lose")
                elif(x==1):
                    if((game[x + 1][y]=="O")and(game[x - 1][y]=="O")):
                        return("lose")

                elif(y==0):
                    if((game[x][y + 1]=="O")and(game[x][y + 2]=="O")):
                        return("lose")
                elif(y==1):
                    if((game[x][y + 1]=="O")and(game[x][y - 1]=="O")):
                        return("lose")

    if((game[0][0]=="X")and(game[1][1]=="X")and(game[2][2]=="X")):
        return("win")
    elif((game[0][2]=="X")and(game[1][1]=="X")and(game[2][0]=="X")):
        return("win")

    if((game[0][0]=="O")and(game[1][1]=="O")and(game[2][2]=="O")):
        return("lose")
    elif((game[0][2]=="O")and(game[1][1]=="O")and(game[2][0]=="O")):
        return("lose")

def relancer():
    global game
    global onoff
    global first
    global statut
    global spaceEnable
    replay = input("Veux tu rejouer ( oui ou non ) : ")
    if (replay=="non"):
        onoff = False
    elif(replay=="oui"):
        print("la partie se relance")
        first = random.randint(1,2)
        onoff = True
        game=[]
        game.append(["-","-","-"])
        game.append(["-","-","-"])
        game.append(["-","-","-"])
        statut = ""
        spaceEnable = 9
        for i in range(0, len(number)):
            print("|".join(str(e)for e in number[i]))
        print("-----------------")
    else:
        print("erreur")
        relancer()
                

while(onoff==True):

    for i in range(0, len(number)):
        print("|".join(str(e)for e in number[i]))
    print("-----------------")

    if first==1:
        playerTurn()
    elif first==2:
        IAchoice()

    for i in range(0, len(number)):
        print("|".join(str(e)for e in game[i]))
    print("-----------------")

    statut = winCheck()

    if(statut=="win"):
        print("win")
        relancer()
    elif(statut=="lose"):
        print("lose")
        relancer()
    elif(spaceEnable==0):
        print("draw")
        relancer()

    if first==1:
        IAchoice()
    elif first==2:
        playerTurn()

    for i in range(0, len(number)):
        print("|".join(str(e)for e in game[i]))
    print("-----------------")

    statut = winCheck()
    
    if(statut=="win"):
        print("win")
        relancer()
    elif(statut=="lose"):
        print("lose")
        relancer()
    elif(spaceEnable==0):
        print("draw")
        relancer()
