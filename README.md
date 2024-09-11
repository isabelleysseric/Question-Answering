<h1 align='center'>Question / Answer System with Wikipedia Corpus<br><i>Expert System with Corpus</i></h1>

<p align='center'>
  <img src=https://github.com/isabelleysseric/Question-Answering/blob/master/images/nlp-qa-etape5.png" alt="Expert System with Corpus"/>
</p>

<h2 align="center">    

  <!-- GitHub -->
  <a href="https://github.com/isabelleysseric/">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" >
  </a>  

  <!-- Project Repo -->
  <a href="https://github.com/isabelleysseric/Question-Answering/">
    <img src="https://img.shields.io/badge/Repo-Question_Answering-green?style=for-the-badge&logo={Question-Answering}&logoColor=white" >
  </a>

  <!-- Wiki Project -->
  <a href="https://github.com/isabelleysseric/Question-Answering/wiki/">
    <img src="https://img.shields.io/badge/Wiki-Question_Answering-green?style=for-the-badge&logo={Question-Answering}&logoColor=white" >
  </a><br>
    
  <!-- AI Page -->
  <a href="https://isabelleysseric.ai/">
    <img src="https://img.shields.io/badge/AI-Page-blue?style=for-the-badge&logo={AI-Page}&logoColor=white" >
  </a>
    
  <!-- Portfollio -->
  <a href="https://isabelleysseric.com/Resume.html">
    <img src="https://img.shields.io/badge/Portfollio-bfbfbf?style=for-the-badge&logo={Portfollio}&logoColor=white" >
  </a>
    
  <!-- LinkedIn -->
  <a href="https://www.linkedin.com/in/isabelleysseric/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" >
  </a>
  <!-- GMAIL -->
  <a href="mailto: isabelleysseric@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" >
  </a>
  
  <!-- Docker Hub -->
  <a href="https://hub.docker.com/u/isabelleysseric">
    <img src="https://img.shields.io/badge/Docker_Hub-2496ED?style=for-the-badge&logo={dockerhub}&logoColor=#2496ed" >
  </a>

  <!-- Gazebo Sim -->
  <a href="https://hub.docker.com/u/isabelleysseric">
    <img src="https://img.shields.io/badge/Gazebo_Sim-orange?style=for-the-badge&logo={gazebosim}&logoColor=#2496ed" >
  </a><br>
  
</h2>
<br>


**Co-équipiers**:  
- Isabelle Eysseric
- Nicolas Garde
- David Poisson
<br/>
<br/>


Ce programme utilise Keras pour créer et utiliser le modèle de Deep Learning.

Vous pouvez installer l'environnement necessaire grâce à conda via la commande 



```
conda create --name <env> --file requirements.txt
```

ou alors

```
conda env create -f environment.yml
```

# Comment l'utiliser

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
