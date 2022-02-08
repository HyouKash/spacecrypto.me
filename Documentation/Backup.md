**Backup 📑 :**

Tout les dossiers et database sont montables depuis le playbook d'ansible

⛔️ Attention, les données liées à la DB des utilisateurs dans dashboardV1.db ne sont pas sauvegardés (Par manque de temps).

Je vous propose tout de même une solution pour les **stocker** et les **sauvegarder** : 

Vous devez ajouter une nouvelle machine qui sera un espace dédié au stockage des sauvegardes dans un disque dur particulier.
Je propose pour le partage des données le protocole **NFS** : 
C'est un protocole très simple permettant d'échanger des fichiers entre deux machines.

Veuillez procéder comme ceci 👨‍🏫 : 

Comme dit plus haut installe le serveur de backup avant tout.

- 1. Ajout de disque
- 2. Partitioning
- Partitionner le disque à l'aide de LVM
- Formater la partition
- Monter la partition
- 3. Install du serveur NFS + conf (N'oubliez pas de démarrer le service)
- 4. Faire de même cette fois ci sur le serveur web
- 5. Faites un service qui s'occupera de faire les sauvegardes de manière  régulière et de les envoyer sur votre backup

Je vais pas tout faire pour vous donc tout est expliqué dans les grandes lignes, vous avez un tuto efficace par it4 ici 👉🏼 [it4 Gitlab](https://gitlab.com/it4lik/b1-linux-2021/-/tree/master/tp/6)

--- 

**➔ Informations :** [README](https://github.com/HyouKash/spacecrypto.me/blob/main/README.md)
