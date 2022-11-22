import random

number=[]
number.append([1,2,3])
number.append([4,5,6])
number.append([7,8,9])

game=[]
game.append([0,0,0])
game.append([0,0,0])
game.append([0,0,0])

onoff = True

playercaseID_x = 0
playercaseID_y = 0

IAcaseID_x = 0
IAcaseID_y = 0

spaceEnable = 9

def checkClosetoWin():
    #check IA horizontal
    for x in range(0,len(game)):
        check = 0
        for y in range(0,len(game[x])):
            if(game[x][y]=="O"):
                check += 1
        if check > 1:
            for y in range(0,len(game[x])):
                if(game[x][y]=="O"):
                    return(number[x][y])

    #check IA vertical
    for y in range(0,len(game)):
        check = 0
        for x in range(0,len(game[y])):
            if(game[x][y]=="O"):
                check += 1
        if check > 1:
            for y in range(0,len(game[x])):
                if(game[x][y]=="O"):
                    return(number[x][y])

    #check IA diago
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
            
    #check Player horizontal
    for x in range(0,len(game)):
        check = 0
        for y in range(0,len(game[x])):
            if(game[x][y]=="X"):
                check += 1
        if check > 1:
            for y in range(0,len(game[x])):
                if(game[x][y]=="-"):
                    return(number[x][y])

    #check Player vertical
    for y in range(0,len(game)):
        check = 0
        for x in range(0,len(game[y])):
            if(game[x][y]=="X"):
                check += 1
        if check > 1:
            for y in range(0,len(game[x])):
                if(game[x][y]=="X"):
                    return(number[x][y])

    #check Player diago
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


                

def playerTurn():
    while(spaceEnable > 0):

        playerChoice = int(input("chose a number : "))

        for x in range(0,len(number)):
            for y in range(0,len(number[x])):
                if(playerChoice == number[x][y]):
                    playercaseID_x = x
                    playercaseID_y = y
                

        if(game[playercaseID_x][playercaseID_y]=="-"):
            game[playercaseID_x][playercaseID_y] = "X"
            spaceEnable -= 1
            break
        else:
            print("this place is not valide")

def setIAchoice(IA_choice):
    while(spaceEnable > 0):
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
        

def IAchoice():
    if spaceEnable == 9:
        setIAchoice(random.choice(1,3,7,9))
    elif spaceEnable == 8:
        verif = setIAchoice(5)
        if verif == False:
            verif = setIAchoice(random.choice(1,3,7,9))
            while verif == False:
                setIAchoice(random.choice(1,3,7,9))
    elif spaceEnable == 7:
        verif = setIAchoice(5)
        if verif == False:
            for x in range(0,len(game)):
                for y in range(0,len(game[x])):
                    if game[x][y]=="O":
                        if(x==0)and(y==0):
                            verif = setIAchoice(random.choice(2,4))
                            while verif == False:
                                setIAchoice(random.choice(2,4))
                        elif(x==2)and(y==0):
                            verif = setIAchoice(random.choice(4,8))
                            while verif == False:
                                setIAchoice(random.choice(4,8))
                        elif(x==0)and(y==2):
                            verif = setIAchoice(random.choice(2,6))
                            while verif == False:
                                setIAchoice(random.choice(2,6))
                        elif(x==2)and(y==2):
                            verif = setIAchoice(random.choice(6,8))
                            while verif == False:
                                setIAchoice(random.choice(6,8))

    elif spaceEnable == 6:
        verif = checkClosetoWin()
        if verif!=False:
            setIAchoice(verif)
        else:
            for x in range(0,len(game)):
                for y in range(0,len(game[x])):
                    if game[x][y]=="O":
                        if(x==0)and(y==0):
                            verif = setIAchoice(random.choice(2,4))
                            while verif == False:
                                setIAchoice(random.choice(2,4))
                        elif(x==2)and(y==0):
                            verif = setIAchoice(random.choice(4,8))
                            while verif == False:
                                setIAchoice(random.choice(4,8))
                        elif(x==0)and(y==2):
                            verif = setIAchoice(random.choice(2,6))
                            while verif == False:
                                setIAchoice(random.choice(2,6))
                        elif(x==2)and(y==2):
                            verif = setIAchoice(random.choice(6,8))
                            while verif == False:
                                setIAchoice(random.choice(6,8))
                        elif(x==1)and(y==1):
                            verif = setIAchoice(random.choice(1,3,7,9))
                            while verif == False:
                                setIAchoice(random.choice(1,3,7,9))
    elif spaceEnable == 5:
        verif = checkClosetoWin()
        if verif!=False:
            setIAchoice(verif)
        elif verif == False:
            for x in range(0,len(game)):
                for y in range(0,len(game[x])):
                    if game[x][y]=="O":
                        if(x==0)and(y==0):
                            verif = setIAchoice(random.choice(2,4))
                            while verif == False:
                                setIAchoice(random.choice(2,4))
                        elif(x==2)and(y==0):
                            verif = setIAchoice(random.choice(4,8))
                            while verif == False:
                                setIAchoice(random.choice(4,8))
                        elif(x==0)and(y==2):
                            verif = setIAchoice(random.choice(2,6))
                            while verif == False:
                                setIAchoice(random.choice(2,6))
                        elif(x==2)and(y==2):
                            verif = setIAchoice(random.choice(6,8))
                            while verif == False:
                                setIAchoice(random.choice(6,8))