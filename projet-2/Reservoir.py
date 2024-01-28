# -*- coding: utf-8 -*-
# Nom_du_fichier: Reservoir.py
# Creer le      : 
# Creer par     : 
# Version num   : 
# Modifier le   :
import math

import matplotlib.pyplot as plt
from IPython.display import clear_output
from Molecule import moleculesSeTouche, deplacerMolecule, creerListMolecules
from Molecule import ajusteDirApresCollision, inverseDirMolecule


def creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD):
    #TODO 3.2.1 Créer le structure de données d'un réservoir
    # Utiliser creerListMolecules (voir 3.1.5)
    list_MoleculesG= creerListMolecules(hauteur,0,posParoi,nbMoleculesG)
    list_MoleculesD=creerListMolecules(hauteur,posParoi,largeur,nbMoleculesD)

    nombre_combinaisons_distinctesG = (math.factorial(nbMoleculesG))/(2*math.factorial(nbMoleculesG-2))
    nombre_combinaisons_distinctesD = (math.factorial(nbMoleculesD))/(2*math.factorial(nbMoleculesD-2))

    list_collisionG = [0] * int(nombre_combinaisons_distinctesG)
    list_collisionD = [0] * int(nombre_combinaisons_distinctesD)

    Reservoir = {"h": hauteur, "l": largeur, "posPar": posParoi, "mG": list_MoleculesG,"mD":list_MoleculesD,"lCG": list_collisionG, "lCD": list_collisionD}
    return Reservoir
def colision(reservoir):
    #TODO 3.2.2 Vérifier si il y a des collisions entre des molécules dans un réservoir
    # Pour chaque molécule vérifier si elles est en collision avec une autre molécule du réservoir
    index = 0
    for i in range(0,len(reservoir["mG"])):
        for j in range(i+1,len(reservoir["mG"])):
            if moleculesSeTouche(reservoir["mG"][i], reservoir["mG"][j]) and reservoir["lCG"][index] ==0:
                reservoir["lCG"][index] = 1
                ajusteDirApresCollision(reservoir["mG"][i], reservoir["mG"][j])
            else:
                reservoir["lCG"][index] = 0
            index +=1
    count = 0
    for i in range(len(reservoir["mD"])):
        for j in range(i+1,len(reservoir["mD"])):
            if moleculesSeTouche(reservoir["mD"][i], reservoir["mD"][j]) and reservoir["lCD"][count] == 0:
                reservoir["lCD"][count] = 1
                ajusteDirApresCollision(reservoir["mD"][i], reservoir["mD"][j])
            else:
                reservoir["lCD"][count] = 0
            count +=1
    return reservoir

def inverseDirMolecules(reservoir):
    #TODO 3.2.3 Ajuster la direction des molécules qui touchent aux parois dans chaque réservoir
    # Faire appel à inverseDirMolecule(mol, paroiG, paroiD, hauteur) (3.2.3)
    liste_1 = []
    liste_2 = []
    for i in reservoir["mG"]:
        x = inverseDirMolecule(i,0,reservoir["posPar"],reservoir["h"])
        liste_1.append(x)
    for j in reservoir["mD"]:
        y = inverseDirMolecule(j, reservoir["posPar"], reservoir["l"], reservoir["h"])
        liste_2.append(y)
    reservoir["mG"] = liste_1
    reservoir["mD"] = liste_2
    return reservoir

def getTemperature(reservoir, cote):
    #TODO 3.2.4 Calcule la température de chaque côté du réservoir.
    # Utiliser la formule dans le Readme
    E = 0
    V = 0
    T = 0   
    if cote == "Gauche":
        N = len(reservoir["mG"])
        for i in range(N):
            V = math.sqrt(reservoir["mG"][i]["dx"] **2 + reservoir["mG"][i]["dy"]**2)
            E += (V**2)/2
        T = E/N
    elif cote == "Droite":
        N = len(reservoir["mD"])
        for i in range(N):
            V = math.sqrt(reservoir["mD"][i]["dx"]**2 + reservoir["mD"][i]["dy"]**2)
            E += (V**2)/2
        T = E / N
    return T 

#####################################################
# Donner
#####################################################
def affichage(reservoir, ax):
    txt = "Température côté Gauche: {:.2f}C \t\t\t\t\t Température côté Droit: {:.2f}C".expandtabs()

    ax.plot([reservoir['posPar'], reservoir['posPar']], [0, reservoir['h']], 'k-', linewidth=10)
    ax.axis([-20, reservoir['l'] + 20, -20, reservoir['h'] + 20])
    ax.title.set_text(txt.format(getTemperature(reservoir, "Gauche"), getTemperature(reservoir, "Droit")))

    for k in [['mG', 'ro'], ['mD', 'go']]:
        for i in range(len(reservoir[k[0]])):
            inte = min(max((abs(reservoir[k[0]][i]['dx']) + abs(reservoir[k[0]][i]['dy'])) / 60, 0.2), 1)
            ax.plot(reservoir[k[0]][i]['x'], reservoir[k[0]][i]['y'], k[1], alpha=inte, ms=reservoir[k[0]][i]['rayon'])
            reservoir[k[0]][i] = deplacerMolecule(reservoir[k[0]][i])

    plt.pause(0.01)
    clear_output() 
    

def deplacerMolecules(reservoir, ax):
    # TODO 3.2.6
    # deplacer_molecule deplace les molecules du reservoir
    # Cette function recoit comme parametre un objet de type reservoire est execute les etapes suivantes:
    # 1) Inverser la direction des molecules du reservoir
    reservoir = inverseDirMolecules(reservoir)
    # 2) Afficher les molecules
    affichage(reservoir, ax)
    # 3) Determination des colision des molecules
    reservoir = colision(reservoir)
    
    return reservoir

if __name__ == '__main__':
    hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD = 2000, 2000, 1300, 30, 30
    reservoir = creerReservoir(hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD)
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot()
    for i in range(1000):
        reservoir = deplacerMolecules(reservoir, ax)
        ax.clear()