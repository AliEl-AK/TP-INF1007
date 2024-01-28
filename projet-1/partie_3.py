# Initilisation des variables
capital_0=300000
taux_interet= 8/100
Cn = []
Cn= [capital_0 + (capital_0 * taux_interet)]
Cn=[Cn[0],[]]
# Calcul du capital au bout de 20 années
for i in range(1,20):
    Cn[i]=Cn[i-1] + (Cn[i-1]* taux_interet)
    Cn.append(Cn[i])
#Affichage du capital au bout de 20 années
print("Capital au bout de 20 années:", Cn[20])