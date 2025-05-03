# 🌍 Explorateur de monde

Application Flask pour découvrir les pays du monde, les ajouter à une liste de pays à visiter, et jouer à un quiz géographique.

## Prérequis
- Python
- Accès à internet (l'application utilise des API publiques)

## Installation

1. Clonez ou téléchargez le projet :
```bash
git clone <lien-du-repo>
cd nom-du-projet
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
```

3. Activez l'environnement virtuel :
- Sous Linux/macOS :
```bash
source venv/bin/activate
```
- Sous Windows :
```bash
venv\Scripts\activate
```

4. Installez les dépendances :
```bash
pip install -r requirements.txt
```

5. Lancez l'application :
```bash
python app.py
```

6. Ouvrez votre navigateur à l'adresse :
```
http://localhost:5000
```

## Fonctionnalités
- 🌐 Carte interactive du monde
- 📍 Cliquer sur un pays pour afficher ses détails
- ✅ Ajouter un pays à votre liste de souhaits
- 🧠 Jouer à un quiz sur les pays
- 📋 Visualiser, supprimer des pays de la liste

## Structure du projet
```
├── app.py               # Point d'entrée Flask
├── templates/           # Fichiers HTML (Jinja2)
├── static/              # Fichiers JS, CSS, images
├── models/              # Modèle de base de données
├── views/               # Routes Flask séparées
├── requirements.txt     # Dépendances Python
└── README.md            # Ce fichier
```

## API utilisées
- [REST Countries](https://restcountries.com)
- [BigDataCloud Reverse Geocoding](https://www.bigdatacloud.com/)
- [OpenStreetMap / Leaflet](https://leafletjs.com)

## Auteur
Projet étudiant réalisé pour l'apprentissage de Flask + intégration API.