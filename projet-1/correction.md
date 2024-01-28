# Correction du Projet 1

## Grille de correction

| **Exercices**                                    | **Note** | **Points** |
| ------------------------------------------------ | :------: | :--------: |
| Exercice 1                                       |    5     |     5      |
| Exercice 2                                       |    7     |     8      |
| Exercice 3                                       |    7     |     7      |
| **Total**                                        | **19.0** |   **20**   |

### Commentaires

- partie1.py:\
  N'oublie pas de réutiliser les variable initiales.
  Dans ton cas, tu aurais dû entrer: 
  ```python
  taux_periodique = taux_annuel / 365
  # Au lieu de:
  taux_periodique = 0.065 / (365)
  ```

- partie2.py:\
  Tu n'as pas besoin de donner explicitement tous les branchements de tes conditions `if`. Par exemple, tu aurais pu simplifier ton code en écrivant:
  ```python
    if capital_1 < capital_2:
        break
  
    # au lieu de 
    if capital_1 >= capital_2:
        pass # <-- ce pass est inutile
    else:
        break
  ```
  Tu dois aussi faire attention à utiliser des noms plus significatifs. Ça permet de rendre ton code plus lisible et plus facile à maintenir. Par exemple, écrire `nb_jours` au lieu de `n`, ou `liste_jours` au lieu de `x`.\
  Une autre erreur dans ce numéro est que tu itères seulement sur les 365 premiers jours (`x = range(365)`). Si le point de croisement des bénéfices des deux investissements était après le 365ème jour, ton programme ne le trouverait pas. (-1 points)\
  Pour résoudre ce problème, tu peux utiliser une boucle `while` qui itère (à l'infini) tant que la condition est vraie. Par exemple:
  ```python
  while capital_1 >= capital_2:
      # ton code
  ```
  Ton utilisation des variables initiales et des variables intermédiaires est excellente, bravo!

- partie3.py:\
  Je vois que tu as finalement gardé la liste 🥲 Comme je t'avais expliqué en classe, cette solution est très inefficace en terme de mémoire. Ta complexité spatiale est linéaire en fonction du nombre de jours. Donc si le nombre de jours est de 1000, tu utilises 1000 fois plus de mémoire que la solution optimale (qui est de ne garder en mémoire que le jour précédent). Tu peux faire le test de ton programme avec un nombre de jours très grand (par exemple 100000000). Ouvre ton Task Manager, exécute ton code et regarde l'utilisation de ta mémoire monter en flèche 🚀😎.

## Très bon travail!
