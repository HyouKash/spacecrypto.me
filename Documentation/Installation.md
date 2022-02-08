**Comment installer la solution 🛠 :**

Vidéo : Coming Soon



A l'écrit :

1. Installer la machine et avoir un accès ssh root sans mot de passe

Si besoin d'aide : https://askubuntu.com/questions/115151/how-to-set-up-passwordless-ssh-access-for-root-user#:~:text=On%20the%20client%20(where%20you%20ssh%20FROM)&text=When%20you%20are%20prompted%20for,to%20ssh%20into%20the%20server.

2. Installer ansible (par Python conseillé) sur votre machine personnelle (Linux only)

```bash
pip install ansible
```

3. Cloner le repo via un terminal de commande sur votre ordinateur

```bash 
sudo git clone https://github.com/HyouKash/spacecrypto.me.git

OU

wget https://github.com/HyouKash/spacecrypto.me.git
```

4. Se rendre dans le dossier "ansible" et éditer via un éditeur de texte le fichier hosts.txt afin d'y insérer l'IP de votre machine

5. Lancer le play-book

```bash 
ansible-playbook -i hosts playbook.yml
```
