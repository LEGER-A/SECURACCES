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
