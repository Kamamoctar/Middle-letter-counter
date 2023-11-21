def leconteur():
    laLettre = input("Insérez la lettre : ")
    leText = input("Insérez le texte : ")
    counter = 0

    if len(laLettre) == 1 and laLettre.isalpha():
        lesMots = leText.split()
        for mot in lesMots:
            if len(mot) >= 3 and laLettre in mot[1:-1] and (mot[0] not in ["'", " "] and mot[-1] not in ["'", " "]):
                counter += 1
    return counter

print(leconteur())
