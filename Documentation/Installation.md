**Comment installer la solution 🛠 :**

Vidéo : Coming Soon



A l'écrit :

1. Installer la machine avec les [Prérequis](https://github.com/HyouKash/spacecrypto.me/blob/main/Documentation/Pr%C3%A9requis.md).

2. Créez un utilisateur **web**, choisissez un mot de passe, puis faites entrer à chaque fois. Enfin donnez des permissions à l'utilisateur web.

```bash
sudo adduser web 
sudo usermod -aG sudo web
```

3. Copiez votre clé SSH publique ou générez la puis copiez la si vous n'en possédez pas.

```bash 
ssh-keygen -t rsa

ssh-copy-id /home/{votre user}/.ssh/id_rsa.pub web@{IP de votre serveur}
```

4. Installer ansible (par Python conseillé) sur votre machine personnelle Linux, si vous n'en possédez pas un, veuillez installer une deuxième machine et reproduire l'étape de la génération de clé + copie.

```bash
pip install ansible
```

5. Cloner le repo via un terminal de commande sur votre ordinateur

```bash 
sudo git clone https://github.com/HyouKash/spacecrypto.me.git

OU

wget https://github.com/HyouKash/spacecrypto.me.git
```

6. Se rendre dans le dossier "ansible" et éditer via un éditeur de texte le fichier hosts.txt afin d'y insérer l'IP de votre machine, cela ressemblera à ça si vous l'affichez.

```bash 
cat hosts.txt
[web]
IP ICI 
```

7. Lancer le playbook et rentrer le mot de passe.

```bash 
ansible-playbook -i hosts playbook.yml -K
BECOME password:
```
