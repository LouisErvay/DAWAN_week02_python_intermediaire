# Parallélisme en Python avec `multiprocessing`

## Introduction au Parallélisme

Le **parallélisme** consiste à exécuter plusieurs tâches **en même temps**, en exploitant pleinement les ressources disponibles, comme les multiples cœurs d'un processeur. En Python, contrairement au **multithreading** qui est limité par le GIL (Global Interpreter Lock), le **multiprocessing** permet une véritable exécution parallèle en créant plusieurs processus indépendants, chacun ayant son propre espace mémoire.

### Pourquoi utiliser `multiprocessing` ?
Le module **`multiprocessing`** est utile pour les tâches qui nécessitent beaucoup de calculs (tâches **CPU-bound**). Chaque processus Python lancé avec `multiprocessing` s'exécute indépendamment et n'est pas affecté par le GIL, ce qui permet une véritable parallélisation des tâches sur les machines multi-cœurs.

---

## Fonctionnement de `multiprocessing`

Le module **`multiprocessing`** crée plusieurs processus (chacun avec sa propre mémoire) qui peuvent s'exécuter en parallèle. Chaque processus est complètement séparé du processus principal, contrairement aux threads qui partagent la mémoire.

### Concepts Clés :
- **Process** : Un processus est une instance d'un programme en cours d'exécution.
- **Pool de processus** : Une collection de processus qui peut être utilisée pour exécuter plusieurs tâches en parallèle.
- **Queue/Pipe** : Des mécanismes permettant la communication entre les processus.

---

## Exemple de base avec `multiprocessing`

Dans cet exemple, nous allons exécuter plusieurs fonctions en parallèle en utilisant `multiprocessing`.

### Exemple :

```python
import multiprocessing
import time

def travail_long(n):
    print(f"Processus {n} démarre.")
    time.sleep(2)  # Simule une tâche longue
    print(f"Processus {n} terminé après 2 secondes.")

if __name__ == "__main__":
    # Créer une liste de processus
    processus = []
    
    for i in range(5):
        p = multiprocessing.Process(target=travail_long, args=(i,))
        processus.append(p)
        p.start()  # Démarrer le processus

    for p in processus:
        p.join()  # Attendre que tous les processus se terminent

    print("Tous les processus sont terminés.")
```