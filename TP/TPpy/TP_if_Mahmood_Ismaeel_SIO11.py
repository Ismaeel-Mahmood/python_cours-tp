

# CODE PIN : J'ai utilisé if et else car on cherche 4567.
# Si code pin vaut 4567 il est correcte sinon il est incorrecte.

pin = input("Entrer le code PIN : ")
if pin == "4567":
    print("code correct")
else:
    print("code incorrect")



# SIGNE D'UN NOMBRE : j'ai utilisé if elif et else car il ya 3 propositions
# Si nombre est supérieur à 0 il est positif, si il est inférieur à 0 il est négatif, si il est égal à 0 il est nul.

nombre = int(input("Saisir un nombre entier : "))
if nombre > 0:
    print("Positif")
elif nombre < 0:
    print("Négatif")
else:
    print("Nul")



# PARITE : Il ya 2 propositions soit pair soit impair.
# J'ai utilisé % 2 pour qu'il soit pair.

nombre = int(input("Saisir un nombre entier : "))
if nombre % 2 == 0:
    print(nombre, "est un nombre pair")
else:
    print(nombre, "est un nombre impair")



# AGE : Il ya 3 propositions, enfant, adolescent, adulte donc on utilise if, elif, else.
# Si l'age est inférieur à 12 c'est un enfant, si il est inférieur à 18 c'est un ado et sinon c'est un adulte.

age = int(input("Entrer votre âge : "))
if age < 12:
    print("A", age, "ans, vous êtes un enfant.")
elif age < 18:
    print("A", age, "ans, vous êtes un adolescent.")
else:
    print("A", age, "ans, vous êtes un adulte.")



# PERTE OU PROFIT : Il ya 3 propositions, profit, perte, ni perte ni profit. Donc on utilise if, elif, else.
# Si le prix de vente est supérieur au prix de fabrication alors il ya un profit, si prix le prix de vente est inférieur au prix de fabrication alors c'est une perte, sion ni perte ni profit

prix_fabrication = float(input("Prix de fabrication : "))
prix_vente = float(input("Prix de vente : "))
if prix_vente > prix_fabrication:
    print("profit")
elif prix_vente < prix_fabrication:
    print("perte")
else:
    print("ni perte ni profit")



# MAXIMUM : Il ya 3 propositions nombre1, nombre2, nombre3 donc if, elif, else.
# nombre1 est plus grand que le nombre2 et nombre3, nombre2 est plus grand que nombre1 et nombre3, sinon nombre3 est plus grand que le nombre1 et nombre2.

nombre1 = float(input("Saisir le premier nombre : "))
nombre2 = float(input("Saisir le second nombre : "))
nombre3 = float(input("Saisir le troisième nombre : "))

if nombre1 >= nombre2 and nombre1 >= nombre3:
    print("Le maximum est le premier nombre", nombre1)
elif nombre2 >= nombre1 and nombre2 >= nombre3:
    print("Le maximum est le second nombre", nombre2)
else:
    print("Le maximum est le troisième nombre", nombre3)



# TRIANGLE RECTANGLE :
# Comme les cotés sont obligatoirement donnés du plus petit au plus grand, cote3 est un hypoténuse
cote1 = float(input("côté 1 : "))
cote2 = float(input("côté 2 : "))
cote3 = float(input("côté 3 : "))

if cote1 > cote2 or cote2 > cote3:
    print("Les longueurs des côtés n’ont pas été saisies dans l’ordre croissant.")
elif cote3 ** 2 == cote1 ** 2 + cote2 ** 2:
    print("triangle rectangle")
else:
    print("triangle non rectangle")



# ANNEE BISSEXTILE:
#Une année est bissextile si elle est divisible par 4 et pas par 100 ; ou elle est divisible par 400.

annee = int(input("Saisir l'année : "))

if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print("Année bissextile")
else:
    print("Année non bissextile")



