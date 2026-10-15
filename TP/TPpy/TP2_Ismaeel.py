'''
#Exercice 1.1: La valeur est 74,6
ma_variable = 25
ma_variable = 74.6
print(ma_variable)

#Exercice 1.2: La valeur est Hello World !
ma_variable = "Hello World !"
Ma_variable = 15
print(ma_variable)

#Exercice 1.3: La valeur est 98
ma_variable = 14
autre_variable = 98
ma_variable = autre_variable
print(ma_variable)

#Exercice 1.4: La valeur est 2
ma_variable = 2
variable = 6
variable = 6 + ma_variable
print(ma_variable) 

#Exercice 1.5: La valeur est 26
ma_variable = 22
ma_variable += 4
print(ma_variable)

#Exercice 1.6: La valeur est 12
ma_variable = 6
ma_variable *= 2
print(ma_variable)

#Exercice 1.7: Il ya une erreur car il faut mettre la barre avant le =
ma_variable = 33
ma_variable =/ 3
print(ma_variable)

#Exercice 1.8 La valeur est Bonjour
ma_variable, autre_variable = "Bonjour", "Hello"
print(ma_variable)

#Exercice 2:
prenom = input("Entrer votre prénom :")
print("Bonjour", prenom, "!")

#Exercice 3.1: Il ya une erreur, si on saisit 18,  Python considère : age = 18 et non pas age = 18+2
age = input("Saisir votre âge :")
print(age + 2)

#Exercice 3.2: Si on saisit 18 On obtient 182 car c'est une succesion de nombres
age = input("Saisir votre âge :")
print(age + "2")

#Exercice 3.3: Si on saisi 18 On obtient 1818 car c'est un caractère répété deux fois
age = input("Saisir votre âge :")
print(age * 2)

#Exercice 4: La valeur est 18 ans
annee_naissance = int(input("Saisir votre année de naissance : "))
annee_actuelle = int(input("Saisir année actuelle : "))
age = annee_actuelle - annee_naissance
print("C'était il y a", age, "années.")

#Exercice 5: En utiliasnt comme nombre 10, on trouve 1024 car 2 puissance 10
nombre = int(input("Saisir un nombre entier : "))
resultat = 2 ** nombre
print("2 puissance", nombre, "=", resultat)

#Exercice 6:
cote = float(input("Saisir la longueur du côté : "))
perimetre = cote * 4
aire = cote * cote
print("Un carré de", cote, "cm de côté a pour périmètre", perimetre, "cm et pour aire", aire, "cm².")

#Exercice 8.1: 5.4 est un texte et il est multiplié par 3 donc on trouve 5.45.45.4
print(str(5.4) * 3)

#Exercice 8.2: On doit seulement additionner les nombres entre eux
print(int("8") + float("9.8"))

#Exercice 8.3: int nombre entier donc 7 et on répète ça 7 fois le nombre 5 donc 5555555
print(str(5) * int(7.6))

#Exercice 8.4: Il ya une erreur car on ne peut pas multiplier une chaine de caractères avec un nombre décimale
print(str(6) * float("4.8"))

#Exercice 9.1: La réponse est 0
test_list = []
print(len(test_list))

#Exercice 9.2: La réponse est 3
test_list = [1, 2, 3]
print(len(test_list))
'''
#Exercice 9.3: La réponse est 3
test_tuple = (1, 2, 3)
print(len(test_tuple))


