Définir une **classe abstraite** en Python se fait de manière similaire à une interface, mais avec une différence majeure : une classe abstraite peut contenir à la fois des **méthodes abstraites** (sans implémentation) et des **méthodes concrètes** (avec une implémentation). Voici comment cela fonctionne.

### Exemple de classe abstraite en Python

```python
from abc import ABC, abstractmethod

# Définition d'une classe abstraite
class Animal(ABC):

    def __init__(self, nom):
        """Initialise le nom de l'animal."""
        self.nom = nom
    
    # Méthode abstraite (obligatoire à implémenter dans les sous-classes)
    @abstractmethod
    def faire_du_bruit(self):
        pass
    
    # Méthode concrète (optionnelle de réécrire dans les sous-classes)
    def respirer(self):
        print("L'animal respire.")

# Sous-classe de Animal qui implémente la méthode abstraite
class Chien(Animal):
    
    def faire_du_bruit(self):
        print("Le chien aboie.")

# Sous-classe de Animal qui implémente la méthode abstraite
class Chat(Animal):
    
    def faire_du_bruit(self):
        print("Le chat miaule.")

# Tester les classes
chien = Chien("Rex")
chien.respirer()      # Affiche : L'animal respire.
chien.faire_du_bruit() # Affiche : Le chien aboie.

chat = Chat("Minou")
chat.respirer()       # Affiche : L'animal respire.
chat.faire_du_bruit()  # Affiche : Le chat miaule.
```

### Explication :

1. **Classe abstraite (`Animal`)** :
   - `Animal` est définie comme une classe abstraite en héritant de la classe `ABC`.
   - Elle contient une **méthode abstraite** `faire_du_bruit()`. Toute sous-classe d'`Animal` doit obligatoirement implémenter cette méthode.
   - Elle contient aussi une **méthode concrète** `respirer()`, qui a déjà une implémentation. Les sous-classes héritent de cette méthode et peuvent choisir de la réutiliser ou de la surcharger si nécessaire.

2. **Sous-classes (`Chien`, `Chat`)** :
   - `Chien` et `Chat` héritent d'`Animal` et doivent obligatoirement implémenter la méthode abstraite `faire_du_bruit()`.
   - Elles héritent également de la méthode `respirer()`, qui est déjà implémentée dans la classe abstraite.

### Quand utiliser une classe abstraite ?

- Tu utilises une **classe abstraite** lorsque tu veux qu’un groupe de classes partage une **implémentation partielle**, tout en laissant certaines méthodes à chaque sous-classe le soin de les compléter.
- Par exemple, ici, tous les animaux respirent de la même manière, donc on peut mettre cette implémentation dans la classe abstraite `Animal`. Par contre, la façon dont chaque animal fait du bruit est différente, donc cela doit être défini dans chaque sous-classe (`Chien`, `Chat`).

### En résumé :
- Une **classe abstraite** peut contenir à la fois des méthodes abstraites et des méthodes concrètes.
- Les sous-classes doivent **obligatoirement** implémenter toutes les méthodes abstraites, mais elles peuvent choisir d'utiliser ou de surcharger les méthodes concrètes.

Cela te donne une base pour structurer ton code quand certaines parties du comportement sont communes, et d'autres sont spécifiques à chaque sous-classe !