# SOCIETE DE TRANSPORT :
# Le tarif normal est de 10 euros, entre 16 à 21 ans il ya une reduction de 40%. J'ai 18 ans donc je dois payer 6 euros.
age = int(input("Saisir votre âge : "))

if age <= 5:
    prix = 0
elif age < 16:
    prix = 5
elif age <= 21:
    prix = 6
elif age <= 50:
    prix = 10
else:
    prix = 9

print("Le prix du transport est de", prix, "euros.")


# VOYAGE SCOLAIRE :
# On doit calculer le prix par élève qui est égal au transport + nourriture + hébergement.
# Le transport dépend du nombre d'élèves, tandis que la nourriture et l'hébergement dépendent du nombre de jours.
eleves = int(input("Nombre d'élèves : "))
jours = int(input("Durée du voyage en jours : "))

if eleves <= 25:
    transport = 110
else:
    transport = 100

nourriture = 3.50 * jours

if eleves < 20:
    hebergement = 4.20 * jours
elif eleves <= 35:
    hebergement = 3.80 * jours
else:
    hebergement = 4.00 * jours

prix = transport + nourriture + hebergement

print("Le prix du voyage revient à", prix, "euros à par élève.")



# VINCI LOCATION :
vehicule = input("Type du véhicule : ")
carburant = input("Carburant : ")
duree = int(input("Duree de location en jour : "))
distance = float(input("Distance en km : "))
offre = input("Offre commerciale : ")

# Prix de location par jour
if vehicule == "Citadine":
    prix_jour = 0  # remplacer par le prix de l'annexe
elif vehicule == "Berline":
    prix_jour = 0  # remplacer par le prix de l'annexe
elif vehicule == "Sportive":
    prix_jour = 0  # remplacer par le prix de l'annexe

# Prix du carburant par km
if carburant == "Diesel":
    prix_km = 0  # remplacer par le prix de l'annexe
elif carburant == "Essence":
    prix_km = 0  # remplacer par le prix de l'annexe

location = prix_jour * duree
consommation = prix_km * distance

total = location + consommation

if offre == "True":
    total = total * 0.90 + 30

print("Le prix total de la location est de", total, "euros.")



# NATATION:
# Je demande d’abord le nombre de séances avec input. Ensuite, je calcule le prix du tarif A en ajoutant l’abonnement annuel de 145 euros avec les prix des séances. 
# Pour le tarif B, je multiplie le nombre de séances par 15,50 euros. Ensuite, j’utilise if, elif, else pour comparer les deux tarifs et déterminer lequel est le meilleur.
# Enfin, j'écris le nombre de séance, il marque les deux montants et je les affiche seulement si je répond yes.

seances = int(input("Nombre de séances : "))
tarif_a = 145 + seances * 10.50
tarif_b = seances * 15.50

if tarif_a < tarif_b:
    print("Pour faire les séances, le tarif A est le plus avantageux.")
elif tarif_b < tarif_a:
    print("Pour faire les séances, le tarif B est le plus avantageux.")
else:
    print("Pour faire les séances, aucun tarif n'est plus avantageux que l'autre.")

details = input("Souhaitez-vous plus de détails? (yes/no) : ")

if details == "yes":
    print("Tarif A : {tarif_a} euros")
    print("Tarif B : {tarif_b} euros")



# VOYELLE, CONSONNE OU CARACTERE SPECIALE:
#J'ecris un caractère, je vérifie d’abord si ce n’est pas une lettre avec isalpha(). 
# Si ce n’est pas une lettre, c’est donc un caractère spécial. Sinon je vérifie si le caractère fait partie des voyelles a,e,i,o,u,y. 
# J’utilise  le mot lower() pour pouvoir accepter les majuscules et les minuscules. Si ce n’est pas une voyelle, alors c’est une consonne.



caractere = input("Saisir un caractère : ")
if not caractere.isalpha():
    print("{caractere} : caractère spécial")
