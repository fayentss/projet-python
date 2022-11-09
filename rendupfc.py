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
    #initialiser IA puis assigner la valeur retourner par random(1,3)
        