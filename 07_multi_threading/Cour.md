https://realpython.com/python-concurrency/

### Concepts de base:

#### 1. Processus :

Un processus est une instance d'un programme, avec son espace mémoire aloué

#### 2. Threads :

Un thread est une unité plus petite, appartenant à un processus. C'est un Fil d'instruction. Un processus peut avoir plusieurs threads.

#### 3. GIL : Global Interpreter Lock

Le Global Interpreter Lock (GIL) est un mécanisme de verrouillage dans l'interpréteur Python (CPython) qui permet à un seul thread d'exécuter du bytecode Python à la fois, même sur des machines multi-cœurs. Il est conçu pour faciliter la gestion de la mémoire, mais limite le parallélisme pour les tâches intensives en calcul (CPU-bound).

