# spacecrypto.me 🪐

---
🟢 = Terminé
🟠 = En cours
🔴 = Pas commencé

**Le site web :**

- Graphique de trading (Style TradingView, hausse/baisse) 🟢
- Page d'informations sur fees, blockchain, feer and gread -> Mempool (Sur le terrain) 🟠
- Page d'informations sur les cryptos (projet, évolution du prix, marketcap) 🔴
- Système d'alerte si prix hit x $ (choix vers discord ou telegram) 🟠
- Monitoring de wallet (crypto, levier, price) exemple : cryptomoonitor.io 🟢
- Possibilité d'ajouter son wallet sur discord via webhook 🟢
- Monitoring via panel admin 🟠
- Déploiement de la solution via ansible 🟠

**Sécurisation de l'infrastructure :**

➜ Sécuriser les ports 🔴

➜ HTTP -> HTTPS 🔴

➜ Cloudflare 🔴

➜ Déploiement sécurisé de la solution via ansible 🟠

---

**Roadmap : 🧾** 

**[J/M/A]** + Actions..

**[04/01/22]** Choix du projet, mise en place de nos idées ainsi que des ressources nécessaires

**[11/01/22]** Création du serveur web avec Python Flask + début du monitoring de wallet crypto

**[17/01/22]** Installation de graphana + influxdb, début de création du graphique avec prix Bitcoin + fin du wallet crypto

**[18/01/22]** Ajout du wallet crypto via discord webhook + début de la page d'informations sur les fees

**[01/02/22]** Ajout des nodes blockchain aux graphiques + création du déploiement de la solution via ansible

---

**A venir : ❗️**

- Que du vert partout 🟢
- Préparation de la documentation
- Préparation de l'oral


# Documentation

**Prérequis ⚙️ :** 
- Machine : 1 (2 si votre machine personnelle ne possède pas Linux)
- RAM / CPU : 2048 / 1
- OS : Ubuntu 20.04

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

**Schéma de l'installation ⏳ :**

<img src="https://cdn.discordapp.com/attachments/497025479233241099/939972398663471164/unknown.png">


**Comment l'utiliser 🕹 :**

Voilà vous avez maintenant la solution utilisable à l'adresse : https://localhost:5000

Les différentes routes sont :

- /
- /dashboard
- /add_crypto
- ADD AUTRES ROUTES

**Monitoring 👨🏼‍💻 :**

Au niveau du monitoring du serveur web, il se fait via le panel admin de Grafana sans que vous n'ayez rien à toucher, profitez de la simplicité.

Login : 

**Backup 📑 :**

Tout les dossiers et database sont montables depuis le playbook d'ansible

⛔️ Attention, les données liées à la DB des utilisateurs dans dashboardV1.db ne sont pas sauvegardés (Par manque de temps).

Je vous propose tout de même une solution pour les **stocker** et les **sauvegarder** : 

Vous devez ajouter une nouvelle machine qui sera un espace dédié au stockage des sauvegardes dans un disque dur particulier.
Je propose pour le partage des données le protocole **NFS** : 
C'est un protocole très simple permettant d'échanger des fichiers entre deux machines.

**Veuillez procéder comme ceci 👨‍🏫 :**

Comme dit plus haut installe le serveur de backup avant tout.

- I. Ajout de disque
- II. Partitioning
- Partitionner le disque à l'aide de LVM
- Formater la partition
- Monter la partition
- III. Install du serveur NFS + conf (N'oubliez pas de démarrer le service)
- IV. Faire de même cette fois ci sur le serveur web
- V. Faites un service qui s'occupera de faire les sauvegardes de manière  régulière et de les envoyer sur votre backup

Je vais pas tout faire pour vous donc tout est expliqué dans les grandes lignes, vous avez un tuto efficace par it4 ici 👇🏻

it4 Gitlab : https://gitlab.com/it4lik/b1-linux-2021/-/tree/master/tp/6
