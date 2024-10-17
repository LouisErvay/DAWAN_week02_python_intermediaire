# Les Context Managers en Python

Les *context managers* en Python permettent de gérer des ressources qui doivent être acquises et libérées de manière explicite, comme la gestion de fichiers, les connexions à des bases de données, ou encore la gestion de threads. Ils sont conçus pour faciliter l'allocation et la libération des ressources en assurant qu'elles seront libérées correctement même en cas d'erreur. Python propose deux manières principales de définir des context managers : par le biais de classes et par le biais de fonctions (ou générateurs).

## 1. Les Context Managers avec les Classes

### 1.1. Objectif d'un Context Manager de Classe
Un *context manager* implémenté à l'aide d'une classe a pour objectif de garantir que certaines actions soient effectuées avant et après un bloc de code. Les actions avant peuvent être l'allocation de ressources, tandis que les actions après incluent généralement le nettoyage des ressources.

### 1.2. Méthodes Spéciales : `__enter__` et `__exit__`
Pour créer un *context manager* avec une classe, il est nécessaire d'implémenter deux méthodes spéciales :
- `__enter__(self)`: Cette méthode est appelée au début du bloc `with`. Elle doit retourner un objet qui pourra être utilisé à l'intérieur de ce bloc.
- `__exit__(self, exc_type, exc_value, traceback)`: Cette méthode est appelée à la fin du bloc `with`, même si une exception survient. Elle reçoit trois arguments permettant de gérer les exceptions si nécessaire.

### 1.3. Utilité dans le Bloc `with`
Le *context manager* est utilisé en conjonction avec le mot-clé `with`, garantissant une gestion propre des ressources. Cela évite les oublis de nettoyage manuel des ressources, comme la fermeture de fichiers ou de connexions.

### 1.4 Exemple de Classe Context Manager 
```python
class AutoFileManager:
    file = None
    def __enter__(self):
        self.file = open("test.txt", "r", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.file.closed:
            self.file.close()

with AutoFileManager() as file:
    x = file.read()
    print(x)
```

## 2. Les Context Managers avec les Fonctions

### 2.1. Utilisation des Décorateurs et du Module `contextlib`
Une autre manière de définir un *context manager* est d'utiliser une fonction décorée par `@contextlib.contextmanager`. Cette méthode est souvent plus concise et se prête bien aux besoins simples.

### 2.2. Structure d'une Fonction `@contextmanager`
Les fonctions utilisées comme context managers sont écrites avec une structure particulière :
- La première partie de la fonction, avant `yield`, contient le code qui s'exécute avant l'entrée dans le bloc `with`.
- L'instruction `yield` indique où le contrôle est transféré au bloc `with`.
- Après `yield`, le code qui s'exécute correspond à la phase de nettoyage ou de libération de la ressource.

### 2.3. Avantages par Rapport aux Classes
L'approche basée sur les fonctions peut être plus simple à lire et à écrire pour des context managers légers. Elle est adaptée pour des cas où il n'y a pas besoin de stocker l'état ou de manipuler des objets complexes.

### 2.4 Exemple de Fonction Context Manager 
```python
from contextlib import contextmanager

@contextmanager
def database_connection():
    file = None
    try:
        file = open("test.txt", "r", encoding="utf-8")
        yield file
    finally:
        if not file.closed:
            file.close()

with database_connection() as file:
    x = file.read()
    print(x)
```