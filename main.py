from stats_calcul import somme, moyenne, ecart_type1
def main():
    valeurs = []
    for i in range(10):
        valeur = float(input(f"Entrez la valeur {i+1}: "))
        valeurs.append(valeur)
    
    print(f"Somme: {somme(valeurs)}")
    print(f"Moyenne: {moyenne(valeurs)}")
    print(f"Écart-type: {ecart_type(valeurs)}")

if __name__ == "__main__":
    main()