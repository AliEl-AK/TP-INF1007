# Initialisation des variables
from typing import Union, Any
capital_init = 2600
nb_jours = ''
capital_init2=(capital_init-60)
taux_journalier1=capital_init * 4.5/(365*100)
taux_journalier2=((capital_init2) * 10/(365*100))
# Calcul du montant du capital avec le premier placement au 100ème jour de l'année
nb_jours = 100
capital1 = (capital_init + (taux_journalier1) * nb_jours)
# Calcul du montant du capital avec le deuxième placement au 300ème jour de l'année
nb_jours = 300
capital2 = (capital_init2 + taux_journalier2 * nb_jours)
# /!\ AVEC UNE BOUCLE/!\ Calcul du jour à partir duquel le deuxième placement rapporte plus que le premier
#shoutout to w3schools.
x = range(365)
for n in x:
    capital_1 = (capital_init + (taux_journalier1) * n)
    capital_2 = ((capital_init2) + taux_journalier2 * n)
    if capital_1 > capital_2:
        pass
    else:
        break
#Affichage des résultats:
print("Montant du capital avec la premier placemnet au 100ème jour:")
print(capital1)
print("Montant du capital avec la deuxième placement au 300ème jour:")
print(capital2)
print("Jour à partir duquel le deuxième placement rapporte plus que le premier:")
print(n)
