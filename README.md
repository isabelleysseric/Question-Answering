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


**Teammates**:
- Isabelle Eysseric
- Nicolas Garde
- David Poisson
<br/>
<br/>


This program uses Keras to create and use the Deep Learning model.  

You can install the necessary environment using conda via the command.  



```
conda create --name <env> --file requirements.txt
```

or else

```
conda env create -f environment.yml
```

# How to use it

The program is executed with the command.

```
python main.py
```

It is possible to add the argument -n to define the maximum number of documents to return. Example:

```
python main.py -n 5
```

It will return the 5 most likely documents to answer the question.

Once the program is executed, a prompt will be displayed where you just have to fill in the question.

To close the prompt and the program, you can enter 'exit' in the prompt.


