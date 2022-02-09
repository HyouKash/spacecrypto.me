# spacecrypto.me 🪐

---
🟢 = Terminé

🟠 = En cours

🔴 = Pas commencé

**Le site web :**

- Graphique de trading (Style TradingView, hausse/baisse) 🟢
- Page d'informations sur blockchain (Sur Grafana) 🟢
- Système d'alerte si prix hit x $ (choix vers discord ou telegram) 🟢
- Monitoring de wallet (crypto, levier, price) exemple : cryptomoonitor.io 🟢
- Possibilité d'ajouter son wallet sur discord via webhook 🟠 (run le script webhook dans un service)
- Monitoring via panel admin Grafana 🟢
- Déploiement de la solution via ansible 🟢
- Changer l'image dans prérequis (obsolète) 🔴

**Sécurisation de l'infrastructure :**

➜ Sécuriser les ports (iptable) 🟢

➜ HTTP -> HTTPS w/Certbot 🔴

➜ Cloudflare 🔴

➜ Déploiement sécurisé de la solution via ansible 🟢

---

**Roadmap : 🧾** 

**[J/M/A]** + Actions..

**[04/01/22]** Choix du projet, mise en place de nos idées ainsi que des ressources nécessaires

**[11/01/22]** Création du serveur web avec Python Flask + début du monitoring de wallet crypto

**[17/01/22]** Installation de graphana + influxdb, début de création du graphique avec prix Bitcoin + fin du wallet crypto

**[18/01/22]** Ajout du wallet crypto via discord webhook + début de la page d'informations sur les fees

**[01/02/22]** Ajout des nodes blockchain aux graphiques + création du déploiement de la solution via ansible

**[08/02/22]** Fin de la config ansible avec gestions de permissions clean, documentation terminée, sécurisation des ports -> drop/reject (plus nmappable) sur les port :9100 :9090 :8333 :8086 mais marche sur localhost, changement du port du site web -> 80

---

**A venir : ❗️**

- Que du vert partout 🟢
- Préparation de l'oral

# Documentation

**Sommaire :**

[I. Prérequis](https://github.com/HyouKash/spacecrypto.me/blob/main/Documentation/Pr%C3%A9requis.md)

[II. Installation](https://github.com/HyouKash/spacecrypto.me/blob/main/Documentation/Installation.md)

[III. Utilisation](https://github.com/HyouKash/spacecrypto.me/blob/main/Documentation/Utilisation.md)

[IV. Monitoring](https://github.com/HyouKash/spacecrypto.me/blob/main/Documentation/Monitoring.md)

[V. Backup](https://github.com/HyouKash/spacecrypto.me/blob/main/Documentation/Backup.md)

**Liste de tout ce qui marche 📝 :**

- Site web utilisable
- Monitoring de wallet via API
- Monitoring de wallet via discord_webhook
- Monitoring du serveur web via Grafana
- Système d'alerte via Grafana
- Solution déployable grâce à Ansible
- Site web sécurisé par CloudFlare
- Fail2ban sur l'accès SSH du serveur web
- Port sécurisé (Iptable)
- Serveur web sécurisé
- 4 services : Prix du Bitcoin, Serveur web, BitcoinCore et docker
- Database fonctionnelle 
- HTTPS fonctionel

**Informations complémentaires ⛔️ :**

Le service **price** s'occupe de récupérer le prix du bitcoin afin de le mettre dans influx-db puis de l'afficher directement dans un graphique via Grafana.

Le service **BitcoinCore** sert à récupérer directement les blocks de la Blockchain afin de directement communiquer avec eux et avoir les informations nécessaires depuis le début de la blockchain.

Le service **docker** s'occupe de run influx.db
