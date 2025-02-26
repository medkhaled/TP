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