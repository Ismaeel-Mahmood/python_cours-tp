# EXERCICE 1:
'''
fruits = ['pomme', 'banane', 'orange']
fruits[1] = 'fraise'
print(fruits[0])
print(fruits[-1])
'''
# EXERCICE 2:
'''
membres = ['Alice', 'Bob', 'Charlie']
nom = input("Entrez un nom : ")
if nom in membres:
    print('Présent')
else:
    print('Absent')
'''
# EXERCICE 3:
'''
panier = ['Livre', 'Stylo']
if len(panier) < 3:
    article = input("Article à ajouter : ")
    panier.append(article)
else:
    print('Panier plein')
print(panier)
'''
# EXERCICE 4:
'''
nombres = [42, 12, 89, 7, 23]
nombres.sort()
nombres.reverse()
print(nombres)
'''
# EXERCICE 5:
'''
notes = [12, 5, 18, 15, 9]
notes.remove(min(notes))
notes.remove(max(notes))
moyenne = sum(notes) / len(notes)
print(moyenne)
'''
# EXERCICE 6:
'''
chiffres = [1, 2, 3, 4, 5, 6, 7, 8]
resultat = chiffres[4:] + chiffres[:4]
print(resultat)
'''
# EXERCICE 7:
'''
serveur = ['Prod-01', 8080, 'ACTIF', 85]
if serveur[3] > 80:
    serveur[2] = 'ALERTE'
print(serveur)
'''
# EXERCICE 8:
'''
codes = [101, 202, 101, 303, 202, 404]
codes = sorted(set(codes))
print(codes)
'''
# EXERCICE 9:
'''
valeurs = ['A', 'B', 'C', 'D', 'E']
k = 2
valeurs = valeurs[-k:] + valeurs[:-k]
print(valeurs)
'''
# EXERCICE 10:
'''
sequence = [1, 2, 3, 3, 2, 1]
est_palindrome = sequence == sequence[::-1]
moities_identiques = sequence[:3] == sequence[3:]

if est_palindrome and moities_identiques:
    print("Palindrome et moitiés identiques")
elif est_palindrome:
    print("Palindrome, mais moitiés différentes")
elif moities_identiques:
    print("Moitiés identiques, mais pas palindrome")
else:
    print("Ni palindrome, ni moitiés identiques")
'''