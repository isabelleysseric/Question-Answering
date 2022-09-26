# TP 3 du cours de traitement de la langue naturelle

Ce programme utilise Keras pour créer et utiliser le modèle de Deep Learning.

Vous pouvez installer l'environnement necessaire grâce à conda via la commande 



```
conda create --name <env> --file requirements.txt
```

ou alors

```
conda env create -f environment.yml
```

# How to use

Le programme s'excecute avec la commande 

```
python main.py
```

Il est posible d'ajouter l'argument -n pour définir le nombres de documents maximal à retourner. Exemple: 

```
python main.py -n 5
```

va retourner les 5 documents les plus probables pour répondre à la question.

Une fois le programme exécuté, un prompt s'affichera ou il suffira de remplir la question.

Pour fermer le prompt et le programme, vous pouvez entrer 'exit' dans le prompt.
