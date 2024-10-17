# Concurrence (concurrency) en Python

La **concurrence** fait référence à la capacité d'un programme à gérer plusieurs tâches en même temps, mais pas forcément en les exécutant au même moment. Il s'agit de jongler avec plusieurs choses à la fois en basculant entre elles.

En Python, la concurrence peut être réalisée de deux manières principales :

## a. `threading` en Python

### Qu'est-ce que `threading` ?

**`threading`** est une bibliothèque Python qui permet de créer et de gérer des threads, c'est-à-dire des sous-processus légers pouvant être exécutés de manière concurrente. Chaque thread fonctionne comme une unité d'exécution indépendante qui partage les mêmes ressources (comme la mémoire) que le processus parent, ce qui rend le `threading` particulièrement utile pour les tâches qui peuvent être divisées en sous-tâches exécutées simultanément.

Le **multithreading** permet de gérer plusieurs tâches en même temps, mais contrairement à l'asynchronisme d'`asyncio`, **le changement de contexte entre les threads est géré par l'interpréteur Python ou le système d'exploitation**. Python utilise un verrou global d'interpréteur (GIL), ce qui peut limiter l'efficacité du multithreading pour les tâches intensives en CPU.

#### Concepts Clés :
- **Thread** : Un thread est une unité légère d'exécution qui fait partie d'un processus.
- **Multitâche préemptif** : Le système ou l'interpréteur décide automatiquement quand basculer d'un thread à un autre.
- **Global Interpreter Lock (GIL)** : En Python, ce verrou empêche plusieurs threads d'exécuter des bytecodes Python en même temps, ce qui limite le parallélisme sur les tâches CPU-bound mais reste efficace pour les tâches I/O-bound.

---

### Exemple d'utilisation de `threading`

#### Exemple de base :

Ce programme montre comment utiliser le module `threading` pour exécuter plusieurs fonctions en parallèle.


```python
import threading
import time

# Définir une fonction à exécuter dans un thread
def dire_bonjour():
    print("Bonjour!")
    time.sleep(2)  # Simule une tâche longue
    print("Bonjour après 2 secondes!")

def dire_au_revoir():
    print("Au revoir!")
    time.sleep(1)  # Simule une tâche plus courte
    print("Au revoir après 1 seconde!")

# Créer deux threads
thread1 = threading.Thread(target=dire_bonjour)
thread2 = threading.Thread(target=dire_au_revoir)

# Démarrer les threads
thread1.start()
thread2.start()

# Attendre que les threads se terminent avant de poursuivre
thread1.join()
thread2.join()

print("Les deux threads sont terminés.")
```

## b. `asyncio` en Python

### Qu'est-ce que `asyncio` ?

**`asyncio`** est une bibliothèque intégrée dans Python qui permet de gérer des tâches de manière asynchrone, facilitant l'écriture de code non-bloquant. Le principal avantage d'`asyncio` est sa capacité à exécuter des opérations d'I/O (entrées/sorties) sans bloquer l'exécution du programme, ce qui est particulièrement utile pour les opérations réseau, la gestion des fichiers, ou d'autres tâches I/O-bound.

#### Concepts Clés :
- **Asynchronisme** : L'exécution des tâches ne suit pas une ligne droite. Le programme peut "attendre" à certains moments (`await`), sans bloquer le reste du programme.
- **`await`** : Il est utilisé pour indiquer un point où le programme suspend son exécution jusqu'à ce que la tâche asynchrone soit terminée. Durant cette période, d'autres tâches peuvent s'exécuter.
- **`async def`** : Permet de définir une fonction asynchrone.

#### Avantages :
- Les tâches peuvent être exécutées de manière concurrente, mais avec un contrôle explicite des moments où le programme peut passer d'une tâche à l'autre.
- Contrairement au threading, où le système décide quand passer d'un thread à l'autre, `asyncio` permet au développeur de contrôler explicitement ces moments.

---

### Exemple d'utilisation de `asyncio`

#### Exemple de base :

Ce programme montre l'exécution de deux tâches asynchrones. Elles utilisent `await` pour attendre un certain temps tout en permettant à d'autres tâches de s'exécuter durant l'attente.

```python
import asyncio

# Définir une fonction asynchrone
async def dire_bonjour():
    print("Bonjour!")
    await asyncio.sleep(2)  # Attendre 2 secondes sans bloquer le programme
    print("Bonjour après 2 secondes!")

async def dire_au_revoir():
    print("Au revoir!")
    await asyncio.sleep(1)  # Attendre 1 seconde
    print("Au revoir après 1 seconde!")

# Créer un événement principal qui exécute les deux tâches en parallèle
async def main():
    # Les tâches sont lancées "concurremment"
    await asyncio.gather(dire_bonjour(), dire_au_revoir())

# Exécuter l'événement principal
asyncio.run(main())
```