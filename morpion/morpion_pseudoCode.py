#importer la fonction random

#initialise la liste number vide
#ajouter la liste [1,2,3] dans la liste number
#ajouter la liste [4,5,6] dans la liste number
#ajouter la liste [7,8,9] dans la liste number

#initialise la liste game vide
#ajouter la liste ["-","-","-"] dans la liste game
#ajouter la liste ["-","-","-"] dans la liste game
#ajouter la liste ["-","-","-"] dans la liste game


#initialiser le booléen onoff a True

#initialiser la variable playercaseID_x a 0
#initialiser la variable playercaseID_y a 0

#initialiser la variable IAcaseID_x a 0
#initialiser la variable IAcaseID_y a 0

#initialiser la variable spaceEnable a 9

#assigner a first le retour de la fonction randint avec comme parametre 1 et 2

#definir la fonction playerTurn
    #initialiser la variable spaceEnable comme variable globale
    #initialiser la variable playercaseID_x comme variable globale
    #initialiser la variable playercaseID_y comme variable globale
    #assigner a playerChoice l'entier du retour de la fonction input avec comme parametre "chose a number"

    #si playerchoice n'est pas un element de la liste [1,2,3,4,5,6,7,8,9] 
        #alors afficher "you need to choose a number between 1 and 9"
        #executer la fonction playerTurn

    #else
        #pour x allant de 0 a 3
            #pour y allant de 0 a 3
                #si playerChoice est egale a l'element number d'indice [x][y]
                    #assigner playercaseID_x a x
                    #assigner playercaseID_y a y

    #si l'element game d'indice [playercaseID_x][playercaseID_y] est egale a 0
        #assigner a l'element game d'indice [playercaseID_x][playercaseID_y] "X"
        #assigner la variable spaceEnable a spaceEnable-1
    #sinon
        #afficher "this place is not valide"
        #executer la fonction playerTurn

#definir la fonction setIAchoice avec comme parametre IA_choice 
    #initialiser la variable spaceEnable comme variable globale
    #pour x allant de 0 a 3
        #pour y allant de 0 a  3
            #si IA_choice est egale a l'element number d'indice [x][y]
                #assigner IAcaseID_x a x
                #assigner IAcaseID_y a y

    #si l'element game d'indice [playercaseID_x][playercaseID_y] est egale a 0
        #assigner a l'element game d'indice [playercaseID_x][playercaseID_y] "X"
        #assigner la variable spaceEnable a spaceEnable-1
        #retourner True
    #sinon
        #retourner False



