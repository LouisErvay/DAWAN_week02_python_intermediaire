Voici une liste des **principaux design patterns** classés en trois grandes catégories : **patterns de création**, **patterns structurels**, et **patterns comportementaux**. Ce sont les plus couramment utilisés en génie logiciel, mais il existe d'autres patterns plus spécifiques. Ces patterns sont documentés dans le fameux livre *"Design Patterns: Elements of Reusable Object-Oriented Software"* écrit par les *Gang of Four* (GoF).

### 1. **Patterns de création (Creational Patterns)**

Ces patterns portent sur la manière dont les objets sont créés. Ils permettent de mieux contrôler l'instanciation et la création d'objets.

1. **Singleton** : Assure qu'une classe n'a qu'une seule instance et fournit un point d'accès global à cette instance.
2. **Factory Method** : Définit une interface pour créer un objet, mais laisse les sous-classes décider de la classe concrète à instancier.
3. **Abstract Factory** : Fournit une interface pour créer des familles d'objets liés ou dépendants sans spécifier leurs classes concrètes.
4. **Builder** : Sépare la construction d'un objet complexe de sa représentation, permettant de créer différents types de représentation avec le même processus de construction.
5. **Prototype** : Permet de créer de nouveaux objets en **copiant** (clonant) une instance existante.

### 2. **Patterns structurels (Structural Patterns)**

Ces patterns concernent la **composition des classes et des objets**. Ils facilitent la création de structures complexes tout en maintenant la souplesse et la simplicité.

1. **Adapter (Wrapper)** : Permet à des interfaces incompatibles de fonctionner ensemble en convertissant l'interface d'une classe dans une autre que les clients attendent.
2. **Bridge** : Sépare l'**abstraction** de son **implémentation** pour qu'elles puissent évoluer indépendamment.
3. **Composite** : Compose des objets en structures arborescentes pour représenter des hiérarchies **partie-tout**. Il permet aux objets et aux compositions d'objets d'être traités de manière uniforme.
4. **Decorator** : Permet d'**ajouter dynamiquement des responsabilités** à un objet sans toucher à sa structure.
5. **Facade** : Fournit une **interface simplifiée** pour un ensemble complexe de classes, de bibliothèques, ou de systèmes.
6. **Flyweight** : Réduit le coût de création d'objets similaires en partageant autant de données que possible entre eux (souvent utilisé pour des systèmes avec beaucoup d'objets, comme des systèmes graphiques).
7. **Proxy** : Fournit un **représentant** ou un **surrogat** pour contrôler l'accès à un autre objet.

### 3. **Patterns comportementaux (Behavioral Patterns)**

Ces patterns se concentrent sur les interactions et les responsabilités entre objets et la manière dont ils communiquent.

1. **Chain of Responsibility** : Passe une requête le long d'une **chaîne** d'objets pour trouver un objet qui la traite, permettant à chaque objet d'accepter ou de refuser de traiter la requête.
2. **Command** : Encapsule une requête sous forme d'objet, permettant de paramétrer des actions, les mettre en file d'attente, ou de les annuler.
3. **Interpreter** : Fournit une manière d'évaluer des langages ou des expressions. Ce pattern est souvent utilisé dans la construction de langages spécifiques à un domaine (DSL).
4. **Iterator** : Fournit un moyen d'**accéder aux éléments** d'une collection de manière séquentielle sans exposer sa représentation interne.
5. **Mediator** : Définit un objet qui gère la **communication** entre un ensemble d'objets pour les rendre indépendants les uns des autres.
6. **Memento** : Capture et restaure l'**état interne** d'un objet sans violer son encapsulation (utile pour implémenter des fonctions d'annulation, par exemple).
7. **Observer (Publish/Subscribe)** : Permet à un objet (le sujet) d'**informer** plusieurs autres objets (observateurs) d'un changement d'état, sans les coupler fortement.
8. **State** : Permet à un objet de modifier son comportement en fonction de son état interne.
9. **Strategy** : Définit une famille d'algorithmes, encapsule chaque algorithme, et les rend interchangeables au moment de l'exécution.
10. **Template Method** : Définit le **squelette d'un algorithme** dans une méthode, en déléguant certaines étapes à des sous-classes. Il permet aux sous-classes de redéfinir certaines étapes sans changer la structure globale de l'algorithme.
11. **Visitor** : Permet de définir de nouvelles opérations sur une structure d'objets sans en modifier les classes.

---

### Autres patterns connus :
En plus des **GoF patterns**, il existe d'autres **patterns de conception** qui sont apparus dans le domaine du génie logiciel :

1. **Dependency Injection** : Un pattern architectural où les dépendances sont **injectées** dans une classe plutôt que créées en son sein, rendant le code plus testable et flexible.
2. **Model-View-Controller (MVC)** : Sépare les préoccupations en trois couches : **Modèle** (gestion des données), **Vue** (interface utilisateur) et **Contrôleur** (gestion des interactions).
3. **Model-View-ViewModel (MVVM)** : Une variante de MVC, souvent utilisée dans des frameworks modernes comme Angular ou React.
4. **Repository Pattern** : Un pattern utilisé pour séparer la **logique métier** de l'**accès aux données**.
5. **Service Locator** : Un pattern pour récupérer des dépendances via un **registre central** de services, en alternative à l'injection de dépendances.

---

### En résumé :

- **Patterns de création** : Concernent la manière dont les objets sont créés (Singleton, Factory, Builder...).
- **Patterns structurels** : Concernent la manière d'organiser les classes et les objets (Adapter, Facade, Decorator...).
- **Patterns comportementaux** : Concernent les interactions entre objets (Observer, Command, Strategy...).

Ces patterns t’aident à structurer ton code pour le rendre **plus modulaire**, **maintenable**, et **facile à comprendre**. Ils ne sont pas des règles strictes, mais des **modèles réutilisables** qui répondent à des situations courantes en programmation.