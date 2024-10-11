La différence entre une **interface** et une **classe abstraite** repose sur les concepts de **modèle** et de **contrat** dans la programmation orientée objet. Voici une explication vulgarisée des deux concepts et des raisons pour choisir l'un ou l'autre.

### 1. **Interface** – **Un contrat sans implémentation**

**Ce que c'est** :
- Imagine une interface comme un **contrat** qu'une classe doit respecter. Ce contrat dit "Si tu veux être de ce type, tu dois obligatoirement avoir ces méthodes".
- **Aucune implémentation** (code) spécifique n’est fournie dans une interface, elle se contente de définir **ce qui doit exister**, pas **comment ça doit fonctionner**.

**Exemple de la vie réelle** :
- Prenons l'interface `Voler`. Si une classe comme `Oiseau`, `Avion`, ou `Hélicoptère` veut implémenter `Voler`, elle doit avoir une méthode `voler()`, mais chaque classe l’implémentera à sa manière.

**Pourquoi utiliser une interface ?** :
- Utiliser une interface, c'est quand tu veux **imposer un comportement** sans te soucier de **comment** ce comportement sera réalisé.
- **Choisir une interface** lorsque tu sais que plusieurs classes vont partager des **comportements communs** (comme `voler`, `nager`, etc.), mais que ces classes n’ont pas de lien hiérarchique évident entre elles (par exemple, un `Avion` n’a pas grand-chose en commun avec un `Oiseau` à part qu'ils volent tous les deux).

### 2. **Classe abstraite** – **Un modèle partiellement implémenté**

**Ce que c'est** :
- Une classe abstraite est comme une **base** ou un **modèle** pour d'autres classes. Elle peut avoir des méthodes **avec du code** (implémentées) et des méthodes **sans code** (abstraites).
- Elle est souvent utilisée pour éviter de réécrire le même code dans plusieurs classes. Les sous-classes qui héritent de la classe abstraite doivent compléter les méthodes abstraites non implémentées.

**Exemple de la vie réelle** :
- Imaginons une classe abstraite `Animal`. Elle peut avoir des méthodes communes comme `respirer()` (avec déjà une implémentation parce que tous les animaux respirent de la même manière) et une méthode abstraite `faire_du_bruit()` (chaque animal doit spécifier comment il fait du bruit).

**Pourquoi utiliser une classe abstraite ?** :
- Tu choisis une classe abstraite quand tu veux **partager du code** entre plusieurs classes tout en forçant certaines d’entre elles à fournir leur propre version de certaines méthodes (comme `faire_du_bruit()`).
- **Choisir une classe abstraite** quand tu as un lien hiérarchique naturel entre tes classes (par exemple, `Animal` → `Chien`, `Chat`, `Oiseau`). Cela permet de **réutiliser du code** et de définir un **comportement partiellement standardisé**.

### Résumé des différences

| **Aspect**              | **Interface**                                           | **Classe Abstraite**                               |
|-------------------------|---------------------------------------------------------|----------------------------------------------------|
| **Implémentation**       | Ne contient **aucune** implémentation (juste des méthodes vides) | Peut contenir des méthodes avec du code et des méthodes abstraites |
| **Héritage**             | Une classe peut implémenter **plusieurs interfaces**    | Une classe ne peut hériter que d'**une seule** classe abstraite     |
| **Utilisation**          | Quand tu veux juste imposer des méthodes, **sans code commun** | Quand tu veux **réutiliser du code** entre les classes |
| **Lien hiérarchique**    | Aucune hiérarchie nécessaire                            | Hiérarchie naturelle entre classes                 |

### Quand choisir l'un ou l'autre ?

- **Interface** : Utilise-la lorsque tes classes n’ont pas besoin de partager du code, mais doivent respecter **certaines règles** (par exemple, tu veux être sûr que toutes les classes qui "voleront" auront une méthode `voler()`).
  
- **Classe abstraite** : Utilise-la lorsque tu veux que les classes partagent **du code commun** et **complètent** certaines parties spécifiques. C'est utile lorsque tes classes ont une relation hiérarchique évidente (comme `Animal` et ses sous-classes).

### En bref :
- **Interface** = "Voici les méthodes que tu dois implémenter, mais je me fiche de comment tu fais."
- **Classe abstraite** = "Voici quelques méthodes prêtes à l'emploi, mais tu dois en compléter certaines toi-même."

Cela te permet de mieux organiser ton code, en fonction de ce que tes classes partagent et de la flexibilité dont tu as besoin.