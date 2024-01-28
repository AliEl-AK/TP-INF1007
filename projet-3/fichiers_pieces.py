import pandas as pd

from constantes import CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS, FICHIER_CAPSULE, FICHIERS_RESERVOIRS, \
    FICHIERS_MOTEURS


def charger_capsules_df(chemin_capsules: str) -> pd.DataFrame:
    # TODO Retournez un dataframe des capsules décrites dans le fichier FICHIER_CAPSULE
    #  Il faut aussi renommer les colonnes pour que celles-ci soient plus lisibles
    create_dataframe = pd.read_csv(chemin_capsules + "/" + FICHIER_CAPSULE)
    new_dataframe_capsules = create_dataframe.rename(columns={'n': 'nom', 'h': 'hauteur', 'm': 'masse', 'p': 'prix', 'pl': 'places'})
    return new_dataframe_capsules

def charger_reservoirs_df(chemin_reservoirs: str) -> pd.DataFrame:
    # TODO Retournez un dataframe combiné des réservoirs décrits dans
    #  les fichiers FICHIERS_RESERVOIRS
    liste_df = []
    for i in FICHIERS_RESERVOIRS:
        liste_df.append(pd.read_json(chemin_reservoirs + "/" + i))
    return pd.concat(liste_df, ignore_index=True)
def charger_moteurs_df(chemin_moteurs: str) -> pd.DataFrame:
    # TODO Retournez un dataframe combiné des moteurs décrits dans
    #  les fichiers FICHIERS_MOTEURS
    list_moteurs = []

    for i in range(1,len(FICHIERS_MOTEURS)+1):     
        file1 = open(chemin_moteurs + f"/moteur{i}.ppl", 'r')
        lines = file1.readlines()
        liste = []
        for line in lines:
            if not ( line.startswith('#') or line.startswith('\n')):
                liste.append(line)
        lines = [line.rstrip('\n') for line in liste]
        list_moteurs.append(dict(item.split('=') for item in lines))
    df_moteurs = pd.DataFrame(list_moteurs).apply(pd.to_numeric, errors='ignore')
    file1.close()
    return df_moteurs
def filtrer_moteurs(moteurs_df: pd.DataFrame, impulsion_minimum: int) -> pd.DataFrame:
    # TODO Retourner un sous-ensemble filtré d'un df de moteurs
    #  où l'impulsion spécifique est au dessus d'un certain seuil
    return moteurs_df[moteurs_df["impulsion specifique"] > impulsion_minimum]

if __name__ == '__main__':
    # charger_capsules_df
    capsules = charger_capsules_df(CHEMIN_CAPSULES)
    print(capsules)
    print()

    # charger_reservoirs_df
    reservoirs = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    print(reservoirs)
    print()

    # charger_moteurs_df
    moteurs = charger_moteurs_df(CHEMIN_MOTEURS)
    print(moteurs)
    print()

    # filtrer_moteurs
    moteurs_filtres = filtrer_moteurs(moteurs, 220)
    print(moteurs_filtres)
