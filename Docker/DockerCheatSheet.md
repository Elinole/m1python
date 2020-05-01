# CHEAT SHEET DOCKER

## PREFIXE
<code>docker</code>

<hr>

### CONTAINERS
#### Lister
<code>ps -a</code>

#### Créer
<code>create (nom_container)</code>

#### Démarrer
<code>start (nom_container)</code>

#### Lancer une commande
<code>run (commande)</code>

#### Stopper
1. Voir la liste des ID des containers

<code>ps -a</code>

2. Supprimer l'ID de la liste

<code>kill (id_container)</code>

#### Supprimer
<code>rm (container)</code>

<hr>

### IMAGES
#### Lister
<code>images</code>

#### Charger
<code>load (fichier tar ou stdin)</code>

#### Construire
<code>build (dockerfile)</code>

#### Créer
<code>commit (container)</code>

#### Tirer
<code>pull (registre)</code>

#### Pousser
<code>push (registre)</code>

#### Supprimer
<code>rmi (image)</code>