elif caractere.lower() in "aeiouy":
    print("{caractere} : voyelle")
else:
    print("{caractere} : consonne")


# FACTURE:
# Je demande le prix hors taxe. Je calcule le prix TTC en faisant une TVA de 19,6 %. 
# Après, je regarde le montant du prix TTC pour savoir quel pourcentage de remise appliquer.
# Il ya plusieur proposition ducoup j'utilise if, elif et else parce que le taux de remise dépend de plusieurs tranches de prix. Enfin, je calcule le montant de la remise puis le prix net à payer. 
# J’utilise .2f pour afficher deux chiffres après la virgule.


ht = float(input("Saisir le prix hors taxe : "))
tva = 19.6
ttc = ht * (1 + tva / 100)

if ttc < 1000:
    taux_remise = 0
elif ttc < 2000:
    taux_remise = 1
elif ttc < 5000:
    taux_remise = 3
else:
    taux_remise = 5

remise = ttc * taux_remise / 100
net_a_payer = ttc - remise

print(f"Prix HT : {ht:.2f} euros")
print(f"Prix TTC : {ttc:.2f} euros")
print(f"Remise : {remise:.2f} euros")
print(f"Prix Net à payer : {net_a_payer:.2f} euros")


# CALCULATRICE :
# Je demande deux nombres. 
# Ensuite, je teste l’opération avec plusieurs if et elif. Pour chaque opération, je fais le bon calcul.
# Pour la division, je vérifie si le deuxième nombre est égal à zéro, car une division par zéro est impossible. 
# Si l’opération saisie ne correspond à aucune des quatre opérations proposées, j’affiche un message comme quoi l’opération n’est pas valide. »


nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
operation = input("Entrez l'opération (addition, soustraction, multiplication, division) : ")

if operation == "addition":
    resultat = nombre1 + nombre2
    print(f"> {nombre1} + {nombre2} = {resultat}")

elif operation == "soustraction":
    resultat = nombre1 - nombre2
    print(f"> {nombre1} - {nombre2} = {resultat}")

elif operation == "multiplication":
    resultat = nombre1 * nombre2
    print(f"> {nombre1} * {nombre2} = {resultat}")

elif operation == "division":
    if nombre2 == 0:
        print("> Erreur : Division par zéro !")
    else:
        resultat = nombre1 / nombre2
        print(f"> {nombre1} / {nombre2} = {resultat:.2f}")

else:
    print("> Opération non valide.")



# IMPOTS :
# Je demande le revenu annuel de l’utilisateur. Ensuite, je vérifie dans quelle tranche de revenus il se trouve. 
# Comme l’énoncé précise que l’impôt doit être calculé par tranche, je ne taxe pas tout le revenu avec le même pourcentage. 
# Par exemple, pour un revenu supérieur à 25 000 euros, je calcule d’abord les 10 % sur la première tranche, puis les 15 % sur la partie supérieure à 25 000 euros. 
# Pour un revenu supérieur à 50 000 euros, j’ajoute également les 20 % sur la dernière tranche.

revenu = float(input("Entrez votre revenu annuel : "))
if revenu <= 10000:
    impot = 0

elif revenu <= 25000:
    impot = (revenu - 10000) * 0.10

elif revenu <= 50000:
    impot = (25000 - 10000) * 0.10
    impot += (revenu - 25000) * 0.15

else:
    impot = (25000 - 10000) * 0.10
    impot += (50000 - 25000) * 0.15
    impot += (revenu - 50000) * 0.20

print(f"> L'impôt à payer est de {impot} €.")


# NATURE D'UN TRIANGLE : 
# Je demande les longueurs des trois côtés. 
# Je vérifie d’abord que les longueurs peuvent réellement former un triangle. Pour cela, la somme de deux côtés doit être supérieure au troisième côté. 
# Si cette condition n’est pas respectée, le triangle n’est pas valide. Ensuite, si les trois côtés sont égaux, c’est un triangle équilatéral. 
# Si deux côtés sont égaux, c’est un triangle isocèle. Sinon, les trois côtés sont différents et le triangle est scalène.

