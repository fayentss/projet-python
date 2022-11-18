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

                if(y==0):
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
        return("win")
    elif((game[0][2]=="O")and(game[1][1]=="O")and(game[2][0]=="O")):
        return("win")

                  
                

while(onoff==True):

    for i in range(0, len(number)):
        print("|".join(str(e)for e in number[i]))


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

    statut = winCheck()
        
    if(statut=="win"):
        for i in range(0, len(number)):
            print("|".join(str(e)for e in game[i]))
        print("-----------------")
        onoff = False
        print("win")
        break
    elif(statut=="lose"):
        for i in range(0, len(number)):
            print("|".join(str(e)for e in game[i]))
        print("-----------------")
        onoff = False
        print("lose")
        break
    elif(spaceEnable==0):
        for i in range(0, len(number)):
            print("|".join(str(e)for e in game[i]))
        print("-----------------")
        onoff = False
        print("draw")
        break

    while(spaceEnable > 0): 

        IAChoice = random.randint(1,9)


        for x in range(0,len(number)):
            for y in range(0,len(number[x])):
                if(IAChoice == number[x][y]):
                    IAcaseID_x = x
                    IAcaseID_y = y
        
        if(game[IAcaseID_x][IAcaseID_y]=="-"):
            game[IAcaseID_x][IAcaseID_y] = "O"
            spaceEnable -= 1
            break


    for i in range(0, len(number)):
        print("|".join(str(e)for e in game[i]))
    print("-----------------")

    statut = winCheck()
    
    if(statut=="win"):
        onoff = False
        print("win")
    elif(statut=="lose"):
        onoff = False
        print("lose")
    elif(spaceEnable==0):
        onoff = False
        print("draw")