#definir la fonction checkClosetoWin
    #pour x allant de 0 a 3
        #initialiser checkIA a 0
        #pour y allant de 0 a 3
            #si l'element game d'indice [x][y] est egale a "O"
                #assigner checkIA a checkIA +1
        #si checkIA est superieur a 1
            #pour y allant de 0 a 3
                #si l'element game d'indice [x][y] est egale a "-"
                    #retourner l'element number d'indice [x][y]

    #pour y allant de 0 a 3
        #initialiser checkIA a 0
        #pour x allant de 0 a 3
            #si l'element game d'indice [x][y] est egale a "O"
                #assigner checkIA a checkIA +1
        #si checkIA est superieur a 1
            #pour y allant de 0 a 3
                #si l'element game d'indice [x][y] est egale a "-"
                    #retourner l'element number d'indice [x][y]

    #initialiser check a 0
    #si l'element game d'indice [0][0] est egale a "O"
        #alors assigner check a check +1
    #si l'element game d'indice [1][1] est egale a "O"
        #alors assigner check a check +1
    #si l'element game d'indice [2][2] est egale a "O"
        #alors assigner check a check +1
    #si check est superieur a 1
        #si l'element game d'indice [0][0] est egale a "-"
            #retourner 1
        #sinon si l'element game d'indice [1][1] est egale a "-"
            #retourner 5
        #sinon si l'element game d'indice [2][2] est egale a "-"
            #retourner 9
    #initialiser check a 0
    #si l'element game d'indice [2][0] est egale a "O"
        #alors assigner  check a check +1
    #si l'element game d'indice [1][1] est egale a "O"
        #alors assigner   check a check +1
    #si l'element game d'indice [0][2] est egale a "O"
        #alors assigner check a check +1
    #si check est superieur a 1
        #si l'element game d'indice [2][0] est egale a "-"
            #retourner 7
        #sinon si l'element game d'indice [1][1] est egale a "-"
            #retourner 5
        #sinon si l'element game d'indice [0][2] est egale a "-"
            #retourner 3
                                        

    #pour x allant de 0 a 3
        #initialiser checkJoueur a 0
        #pour y allant de 0 a 3
            #si l'element game d'indice [x][y] est egale a "X"
                #assigner checkJoueur a checkJoueur +1
        #si checkJoueur est superieur a 1
            #pour y allant de 0 a 3
                #si l'element game d'indice [x][y] est egale a "-"
                    #retourner l'element number d'indice [x][y]

    #pour y allant de 0 a 3
        #initialiser checkJoueur a 0
        #pour x allant de 0 a 3
            #si l'element game d'indice [x][y] est egale a "X"
                #assigner checkJoueur a checkJoueur +1
        #si checkJoueur est superieur a 1
            #pour y allant de 0 a 3
                #si l'element game d'indice [x][y] est egale a "-"
                    #retourner l'element number d'indice [x][y]

    #initialiser check a 0
    #si l'element game d'indice [0][0] est egale a "X"
        #alors assigner check a check +1
    #si l'element game d'indice [1][1] est egale a "X"
        #alors assigner check a check +1
    #si l'element game d'indice [2][2] est egale a "X"
        #alors assigner check a check +1
    #si check est superieur a 1
        #si l'element game d'indice [0][0] est egale a "-"
            #retourner 1
        #sinon si l'element game d'indice [1][1] est egale a "-"
            #retourner 5
        #sinon si l'element game d'indice [2][2] est egale a "-"
            #retourner 9
    #initialiser check a 0
    #si l'element game d'indice [2][0] est egale a "X"
        #alors assigner  check a check +1
    #si l'element game d'indice [1][1] est egale a "X"
        #alors assigner   check a check +1
    #si l'element game d'indice [0][2] est egale a "X"
        #alors assigner check a check +1
    #si check est superieur a 1
        #si l'element game d'indice [2][0] est egale a "-"
            #retourner 7
        #sinon si l'element game d'indice [1][1] est egale a "-"
            #retourner 5
        #sinon si l'element game d'indice [0][2] est egale a "-"
            #retourner 3

    #retourner False