a = float(input("Entrez la longueur du premier côté : "))
b = float(input("Entrez la longueur du deuxième côté : "))
c = float(input("Entrez la longueur du troisième côté : "))

if a <= 0 or b <= 0 or c <= 0:
    print("> Les longueurs fournies ne forment pas un triangle valide.")

elif a + b <= c or a + c <= b or b + c <= a:
    print("> Les longueurs fournies ne forment pas un triangle valide.")

elif a == b and b == c:
    print("> C'est un triangle équilatéral.")

elif a == b or a == c or b == c:
    print("> C'est un triangle isocèle.")

else:
    print("> C'est un triangle scalène.")



# SALAIRE NET:

salaire_base = float(input("Entrez le salaire de base de l'employé : "))
ventes = int(input("Entrez le nombre de ventes réalisées par l'employé : "))
anciennete = int(input("Entrez le nombre d'années travaillées (ancienneté) : "))
cadre = input("L'employé est-il un cadre ? (True/False) : ")

# Prime de performance
if ventes > 100:
    prime_performance = salaire_base * 0.10
else:
    prime_performance = 0

# Prime d'ancienneté
if anciennete > 10:
    prime_anciennete = salaire_base * 0.10
elif anciennete >= 5:
    prime_anciennete = salaire_base * 0.05
else:
    prime_anciennete = 0

# Prime de responsabilité
if cadre == "True":
    prime_responsabilite = salaire_base * 0.05
else:
    prime_responsabilite = 0

# Salaire brut
salaire_brut = (
    salaire_base
    + prime_performance
    + prime_anciennete
    + prime_responsabilite
)

# Taxes
if salaire_brut < 2000:
    taux_taxes = 0.20
elif salaire_brut <= 5000:
    taux_taxes = 0.30
else:
    taux_taxes = 0.40

taxes = salaire_brut * taux_taxes
salaire_net = salaire_brut - taxes

print(f"> Salaire de base : {salaire_base:.2f} €")
print(f"Prime de performance : {prime_performance:.2f} €")
print(f"Prime d'ancienneté : {prime_anciennete:.2f} €")
print(f"Prime de responsabilité : {prime_responsabilite:.2f} €")
print(f"Salaire brut : {salaire_brut:.2f} €")
print(f"Montant des taxes : {taxes:.2f} €")
print(f"Salaire net : {salaire_net:.2f} €")


# MOT DE PASSE :
#Je demande le mot de passe puis je vérifie chaque critère un par un. 
# Je vérifie d’abord qu’il contient au moins 8 caractères avec len(). Ensuite, j’utilise le module re pour rechercher une majuscule, un chiffre et un caractère spécial. 
# J’utilise une variable valide qui vaut True au départ. Si un critère n’est pas respecté, je l’affiche et je passe valide à False.
#  À la fin, si tous les critères sont respectés, le mot de passe est valide, sinon il est invalide. »

import re
mot_de_passe = input("Entrez un mot de passe : ")

valide = True

if len(mot_de_passe) < 8:
    print("> Le mot de passe doit contenir au moins 8 caractères.")
    valide = False

if not re.search("[A-Z]", mot_de_passe):
    print("> Le mot de passe doit contenir au moins une majuscule.")
    valide = False

if not re.search("[0-9]", mot_de_passe):
    print("> Le mot de passe doit contenir au moins un chiffre.")
    valide = False

if not re.search("[@#!$%&*]", mot_de_passe):
    print("> Le mot de passe doit contenir au moins un caractère spécial (@,#,!,$,%,&,*).")
    valide = False

if valide:
    print("> Mot de passe valide.")
else:
    print("> Mot de passe invalide.")



