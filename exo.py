def add(x,y):
    return(x + y)

def sub(x,y):
    return(x - y)

def multiply(x,y):
    return(x * y)

def divide(x,y):
    if y == 0:
        return("erreur")
    else:
        return(x / y)

def modulo(x,y):
    if y == 0:
        return("erreur")
    else:
        return(x % y)


def salaireSeconde(salaireHoraire, heureParJourOuvrable, nonJourOuvrable):
    salaire = (((7-nonJourOuvrable)*4)*heureParJourOuvrable)*salaireHoraire
    salaireSec = salaireHoraire/3600

def salaireNet(salaireBrut, coef):
    return(salaireBrut*(1-(coef/100)))
