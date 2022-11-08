def add(x,y):
    return(x + y)

def sub(x,y):
    return(x - y)

def multiply(x,y):
    return(x * y)

def divide(x,y):
    if y == 0:
        print("error")
        return(None)
    else:
        return(x / y)

def modulo(x,y):
    if y == 0:
        print("error")
        return(None)
    else:
        return(x % y)

def salaireSeconde(salaireHoraire, heureParJourOuvrable, jourOuvrable):
    #Assigner a salaireAnnuel le salaire gagner par an
    salaireAnnuel = salaireHoraire * heureParJourOuvrable * jourOuvrable
    #Calculer, puis assigner a nbSecondeParAn, le nombre de seconde dans une année non-bisextile
    nbSecondeParAn = 60 * 60 * 24 * 365
    #Retourner le salaire Annuel divisé par le nombre de seconde par an
    return(salaireAnnuel * nbSecondeParAn)

def salaireNet(salaireBrut, taxe, public):
    #Calculer, puis assigner le coefficient multiplicateur
    if (public):
        taxe-=15    
    coeffMultiplicateur = 1-(taxe/100)
    #Retourner le salaire brut multiplier par le coeffmultiplicateur
    return(salaireBrut*coeffMultiplicateur)



def jeux(lettreSouhaiter):
    #demander une lettre et assigner a y
    lettreAleatoire = str(input("donne une lettre : "))
    #repeter tant que la lettre n'est pas celle demander
    while (lettreSouhaiter != lettreAleatoire):
        print("se n'est pas ça !")
        #demander une nouvelle lettre et assigner a y
        lettreAleatoire = str(input("donne une lettre : "))     
    print("bien jouer tu as trouver")


#exercice 1:
#faire une fonction qui concatene 2 chaines de caractere, les separants par une virgule 
def exoUn(chaine1, chaine2):
    return(chaine1+", "+chaine2)


#exercice 2:
#faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere
#avec l'ensemble des occurences d'un chiffre e.g.:
#pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau, 0) renvoyer "0, 4, 7" n'hesitez pas a implementer la premiere fonction
def exoDeux(liste, valeurVoulu):
    