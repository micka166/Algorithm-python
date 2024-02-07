# Variables et Types de Données:

x = 10 (affectation de variable)

Types de données: int, float, str, list, tuple, dict, set, bool, etc.

# Opérations de Base:

+, -, \*, / (opérations mathématiques)

% (modulo)

// (division entière)
\*\* (exponentiation)


# Structures de Contrôle:

if, elif, else (instructions conditionnelles)

for (boucle for)

while (boucle while)

break, continue (contrôle de boucle)


# Fonctions:

def (définir une fonction)

return (retourner une valeur depuis une fonction)

Paramètres et arguments de fonction

# Listes et Tuples:

Indexation et découpage (liste[1], liste[1:3])

Méthodes de liste: append(), extend(), insert(), remove(), pop()

Dictionnaires:

Définition et accès (dictionnaire = {'clé': 'valeur'})

### Méthodes de dictionnaire: keys(), values(), items()
#### Ensemble

Définition (ensemble = {1, 2, 3})

Opérations d'ensemble: union, intersection, différence, etc.

# Entrée/Sortie:

print() (affichage)

input() (saisie utilisateur)

Gestion d'Exceptions:

try, except, finally
# Modules et Bibliothèques:

import (importer des modules)

Bibliothèques populaires: math, random, datetime, os, sys

Travail avec des Fichiers:

open(), read(), write(), close()
# Classes et Objets:

class (définir une classe)