#definir la fonction IAchoice()

    #si spaceEnable est egal a 9 alors
        #exucuter la fonction setIAchoice(random.choice([1,3,7,9]))

    #sinon si spaceEnable est egal a 8 alors 
        #si game[1][1] est egal a "X" alors 
            #exucuter la fonction setIAchoice(random.choice([1,3,7,9]))
        #sinon alors
            #exucuter la fonction setIAchoice(5)

    #sinon si spaceEnable est egal a 7 alors
        #definir verif a exucuter la fonction setIAchoice(5)
        #si verif est egal a False alors
            #pour x allant de 0 a 3 alors
                #pour y allant de 0 a 3 alors
                    #si game[x][y] est egal a "O" alors
                        #si x est egal a 0 et que y est egal a 0 alors
                            #definir verif a la valeur de la fonction de setIAchoice(random.choice([2,4]))
                            #tant que verif est egal a False alors
                                #difinir verif a la valeur de la fonction de setIAchoice(random.choice([2,4]))
                        #sinon si x est egal a 2 et que y est egal a 0 alors
                            #definir verif a la valeur de la fonction de setIAchoice(random.choice([4,8]))
                            #tant que verif est egal a False alors
                                #difinir verif a la valeur de la fonction de setIAchoice(random.choice([4,8]))
                        #sinon si x est egal a 0 et que y est egal a 2 alors
                            #definir verif a la valeur de la fonction de setIAchoice(random.choice([2,6]))
                            #tant que verif est egal a False alors
                                #difinir verif a la valeur de la fonction de setIAchoice(random.choice([2,6]))
                        #si x est egal a 2 et que y est egal a 2 alors
                            #definir verif a la valeur de la fonction de setIAchoice(random.choice([6,8]))
                            #tant que verif est egal a False alors
                                #difinir verif a la valeur de la fonction de setIAchoice(random.choice([6,8]))
    #sinon si spaceEnable est egal a 6 alors
        #definir verif a la valeur retouner par fonction checkCloseToWin()
        #si verif n'est pas egal a False alors 
            #difinir verif a la valeur retourner par la fontion setIAchoice(verif)
        #sinon alors
        #si game[0][0] est egal a "-" et que game[1][0] est egal a "X" et que game[0][1] est egal a "X" alors
            #appeler la fonction setIAchoice(1)
        #sinon si game[0][2] est egal a "-" et que game[0][1] est egal a "X" et que game[1][2] est egal a "X" alors
            #appeler la fonction setIAchoice(3)
        #sinon si game[2][0] est egal a "-" et que game[1][0] est egal a "X" et que game[2][1] est egal a "X" alors
            #appeler la fonction setIAchoice(7)*
        #sinon si game[2][2] est egal a "-" et que game[2][1] est egal a "X" et que game[1][2] est egal a "X" alors
            #appeler la fonction setIAchoice(9)
        #sinon si game[1][1] est egal a "O" alors
            #definir verif par la valeur retourner par la fonction setIAchoice(random.choice([2,4,6,8]))
            #tant que verif est egal a False alors
                #definir verif par la valeur retourner par la fonction setIAchoice(random.choice([2,4,6,8]))
        #sinon 
            #pour x allant de 0 a 3 alors
                #pour y allant de 0 a 3 alors
                    #si game[x][y] est egal a "O" alors
                        #si x est egal a 0 et que y est egal a 0 alors
                            #definir verif a la valeur de la fonction de setIAchoice(random.choice([2,4]))
                            #tant que verif est egal a False alors
                                #difinir verif a la valeur de la fonction de setIAchoice(random.choice([2,4]))
                        #sinon si x est egal a 2 et que y est egal a 0 alors
                            #definir verif a la valeur de la fonction de setIAchoice(random.choice([4,8]))
                            #tant que verif est egal a False alors
                                #difinir verif a la valeur de la fonction de setIAchoice(random.choice([4,8]))
                        #sinon si x est egal a 0 et que y est egal a 2 alors
                            #definir verif a la valeur de la fonction de setIAchoice(random.choice([2,6]))
                            #tant que verif est egal a False alors
                                #difinir verif a la valeur de la fonction de setIAchoice(random.choice([2,6]))
                        #si x est egal a 2 et que y est egal a 2 alors
                            #definir verif a la valeur de la fonction de setIAchoice(random.choice([6,8]))
                            #tant que verif est egal a False alors
                                #difinir verif a la valeur de la fonction de setIAchoice(random.choice([6,8]))

    #sinon si spaceEnable est egal a 5 ou 4 ou 3 ou 2 alors
        #definir verif a la valeur retourner par la fonction checkCloseToWin()
        #si verif n'est pas egal a False alors
            #definir verif a la valeur retourner de la fonction setIAchoice(verif)
        #sinon
            #definir verif a la valeur de la fonction de setIAchoice(random.choice([1,2,3,4,5,6,7,8,9]))
            #tant que verif est egal a False alors
                #difinir verif a la valeur de la fonction de setIAchoice(random.choice([1,2,3,4,5,6,7,8,9]))

    #sinon si spaceEnable est egal a 1 alors
        #pour x allant de 0 a 3 alors
            #pour y allant de 0 a 3 alors
                #si game[x][y] est egal a "-" alors
                    #appeler la fonction setIAchoice(int(number[x][y]))

