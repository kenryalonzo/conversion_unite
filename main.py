def conversion_pouces_vers_cm():
    entrer_str = input("quelles est donc la valur à convertir en cm\n")
    try:
        value = float(entrer_str)
    except:
        print("ERREUR: entrez une valeur valide")
    result = value * 2.54
    print(f"La conversion de {value}pouces -> {result}cm")

def conversion_cm_vers_pouce():
    user_str = input("quelles est donc la valur à convertir en pouce\n")
    try:
        valeur = float(user_str)
    except:
        print("ERREUR: entrez une valeur valide")
    resultat = valeur * 0.394
    print(f"La conversion de {valeur}cm -> {resultat}pouces")


def poser_question():
    choix_int = 0
    while choix_int == 0:
        choix_str = input("Quelle conversion voulez vous effectuez : \n1- pouces vers cm\n2- cm vers pouces\n")
        try:
            choix_int = int(choix_str)
        except:
            print("ERREUR: Vous devez enter un chiffre")
    return choix_int

choix = poser_question()

while True:
    if 0 < choix < 3:
        if choix == 1:
            print("Très bien, vous avez choisi la conversion de pouce à cm\n")
            conversion_pouces_vers_cm()
        elif choix == 2:
            print("Très bien, vous avez choisi la conversion de cm à pouce\n")
            conversion_cm_vers_pouce()
        break
    else:
        print("Vous n'avez que deux choix possibles : 1 et 2. Veuillez Réessayer.")
        choix = poser_question()