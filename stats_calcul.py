import math

def somme(valeurs):
    return sum(valeurs)

def moyenne(valeurs):
    return sum(valeurs) / len(valeurs) if valeurs else 0

def ecart_type(valeurs):
    if len(valeurs) < 2:
        return 0
    moy = moyenne(valeurs)
    variance = sum((x - moy) ** 2 for x in valeurs) / len(valeurs)
    return math.sqrt(variance)
def mediane(valeurs):
    n = len(valeurs)
    valeurs.sort()
    if n % 2 == 0:
        return (valeurs[n//2 - 1] + valeurs[n//2]) / 2
    else:
        return valeurs[n//2]