# Initialisation des variables
capital = 8000 # en dollars
nb_jours = 72 # en jours
taux_annuel = 0.065# pourcentage / 100
# Calcul du taux périodique 
taux_periodique = 0.065 / (365)
# Calcul des intérêts 
interet = capital * taux_periodique * nb_jours

# Calcul de la valeur acquise
valeur_acquise = capital + interet
# Affichage des interets et de la valeur acquise 
print("Les intérêts gagnés après 72 jours sont :")
print(interet)
print("La valeur acquise après 72 jours est :")
print(valeur_acquise)