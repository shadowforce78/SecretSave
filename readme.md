# 🔐 Gestionnaire de Mots de Passe

### Description

Ce gestionnaire de mots de passe est conçu pour offrir un stockage sécurisé de tes mots de passe en utilisant le chiffrement AES. Grâce à une **clé maître**, les mots de passe sont protégés contre les accès non autorisés et stockés dans un fichier sécurisé. Ce projet est pensé pour une utilisation simple et rapide en ligne de commande.

---

## 🚀 Fonctionnalités

- **Génération de mots de passe** : Crée des mots de passe forts aléatoires en un clic.
- **Cryptage sécurisé** : Les mots de passe sont chiffrés avec le protocole `AES` pour une sécurité maximale.
- **Accès sécurisé** : Le gestionnaire est protégé par un mot de passe maître, indispensable pour voir ou gérer les mots de passe.
- **Interface en ligne de commande (CLI)** : Accès rapide et simple aux différentes fonctionnalités.

---

## 📋 To-Do List

### Features à implémenter

- [x] **Initialiser le Projet** : Créer le fichier principal `main.py` et un fichier `.json` ou une base SQLite pour stocker les mots de passe.
- [x] **Mot de Passe Maître** : Mettre en place un système de mot de passe maître pour sécuriser l'accès au gestionnaire.
- [ ] **Générateur de Mots de Passe** : Créer une fonction qui génère des mots de passe forts.
- [ ] **Chiffrement & Déchiffrement** : Utiliser la bibliothèque `cryptography` pour encrypter les mots de passe avant de les stocker.
- [ ] **CRUD des Mots de Passe** : Ajouter les fonctions pour Créer, Lire, Mettre à jour et Supprimer les mots de passe.
- [ ] **Interface CLI** : Configurer une interface ligne de commande avec des options simples pour naviguer dans les fonctionnalités.
- [ ] **Validation de Sécurité** : Vérifier la force des mots de passe lors de la création pour encourager de bonnes pratiques de sécurité.

### Fonctions avancées (nice-to-have)

- [ ] **Expiration des Mots de Passe** : Option pour notifier les mots de passe trop anciens.
- [ ] **Sauvegarde chiffrée** : Créer une option de sauvegarde en fichier `.enc` pour sécuriser les données.
- [ ] **Interface Graphique (UI)** : Implémenter une interface simple en `tkinter` ou `Flask` pour améliorer l’UX.

---

## 🛠️ Installation & Utilisation

### Prérequis

- Python 3.x
- Bibliothèque `cryptography` pour le chiffrement `simple-chalk` pour les couleurs.

### Installation des dépendances

```bash
pip install -r requirements.txt
```
