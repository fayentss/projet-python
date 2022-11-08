import random
scoreJoueur = 0
scoreAI = 0

#comparer IA et Joueur pour determiné les resultats du round
def round():
    #pour IA = pierre
    if (AI == 1):
        if (joueur==1):
            return("draw")
        elif (joueur==2):
            return("win")
        elif (joueur ==3):
           return("lose")
        else:
            return("error")
    #pour IA = papier
    elif (AI == 2):
        if (joueur==1):
            return("lose")
        elif (joueur==2):
            return("draw")
        elif (joueur ==3):
            return("win")
        else:
            return("error")
    #pour IA = ciseaux
    elif (AI == 3):
        if (joueur==1):
            return("win")
        elif (joueur==2):
            return("lose")
        elif (joueur ==3):
            return("draw")
        else:
            return("error")
    #pour IA = error 
    else:
        return("error")

#relancer un nouveau round jusqu'a se que quelqu'un soit a 5
while((scoreAI < 5)and(scoreJoueur < 5)):
    #chois IA
    AI = random.randint(1,3)
    #chois joueur
    joueur = int(input("pierre(1),papier(2),ciseaux(3) : "))
    #assigner resultat du round a une variable
    scoreRound = round()

    #afficher chois joueur
    if (joueur==1):
        print("Joueur : Pierre")
    elif (joueur==2):
        print("Joueur : Papier")
    elif (joueur ==3):
        print("Joueur : Ciseaux")
    else:
        print("error")
    #afficher chois IA
    if (AI==1):
        print("AI : Pierre")
    elif (AI==2):
        print("AI : Papier")
    elif (AI ==3):
        print("AI : Ciseaux")
    else:
        print("error")

    #mettre a jour puis afficher : round gagner
    if (scoreRound == "win"):
        scoreJoueur += 1 
        print("round result : win")
    #mettre a jour puis afficher : round perdu
    elif (scoreRound == "lose"):
        scoreAI += 1
        print("round result : lose")
    #afficher : round gagner
    elif (scoreRound == "draw"):
        print("round result : draw")
    #afficher : round error
    elif (scoreRound == "error"):
        print("round result : error")

    #afficher les scores actuels
    print ("score : AI = "+str(scoreAI)+" / Player = "+str(scoreJoueur))

#afficher le gagnant final en fonction du score
if (scoreAI == 5):
    print("le grand vainceur est l'IA")

elif(scoreJoueur == 5):
    print("le grand vainceur est le Joueur")