#definir la fonction winCheck()
    #pour x allant de 0 a 3 alors
        #pour y allant de 0 a 3 alors
            #si game[x][y] est egal a "X" alors
                #si x est egal a 0 alors
                    #if game[x + 1][y] est egal a "X" et que game[x + 2][y] est egal a "X"
                        #retourner la valeur "win"
                #sinon si x est egal a 1 alors
                    #if game[x + 1][y] est egal a "X" et que game[x - 1][y] est egal a "X"
                        #retourner la valeur "win"
                #sinon si y est egal a 0 alors
                    #if game[x][y + 1] est egal a "X" et que game[x][y + 2] est egal a "X"
                        #retourner la valeur "win"
                #sinon si y est egal a 1 alors
                    #if game[x][y + 1] est egal a "X" et que game[x][y - 1] est egal a "X"
                        #retourner la valeur "win"

            #si game[x][y] est egal a "O" alors
                #si x est egal a 0 alors
                    #if game[x + 1][y] est egal a "O" et que game[x + 2][y] est egal a "O"
                        #retourner la valeur "lose"
                #sinon si x est egal a 1 alors
                    #if game[x + 1][y] est egal a "O" et que game[x - 1][y] est egal a "O"
                        #retourner la valeur "lose"
                #sinon si y est egal a 0 alors
                    #if game[x][y + 1] est egal a "O" et que game[x][y + 2] est egal a "O"
                        #retourner la valeur "lose"
                #sinon si y est egal a 1 alors
                    #if game[x][y + 1] est egal a "O" et que game[x][y - 1] est egal a "O"
                        #retourner la valeur "lose"

    #si game[0][0] est egal a "X" et que game[1][1] est egal a "X" et que game[2][2] est egal a "X" alors
        #retourner la valeur "win"
    #sinon si game[0][2] est egal a "X" et que game[1][1] est egal a "X" et que game[2][0] est egal a "X" alors
        #retourner la valeur "win"

    #si game[0][0] est egal a "O" et que game[1][1] est egal a "O" et que game[2][2] est egal a "O" alors
        #retourner la valeur "lose"
    #sinon si game[0][2] est egal a "O" et que game[1][1] est egal a "O" et que game[2][0] est egal a "O" alors
        #retourner la valeur "lose"

#definir la fonction relancer()
    #appeler la variable global game
    #appeler la variable global onoff
    #appeler la variable global first
    #appeler la variable global statut
    #appeler la variable global spaceEnable
    #initialiser la variable replay a la fonction fonction input("Veux tu rejouer ( oui ou non ) : ")
    #si replay est egal a "non" alors 
        #difinir onoff a False
    #sinon si replay est egal a "oui" alors
        #afficher "la partie se relance"
        #definir first a la valeur retourner par la fonction random.randint(1,2)
        #definir onoff a True
        #definir game comme une liste vide
        #ajouter a game ["-","-","-"]
        #ajouter a game ["-","-","-"]
        #ajouter a game ["-","-","-"]
        #definir statut a ""
        #definir spaceEnable a 9
        #pour i allant de 0 a 3 alors
            #afficher la jointure de number[i] avec tout ses composant transformer en string un par un a l'aide d'une boucle (print("|".join(str(e)for e in number[i]))
        #afficher "---------------"
    #sinon alors
        #afficher "erreur"
        #relancer()
    
#tant que onoff est egale a True

    #pour i allant de 0 a 3
        #afficher la jointure de number[i] avec tout ses composant transformer en string un par un a l'aide d'une boucle (print("|".join(str(e)for e in number[i]))
    #afficher "-----------------"

    #si  first est egale a 1
        #alors executer playerTurn
    #sinon si first est egale a 2
        #alors executer IAchoice
    
    #pour i allant de 0 a 3
        #afficher la jointure de game[i] avec tout ses composant transformer en string un par un a l'aide d'une boucle (print("|".join(str(e)for e in game[i]))
    #afficher "-----------------"

    #assigner a status le retour de la fonction winCheck

    #si status est egale a "win"
        #alors afficher "win"
        #executer la fonction relancer
    #sinon si status est egale a "lose"
        #alors afficher "lose"
        #executer la fonction relancer
    #sinon si spaceEnable est egale a 0
        #alors afficher "draw"
        #executer la fonction relancer

    #si first est egale a 1
        #executer la fonction IAchoice
    #sinon si first est egale a 2
        #executer la fonction playerTurn

    #pour i allant de 0 a 3
        #afficher la jointure de game[i] avec tout ses composant transformer en string un par un a l'aide d'une boucle (print("|".join(str(e)for e in game[i]))
    #afficher "-----------------"

    #assigner a status le retour de la fonction winCheck

    #si status est egale a "win"
        #alors afficher "win"
        #executer la fonction relancer
    #sinon si status est egale a "lose"
        #alors afficher "lose"
        #executer la fonction relancer
    #sinon si spaceEnable est egale a 0
        #alors afficher "draw"
        #executer la fonction relancer
        