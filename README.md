# SECURACCES
Le projet SECURACCES consiste à concevoir et réaliser un système de contrôle d'accès physique sécurisé. L'accès est conditionné à la présentation d'une carte RFID valide, les tentatives d'accès sont enregistrées dans une base de données consultables via une interface web.

## Matériel Utilisé
- Raspberry pi 3 B
- Lecteur RFID RC522
- 2 Cartes / 2 badges RFID
- Carte microcontrôleur ESP32
- Breadboard / Fils pour cablage

### Étapes de déploiement du projets

*Étape 1 
	- Installation de l'os sur la Raspberry. Le SSH par clés est réalisé lors de l'installation. 
	- Mise a jour des paquets et instalation des dépendences python. (python3-pip/python3-venv).
	- Mise en place d'un clone du dépot github "SECURACCES".

*Étape 2 
	- Étude de la partie physique du projet (RadioFrequencyIDentification).
	- Réalisation de test sur la mesure de porté entre le lecteur et les cartes RFID.
	- Rédaction de cette partie dans le rapport.

*Étape 3
	- Analyse des diagrammes UML et SYSML du projet SECURACCES.
	- Documentation de l'analyse dans le rapport de projet.

*Étape 4
	- Élaboration et test du script UID sur l'IDE Arduino, disponible sur Github.
	- Documentation dans le rapport de projet.
	- Test des actionneurs et des LEDS avec un script test des LEDS et BUZZER, disponible sur Github.
	- Analyse et explication dans le rapport de projet.

*Étape 5
	- Installation et configuration de UFW sur le Rasberry. Les ports 22/80/500 sont ouvert, le reste est bloqué.
	- Mise en place d'un programme phython pour recevoir les requêtes sur le Raspberry. Fichier app.py.
	- Connection de ESP32 au réseau Wi-Fi avec le script wifi_http.
	- Mise en place de l'API REST avec le token bearer, la gestion des erreurs et le delai anti-rebond. Script Wifi_http_token_gestion-erreurs_anti-rebond.
	- Capture du trafic HTTP avec tcpdump.
	- Détails des procédures et analyse dans le rapport.

# Procédure d’installation sur Raspberry Pi

## 1 — Clonage du dépôt GitHub

```bash
git clone https://github.com/LEGER-A/SECURACCES.git
```

```bash
cd SECURACCES/Rpi
```

---

# 2 — Création de l’environnement virtuel Python

Création du `venv` :

```bash
python3 -m venv venv
```

Activation de l’environnement :

```bash
source venv/bin/activate
```

Le terminal doit afficher :

```text
(venv)
```

---

# 3 — Installation des dépendances Python

Installation des bibliothèques nécessaires :

```bash
pip install -r requirements.txt
```

Exemple de dépendances installées :

* Flask
* Flask-Bcrypt
* pytest
* Werkzeug

---

# 4 — Initialisation de la base de données SQLite

Exécution du script de création de la base :

```bash
python init_data.py
```

Ce script crée automatiquement :

* la base `id_utilisateurs.db`
* la table `cartes_rfid`
* la table `journaux_acces`
* la table `admins`

---

# 5 — Lancement manuel du serveur Flask

Démarrage du serveur :

```bash
python app.py
```

Le serveur Flask démarre alors sur :

```text
http://192.168.1.45:5000
```

---

# 6 — Mise en place du service systemd

Création du service :

```bash
sudo nano /etc/systemd/system/securacces.service
```

Configuration du fichier :

```ini
[Unit]
Description=SECURACCES Flask API

[Service]
User=util
WorkingDirectory=/home/util/SECURACCES/Rpi
ExecStart=/home/util/SECURACCES/Rpi/venv/bin/python /home/util/SECURACCES/Rpi/app.py

[Install]
WantedBy=multi-user.target
```

---

# 7 — Activation du service

Rechargement des services :

```bash
sudo systemctl daemon-reload
```

Activation automatique au démarrage :

```bash
sudo systemctl enable securacces
```

Démarrage du service :

```bash
sudo systemctl start securacces
```

---

# 8 — Vérification du fonctionnement

Vérification de l’état du service :

```bash
sudo systemctl status securacces
```

Le statut doit afficher :

```text
active (running)
```

---

# 9 — Test de l’API Flask

Depuis un navigateur ou un autre équipement du réseau :

```text
http://192.168.1.45:5000
```

L’API Flask est alors prête à recevoir les requêtes HTTP envoyées par l’ESP32.
