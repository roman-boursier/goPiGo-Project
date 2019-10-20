# goPiGo-Project
[M2 ISE 2019] Master informatique 2ème année 2019-2020
 
1. Présentation du projet

L’objectif de ce projet est la réalisation d’un robot capable de chercher et trouver un objet désigné. On indique dans un premier temps au robot un objet, celui-ci est alors capable de parcourir l’espace, reconnaître l’objet, et se diriger vers celui-ci.
 
2. Les technologies et matériels utilisés
2.1 Hardware
Raspberry Pi 3 + Gopigo
Capteur ultrason
MicroSD Card
Cable de liaison
Camera
Module Wi-fi
 
2.2 Software
Os : Rasbian
Langages de programmation : Python
Bibliothèques utiles : Python Anaconda, Pandas, Gensim, Keras, Tensorflow
 
3. Détails d’implémentations
L’implémentation se décompose en deux parties distinctes : 
3.1 Déplacement du robot
La première phase du projet consistera à développer un algorithme donnant au robot la capacité de “fouiller” au sein de son environnement. L’idéal serait également de parvenir à optimiser les déplacements du robot pour que celui-ci trouve le chemin le plus court vers son objectif. Pour communiquer l’objet au robot, nous prévoyons dans un premier temps de lancer les instructions via notre ordinateur, mais si le temps nous le permet, il serait intéressant de développer une application Android dédiée.
Nous envisageons dans un premier temps de créer un espace quadrillé, à chaque intersection, le cerveau moteur, équipé de la caméra effectue une rotation. Si l’objet est détecté, le robot devra trouver le chemin le plus court, sinon, il se dirige vers la prochaine intersection. L’idée est également de complexifier le quadrillage au fur et à mesure des implémentations afin de valider notre modèle.
 

 
 
 
3.1 Machine learning
Création du corpus ou dataset : Le robot devra dans un premier reconnaître des items comme un fruit (citron, pomme, etc …), ou des objets usuels (ballon, téléphone etc ..). Le réseau de neurones sera donc entraîné sur ce type d’image.

Une fois le modèle généré il faudra évaluer chacunes des images fourni par la caméra. Si on obtient une probabilité satisfaisante, le robot devra alors se diriger vers l’objet.  Une optimisation sera nécessaire afin d’obtenir un bon compromis entre le temps d’évaluation et les performances de reconnaissance.



 
 
 