**init** (méthode d'initialisation)

Attributs et méthodes de classe

Expressions Régulières:

Module re

# Manipulation de Chaînes de Caractères:

Concaténation, découpage, méthodes de chaîne

Opérations sur les Fichiers et Répertoires:

Module os
# Gestion de la Date et de l'Heure:

Module datetime

# Opérateurs Logiques
and : Retourne True si les deux expressions booléennes à gauche et à droite de l'opérateur sont vraies.
or : Retourne True si au moins l'une des expressions booléennes à gauche ou à droite de l'opérateur est vraie.
not : Retourne l'inverse de la valeur booléenne de l'expression suivant l'opérateur.

# OPERATEUR DE COMPARAISON
    == : Égal à

    != : Différent de

    < : Inférieur à

    > : Supérieur à

    <= : Inférieur ou égal à

    >= : Supérieur ou égal à



# Function exemple 

1. Print
2. Additionner
3. soustraire
4. Multiplier
5. Diviser
6. Factorielle
7. Est pair
8. Est un nombre Premier


<font color="red">
Les function sont appeler par le nom 

Les methodes sont appeler par les objets 
<font color="white">
# les variables SCOP

# Les Scopes en Python

En Python, le terme "scope" fait référence à la portée d'une variable, c'est-à-dire la partie du code dans laquelle cette variable est accessible. Il existe plusieurs types de portées en Python, notamment :

## 1. Portée Locale (Local Scope)

Une variable définie à l'intérieur d'une fonction est accessible uniquement à l'intérieur de cette fonction. Elle est dite être dans un scope local. Une fois que la fonction est terminée, la variable n'est plus accessible.

Exemple :
```python
def ma_fonction():
    x = 10  # x est dans le scope local de ma_fonction
    print(x)

ma_fonction()  # Affiche : 10
print(x)  # Cette ligne provoquera une erreur car x n'est pas accessible ici
```
## 2. Portée Globale (Global Scope)
Une variable définie en dehors de toutes les fonctions est accessible dans tout le programme. Elle est dite être dans un scope global.

Exemple :
```
python
Copy code
y = 20  # y est dans le scope global

def ma_fonction():
    print(y)

ma_fonction()  # Affiche : 20
print(y)  # Affiche : 20
```
## 3. Portée de la Fonction Imbriquée (Enclosing Scope)
Si une fonction est définie à l'intérieur d'une autre fonction, elle a accès aux variables de la fonction englobante.

Exemple :
```
python
Copy code
def externe():
    z = 30  # z est dans le scope de la fonction externe

    def interne():
        print(z)

    interne()

externe()  # Affiche : 30
```
## 4. Portée de Boucle (Loop Scope)
Les variables définies dans une boucle sont accessibles uniquement à l'intérieur de cette boucle.

Exemple :
```
python
Copy code
for i in range(3):
    print(i)  # i est dans le scope de la boucle
```

## Valeurs par default

### En Python, vous pou définir desurs par défaut les paramètres d' fonction. Lorsque vous appelez la fonction, vous pouvez omettre ces paramètres et les valeurs par défautont utilisées à la place.

Voici un exemple de avec des valeurs par défaut
```python
def ma_fonction(param1, param2=10, param3=20):
    print(param1, param2, param3)

ma_fonction(1)  # Affiche : 1 10 20
ma_fonction(1, 2)  # Affiche : 1 2 20
ma_fonction(1, 2, 3)  # Affiche : 1 2 3

```

### Dans cet exemple, param2 et param3 ont des valeurs par défaut de 10 et 20 respectivement. Lorsque vous appelez ma_fonction avec un seul argument, les valeurs par défaut de param2 et param3 sont utilisées. Lorsque vous appelez ma_fonction avec deux arguments, la valeur par défaut de param3 est utilisée. Et lorsque vous appelez ma_fonction avec trois arguments, les valeurs que vous avez spécifiées sont utilisées pour param1, param2, et param3.

### Vous pouvez également définir des valeurs par défaut pour des paramètres en utilisant des expressions Python. Par exemple 
```python
def ma_fonction(param1, param2=None):
    if param2 is None:
        param2 = []
    param2.append(param1)
    print(param2)

ma_fonction(1)  # Affiche : [1]
ma_fonction(2, [3])  # Affiche : [2, 3]
```
Dans cet exemple, param2 a une valeur par défaut de None. Lorsque vous appelez ma_fonction avec un seul argument, param2 est défini comme une nouvelle liste et param1 est ajouté à cette liste. Lorsque vous appelez ma_fonction avec deux arguments, param2 est défini comme la valeur que vous avez spécifiée et param1 est ajouté à cette liste.

# Duck Typing

Duck typing est un concept de programmation qui permet de déterminer le type d'un objet en fonction de ses méthodes et attributs, plutôt que de son type déclaré. Le nom de cette approche vient de la phrase « Si ça marche comme un canard, nage comme un canard et caquète comme un canard, c'est un canard ».

En d'autres termes, duck typing consiste à vérifier si un objet possède les méthodes et attributs nécessaires pour remplir une certaine fonction, plutôt que de vérifier son type. Cela permet de rendre le code plus flexible et réutilisable, car il peut fonctionner avec n'importe quel objet qui possède les méthodes et attributs requis, quel que soit son type.

Par exemple, en Python, on peut utiliser duck typing pour définir une fonction qui prend en argument un objet qui doit avoir une méthode append(). Cette fonction fonctionnera avec n'importe quel objet qui possède cette méthode, qu'il s'agisse d'une liste, d'une chaîne de caractères, d'un dictionnaire ou de tout autre objet personnalisé.

Voici un exemple de fonction utilisant duck typing en Python :

```python
Copy code
def append_to_object(obj, value):
    obj.append(value)

# Cette fonction fonctionnera avec une liste
my_list = []
append_to_object(my_list, "hello")

# Cette fonction fonctionnera également avec une chaîne de caractères
my_string = ""
append_to_object(my_string, "world")
```
  Dans cet exemple, la fonction append_to_object() utilise duck typing pour ajouter une valeur à n'importe quel objet qui possède une méthode append(). La fonction fonctionnera donc avec une liste ou une chaîne de caractères, mais aussi avec tout autre objet personnalisé qui possède cette méthode.


# Docstrings en Python

En Python, les docstrings sont des chaînes de caractères littérales qui sont utilisées comme commentaires pour documenter des parties spécifiques du code. Ils sont généralement utilisés pour expliquer ce que fait une fonction, une méthode, une classe ou un module.

Les docstrings sont définis en utilisant des triples guillemets (""" ou ''') au début et à la fin de la chaîne de caractères. Ils sont souvent multi-lignes, bien qu'ils puissent aussi être sur une seule ligne.

Un exemple de docstring pour une fonction pourrait ressembler à ceci :

```python
def add(a, b):
    """
    Cette fonction ajoute deux nombres et renvoie le résultat.
    :param a: Le premier nombre à ajouter.
    :param b: Le deuxième nombre à ajouter.
    :return: Le résultat de l'ajout de a et b.
    """
    return a + b
```
<font color='red'>
# Au Format google les docstrings sont pareil 

```python
def add(a, b):
    """
    Cette fonction ajoute deux nombres et renvoie le résultat.

    Args:
        a (int or float): Le premier nombre à ajouter.
        b (int or float): Le deuxième nombre à ajouter.

    Returns:
        int or float: Le résultat de l'ajout de a et b.
    """
    return a + b


Fonctions recursive

Voici un exemple simple d'une fonction récursive en Python qui calcule la factorielle d'un nombre :
```python

def factorial(n):
    # Cas de base : si n est égal à 0 ou 1, la factorielle est 1
    if n == 0 or n == 1:
        return 1
    # Cas récursif : la factorielle de n est égale à n multiplié par la factorielle de (n-1)
    else:
        return n * factorial(n-1)

result = factorial(5)
print("Factorielle de 5 est :", result)
```
- Dans cette fonction factorial, la partie récursive est n * factorial(n-1). La fonction appelle elle-même avec un argument réduit jusqu'à atteindre le cas de base (n == 0 ou n == 1), où elle retourne 1. Ensuite, chaque appel de fonction se déroule dans le sens inverse, multipliant les résultats pour obtenir la factorielle du nombre initial.
    
<font color='white'>



# LISTE DES MODULES

1. **os** - Fonctionnalités de système d'exploitation.
2. **sys** - Paramètres et fonctions spécifiques au système.
3. **math** - Fonctions mathématiques.
4. **random** - Génération de nombres aléatoires.
5. **datetime** - Manipulation de dates et heures.
6. **json** - Encodage et décodage de données JSON.
7. **re** - Expressions régulières.
8. **csv** - Lecture et écriture de fichiers CSV.
9. **urllib** / **urllib2** / **requests** - Pour les requêtes HTTP.
10. **sqlite3** - Base de données SQLite.
11. **email** - Manipulation des e-mails.
12. **smtplib** - Envoi d'e-mails via SMTP.
13. **tkinter** / **PyQt** / **wxPython** - Bibliothèques pour créer des interfaces graphiques.
14. **multiprocessing** - Traitement multi-thread et multi-processus.
15. **socket** - Communication par socket.
16. **xml** / **xml.etree.ElementTree** - Traitement XML.
17. **logging** - Système de journalisation.
18. **unittest** - Cadre de test unitaire.
19. **pickle** / **cPickle** - Sérialisation d'objets Python.
20. **gzip** / **zipfile** - Compression de fichiers.
21. **collections** - Types de données supplémentaires.
22. **itertools** - Fonctions pour créer et manipuler des itérateurs.
23. **time** - Fonctions relatives au temps.
24. **subprocess** - Exécution de processus supplémentaires.
25. **platform** - Informations sur la plate-forme.
26. **argparse** - Analyse des arguments de ligne de commande.
27. **socketserver** - Cadre pour les serveurs de réseau.
28. **http.server** - Serveur HTTP.
29. **ssl** - Prise en charge de SSL.
30. **hashlib** - Fonctions de hachage sécurisé.
31. **collections** - Types de données supplémentaires.
32. **os.path** - Manipulation de chemins de fichiers.
33. **shutil** - Opérations de fichiers et de répertoires.
34. **gettext** - Système de localisation.
35. **curses** - Interface utilisateur en mode texte.
36. **asyncio** - Support de programmation asynchrone.
37. **numpy** - Traitement de tableaux et calculs mathématiques.
38. **pandas** - Analyse de données et manipulation de tableaux de données.
39. **matplotlib** - Traçage de graphiques et de visualisations.
40. **scikit-learn** - Bibliothèque pour l'apprentissage automatique.
41. **tensorflow** / **PyTorch** - Bibliothèques pour le deep learning.
42. **NLTK** - Outils pour le traitement du langage naturel.
43. **Beautiful Soup** - Parsing HTML et XML.
44. **requests-html** - Bibliothèque HTTP combinant BeautifulSoup et requests.
45. **Pygame** - Développement de jeux.
46. **Django** / **Flask** - Frameworks pour le développement web.
47. **SQLAlchemy** - Outil de mapping objet-relationnel (ORM) pour la manipulation de bases de données relationnelles.
48. **wxPython** - Bibliothèque GUI native de Python pour les applications de bureau.
49. **Pillow** - Bibliothèque de traitement d'images.
50. **PyQt** / **PyGTK** - Autres bibliothèques GUI pour les applications de bureau.
51. **pySerial** - Communication série avec les périphériques.
52. **openpyxl** - Manipulation de fichiers Excel.
53. **pytz** - Gestion des fuseaux horaires.
54. **FuzzyWuzzy** - Comparaison de chaînes floues.
55. **scrapy** - Framework d'extraction de données.
56. **SymPy** - Bibliothèque de calcul symbolique.
57. **pytest** - Cadre de test pour Python.
58. **pyinstaller** - Convertit des scripts Python en exécutables autonomes.
59. **cx_Freeze** - Convertit des scripts Python en exécutables autonomes.
60. **pydantic** - Validation de données et génération de modèles de données.
61. **fastapi** - Cadre pour la création d'API web rapides.
62. **pyTelegramBotAPI** - Bibliothèque pour interagir avec l'API Telegram.
63. **pygame** - Bibliothèque pour le développement de jeux vidéo.
64. **flask-restful** - Extension Flask pour la création d'API RESTful.
65. **requests** - Bibliothèque HTTP pour les requêtes web.
66. **paramiko** - Implémentation de protocoles SSH en Python.
67. **netmiko** - Bibliothèque pour la gestion d'équipements réseau via SSH.
68. **pyodbc** - Interface Python pour les bases de données ODBC.
69. **pytube** - Bibliothèque pour le téléchargement de vidéos YouTube.
70. **pydub** - Manipulation facile des fichiers audio.
71. **tweepy** - Bibliothèque Python pour l'accès à l'API Twitter.
72. **google-api-python-client** - Client Python pour l'utilisation des API Google.
73. **beautifulsoup4** - Analyse HTML et XML de manière propre et simple.
74. **websocket-client** - Client WebSocket pour Python.
75. **pycairo** - Liaison Python pour la bibliothèque graphique Cairo.
76. **psycopg2** - Adaptateur de base de données PostgreSQL pour Python.
77. **cx_Oracle** - Adaptateur de base de données Oracle pour Python.
78. **redis-py** - Client Python pour Redis.
79. **elasticsearch** - Client Python pour Elasticsearch.
80. **kivy** - Framework pour la création d'applications multi-touch.




# Commnt fonctionne les imports de python 

1. L'importation de modules en Python est un mécanisme qui permet d'inclure et d'utiliser des fonctionnalités provenant d'autres fichiers Python ou de bibliothèques externes. Voici comment Python gère les importations :

2. Recherche de modules : Lorsque vous effectuez une instruction d'importation, Python recherche le module spécifié dans une liste prédéfinie de chemins de recherche. Ces chemins incluent le répertoire où le script en cours d'exécution est situé, ainsi que d'autres répertoires spécifiés dans la variable d'environnement PYTHONPATH. De plus, Python inclut les chemins par défaut où les bibliothèques standard sont installées.

3. Chargement du module : Une fois que Python a localisé le module à importer, il le charge en exécutant le code contenu dans le fichier du module. Lors de son chargement, le code est exécuté dans un espace de nommage séparé pour le module.

4. Attribution de référence : Une fois le module chargé, Python crée un objet qui représente le module et l'associe à un nom dans l'espace de noms du script ou du module qui a effectué l'importation. Vous pouvez ensuite accéder aux attributs et fonctions du module à travers ce nom.$



# Installation de nouveau module 

```python pip install 'nom de l'import ```'



