from typing import List

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from constantes import DELTA_V_MINIMUM_PAR_CORPS_CELESTE, CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS
from fichiers_pieces import charger_capsules_df, charger_moteurs_df, charger_reservoirs_df
from fusee import Fusee, Capsule, Reservoir, Moteur


def creer_capsules(capsules_df: pd.DataFrame) -> List[Capsule]:
    # TODO Transformez le dataframe des capsules en liste d'objets de type Capsule
    liste_capsule = []
    for row in capsules_df.to_dict(orient="records"):
        capsule = Capsule(row["nom"], row["hauteur"],row["masse"], row["prix"],row["places"])
        liste_capsule.append(capsule)
    return liste_capsule

def creer_moteurs(moteurs_df: pd.DataFrame) -> List[Moteur]:
    # TODO Transformez le dataframe des moteurs en liste d'objets de type Moteur
    liste_moteur = []
    for row in moteurs_df.to_dict(orient="records"):
        moteur = Moteur(row["nom"], row["hauteur"],row["masse"], row["prix"],row["impulsion specifique"])
        liste_moteur.append(moteur)
    return liste_moteur

def creer_reservoirs(reservoirs_df: pd.DataFrame) -> List[Reservoir]:
    # TODO Transformez le dataframe des reservoir en liste d'objets de type Reservoir
    liste_reservoir = []
    for row in reservoirs_df.to_dict(orient="records"):
        reservoir = Reservoir(row["nom"], row["hauteur"],row["masse"], row["prix"],row["capacite"])
        liste_reservoir.append(reservoir)
    return liste_reservoir

def corps_celestes_accessibles(fusee: Fusee) -> List[str]:
    # TODO Retournez la liste des corps célestes accessibles par la fusée.
    #  Utiliser DELTA_V_MINIMUM_PAR_CORPS_CELESTE
    liste_corps_celestes = []
    for key, value in DELTA_V_MINIMUM_PAR_CORPS_CELESTE.items():
        if fusee.calculer_deltav() > value:
            liste_corps_celestes.append(key)
    return liste_corps_celestes


def comparer_fusee(fusee_1: Fusee, fusee_2: Fusee) -> None:
    # TODO créer un grouped barplot comparant les fusées passées en paramètre en fonction des trois métriques suivantes:
    #  * Masse / Coût
    #  * DeltaV / Coût
    #  * DeltaV / Masse
    # TODO Générez un dataframe avec trois colonnes; fusée, résultats des différents ratios et type_ratio
    dict_1 = {"fusée": [fusee_1.nom]*3, "ratios":[fusee_1.masse/fusee_1.prix, fusee_1.calculer_deltav()/fusee_1.prix, fusee_1.calculer_deltav()/fusee_1.masse], "type_ratio": ["Masse / Coût", "DeltaV / Coût", "DeltaV / Masse"]}
    dict_2 = {"fusée": [fusee_2.nom]*3, "ratios": [fusee_2.masse / fusee_2.prix, fusee_2.calculer_deltav() / fusee_2.prix, fusee_2.calculer_deltav() / fusee_2.masse],"type_ratio": ["Masse / Coût", "DeltaV / Coût", "DeltaV / Masse"]}

    dataframe1 = pd.DataFrame.from_dict(dict_1)
    dataframe2 = pd.DataFrame.from_dict(dict_2)
    dataframe_combine = pd.concat([dataframe1, dataframe2])

    print(dataframe_combine)

    g = sns.catplot(data=dataframe_combine, x="fusée", y="ratios", hue="type_ratio", kind="bar")
    g.set(ylim=(0, 0.3))
    plt.show()



if __name__ == '__main__':
    # creer_capsules
    capsules_df = charger_capsules_df(CHEMIN_CAPSULES)
    capsules = creer_capsules(capsules_df)
    for capsule in capsules:
        print(capsule)
    print()

    # creer_moteurs
    moteurs_df = charger_moteurs_df(CHEMIN_MOTEURS)
    moteurs = creer_moteurs(moteurs_df)
    for moteur in moteurs:
        print(moteur)
    print()

    # creer_reservoirs
    reservoirs_df = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    reservoirs = creer_reservoirs(reservoirs_df)
    for reservoir in reservoirs:
        print(reservoir)
    print()

    # corps_celestes_accessibles
    capsule = Capsule("PasDBonSens", 1.5, 840.0, 600.0, 1)
    reservoir_1 = Reservoir("Piscine", 25.0, 9000.0, 13000.00, 6480.0)
    moteur = Moteur("La Puissance", 12.0, 15000.0, 39000.00, 295)
    fusee_1 = Fusee("Romano Fafard", capsule, reservoir_1, moteur)

    deltaV = fusee_1.calculer_deltav()
    corps_celestes = corps_celestes_accessibles(fusee_1)
    print(f"La fusée {fusee_1.nom} peut aller, avec {deltaV:.2f} de deltaV, jusqu'à: {corps_celestes}")
    print()

    # comparer_fusee
    reservoir_2 = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    fusee_2 = Fusee("Romano Fafard Lite", capsule, reservoir_2, moteur)
    comparer_fusee(fusee_1, fusee_2)
