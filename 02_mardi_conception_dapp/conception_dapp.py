# Trois notions:
# 1- Les principes solides
# 2- Design paterns -> Réutilisable, catalogues de solutions à des problèmes génériques
# 3-

# DevOps c'est:
# L'idée d'une livraison continue -> exemple: toutes les semaines réunion avec le client, livraison de l'avancement, ect..
# Afin d'éviter les conflits entre les dev qui font pleins de fonctionnalités, et ceux qui déploient, vis a vis servers, contraintes sécu ect..
# Du coup pour éviter ces problématiques de conflit, on a essayer de mettre en place des regles ect
# C'est ca le devops, developpeur opération, la maitrise du lien entre des deux

# Que le code soit testable sans intégration, que le code puisse etre intégrer suite aux tests
# - Que l'architecture logicielle soit flexible pour l'évolution
# - Qu'elle offre une flexibilité au choix technique -> peut etre que demain on passe de sqlite a mongoDB
# Donc prévoir ces potentiels changement futurs, donc travailler sur des découplages -> les entités ne doivent pas etre couplés entre elles
# Que les entités travaillent ensemble mais ne dépendent pas les unes des autres.

# Par exemple pour la DB avec une couche intermédiaire entre les fonctionnalités propres à la DB, et les fonctionnalités utiles du client


# QUAND ON FAIT LE OBJET
# - Notion de responsabilité de la class
# Class Employee -> la class employer -> la responsabilité de la class employee n'est pas de s'auto gérer en db
# Class EmployeeDbService -> la class qui gère les employers dans la base de donnée