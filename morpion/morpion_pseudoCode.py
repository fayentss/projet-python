#importer de la bibliotheque random

#declarer number en tant que liste
#ajouter a number la liste (1,2,3)
#ajouter a number la liste (4,5,6)
#ajouter a number la liste (7,8,9)

#declarer game en tant que liste
#ajouter a game la liste ("-","-","-")
#ajouter a game la liste ("-","-","-")
#ajouter a game la liste ("-","-","-")

#initialiser onoff a True

#initialiser playercaseID_x a 0
#initialiser playercaseID_y a 0

#initialiser IAcaseID_x a 0
#initialiser IAcaseID_y a 0

#initialiser spaceEnable a 9

#definir la fonction wincheck
    #pour x allant de 0 a la valeur revoyer par la fonction len(number)
        #pour y allant de 0 a la valeur revoyer par la fonction len(number[x])
            #si game[x][y] est egal a "X" alors
                #si x est egal a 0 alors
                    #si game[x + 1][y] est egal a "X" et que game[x + 2][y] est egal a "X" alors
                        #retourner le text "win"

                #sinon si x est egal a 1 alors
                    #si game[x][y + 1] est egal a "X" et que [x - 1][y] est egal a "X" alors
                        #retourner le text "win"

                #sinon si y est egal a 0 alors
                    #si game[x][y + 1] est egal a "X" et que [x][y + 2] est egal a "X" alors
                        #retourner le text "win"

                #sinon y est egal a 1 alors
                    #si game[x][y + 1] est egal a "X" et que game[x][y - 1] est egal a "X" alors
                        #retourner le text "win"


            #si game[x][y] est egal a "O" alors
                #si x est egal a 0 alors
                    #si game[x + 1][y] est egal a "O" et que game[x + 2][y] est egal a "O" alors
                        #retourner le text "lose"

                #sinon si x est egal a 1 alors
                    #si game[x][y + 1] est egal a "O" et que [x - 1][y] est egal a "O" alors
                        #retourner le text "lose"

                #sinon si y est egal a 0 alors
                    #si game[x][y + 1] est egal a "O" et que [x][y + 2] est egal a "O" alors
                        #retourner le text "lose"

                #sinon y est egal a 1 alors
                    #si game[x][y + 1] est egal a "O" et que game[x][y - 1] est egal a "O" alors
                        #retourner le text "lose"

    
    #si gamegame[0][0] est egal a "X" et que game[1][1] est egal a "X" et que game[2][2] est egal a "X" alors
        #retourner le text "win"
    #sinon si gamegame[0][2] est egal a "X" et que game[1][1] est egal a "X" et que game[2][0] est egal a "X" alors
        #retourner le text "win"

    #si gamegame[0][0] est egal a "O" et que game[1][1] est egal a "O" et que game[2][2] est egal a "O" alors
        #retourner le text "lose"
    #sinon si gamegame[0][2] est egal a "O" et que game[1][1] est egal a "O" et que game[2][0] est egal a "O" alors
        #retourner le text "lose"
                

                  
#tant que onoff est egal a True alors 

    #pour i allant de 0 a la valeur retourner par la fonction len(number)
        # afficher la valeur de la jointure pour toutes les valeur de number[i] transformer en string "print("|".join(str(e)for e in number[i]))"

    #tant que spaceEnable est plus grand que 0 alors 

        #playerChoice est egale a la valeur retourner par la fonction input("un nombre entre 1 et 9") dans la fonction int

        #pour x allant de 0 a la valeur revoyer par la fonction len(number)
            #pour y allant de 0 a la valeur revoyer par la fonction len(number[x])
                #si playerChoice est egal a number[x][y] alors
                    #initialiser la variable playercaseID_x et inserer la valeur x
                    #initialiser la variable playercaseID_y et inserer la valeur y
                
        #si game[playercaseID_x][playercaseID_y] est egal a "-" alors 
            #game[playercaseID_x][playercaseID_y] est egal a "X"
            #decrementer spaceEnable de 1
            #break (quitter la boucle)
        #sinon
            #afficher "this place is not valide"

    #initialiser la variable statut au resultat de la fonction winCheck()

    #si statut est egal a "win" alors
        #pour i allant de 0 a la valeur retourner par la fonction len(number)
            #afficher la valeur de la jointure pour toutes les valeur de number[i] transformer en string "print("|".join(str(e)for e in number[i]))"
        #afficher "---------------" 
        #onoff est egal a False
        #afficher "win"
        #break
    #sinon si statut est egal a "lose" alors 
        #pour i allant de 0 a la valeur retourner par la fonction len(number)
            #afficher la valeur de la jointure pour toutes les valeur de number[i] transformer en string "print("|".join(str(e)for e in number[i]))"
        #afficher "---------------" 
        #onoff est egal a False
        #afficher "lose"
        #break
    #sinon si spaceEnable est egal  alors 
        #pour i allant de 0 a la valeur retourner par la fonction len(number)
            #afficher la valeur de la jointure pour toutes les valeur de number[i] transformer en string "print("|".join(str(e)for e in number[i]))"
        #afficher "---------------" 
        #onoff est egal a False
        #afficher "draw"
        #break

    #tant que spaceEnable est plus grand que 0 alors 

        #IAChoice est egal a la valeur retourner par la fonction random.randint(1,9)

        #pour x allant de 0 a la valeur revoyer par la fonction len(number)
            #pour y allant de 0 a la valeur revoyer par la fonction len(number[x])
                #si IAChoice est egal a number[x][y]
                    #initialiser la variable IAcaseID_x et inserer la valeur x
                    #initialiser la variable IAcaseID_y et inserer la valeur y

        #si game[IAcaseID_x][IAcaseID_y] est egal a "-" alors
            #game[IAcaseID_x][IAcaseID_y] est egal a "O"
            #decrementer spaceEnable de 1
            #break (quitter la boucle)

    #pour i allant de 0 a la valeur retourner par la fonction len(number)
        #afficher la valeur de la jointure pour toutes les valeur de number[i] transformer en string "print("|".join(str(e)for e in number[i]))"
    #afficher "---------------"

    #initialiser la variable statut au resultat de la fonction winCheck()

    #si statut est egal a "win" alors 
        #onoff est egal a False
        #afficher "win"
    #sinon si statut est egal a "lose" alors 
        #onoff est egal a False
        #afficher "lose"
    #sinon si spaceEnable est egal  alors 
        #onoff est egal a False
        #afficher "draw"
