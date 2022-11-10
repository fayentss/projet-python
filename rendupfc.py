#initialiser scoreJoueur a 0
#initialiser scoreIA a 0

#definition d'une fonction round:
    #si IA est egal a 1 alors:
        #si Joueur est egal a 1 alors
            #retourner "draw"
        #sinon si Joueur est egal a 2 alors
            #retourner "win"
        #sinon si Joueur est egal a 3 alors
            #retourner "lose"
        #sinon alors 
            #retourner "error"

    #sinon si IA est egal a 2 alors:
        #si Joueur est egal a 1 alors
            #retourner "lose"
        #sinon si Joueur est egal a 2 alors
            #retourner "draw"
        #sinon si Joueur est egal a 3 alors
            #retourner "win"
        #sinon alors 
            #retourner "error"

    #sinon si IA est egal a 3 alors:
        #si Joueur est egal a 1 alors
            #retourner "win"
        #sinon si Joueur est egal a 2 alors
            #retourner "lose"
        #sinon si Joueur est egal a 3 alors
            #retourner "draw"
        #sinon alors 
            #retourner "error"
    
    #sinon alors
        #retourner "error"


#tant que scoreIA est plus petit que 5 et que scoreJoueur est plus petit que 5 alors
    #initialiser IA puis assigner la valeur retourner par la fonction random(1,3) (retourne une valeur aletoire entre 1 et 3)
    #initialiser Joueur puis assigner la valeur retourner la fonction input (attention la valeur doit etre 1, 2 ou 3)
    #initialiser scoreRound puis assigner le resultat retourner par la fonction round()

    #si Joueur est egal a 1 alors
        #afficher "Joueur : Pierre"
    #sinon si Joueur est egal a 2 alors
        #afficher "Joueur : Papier"
    #sinon si Joueur est egal a 3 alors
        #afficher "Joueur : Ciseaux"
    #sinon alors
        #afficher "error"

    #si IA est egal a 1 alors
        #afficher "IA : Pierre"
    #sinon si IA est egal a 2 alors
        #afficher "IA : Papier"
    #sinon si IA est egal a 3 alors
        #afficher "IA : Ciseaux"
    #sinon alors
        #afficher "error"

    #si scoreRound est egal a "win" alors
        #incremeter scoreJoueur de 1
        #afficher "round result : win"
    #sinon si scoreRound est egal a "lose" alors
        #incremeter scoreIA de 1
        #afficher "round result : lose"
    #sinon si scoreRound est egal a "draw" alors
        #afficher "round result : draw"
    #sinon si scoreRound est egal a "error" alors
        #afficher "round result : error"

    #afficher le valeur de scoreIA et de scoreJoueur

#si scoreIA est egal a 5 alors
    #afficher "le grand vainceur est l'IA"
#sinon si scoreJoueur est egal a 5 alors
    #afficher "le grand vainceur est le Joueur"
        