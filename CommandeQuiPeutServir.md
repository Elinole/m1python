# Commande Linux qui peut servir

<code>$ sudo groupadd docker</code>
- Créer le groupe "docker" dans celui des privilégiés pour exécuter des commandes nécessitant sudo

<code>sudo gpasswd -a $USER docker</code>
- Ajouter l'utilisateur actuel (connecté à l'OS Linux) dans le groupe docker

## Pourquoi ?

De cette manière, l'utilisateur pourra utiliser docker sans devoir taper <code>sudo</code> devant la commande.