number=[]
number.append([1,2,3])
number.append([4,5,6])
number.append([7,8,9])

game=[]
game.append([0,0,0])
game.append([0,0,0])
game.append([0,0,0])

for i in range(0, len(number)):
        print("|".join(str(e)for e in number[i]))







for i in range(0, len(number)):
    print("|".join(str(e)for e in game[i]))
print("-----------------")