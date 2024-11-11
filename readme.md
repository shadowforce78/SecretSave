# PasswordManager 🔒

**PasswordManager** est une application de gestion de mots de passe sécurisée, conçue pour faciliter l'enregistrement et la récupération de vos identifiants tout en assurant la confidentialité de vos données. Le projet utilise le chiffrement pour stocker les informations de manière sécurisée, ce qui garantit que vos données restent protégées même en cas d'accès non autorisé.

---

## Table des matières

1. [Aperçu des branches](#aperçu-des-branches)
2. [Fonctionnalités](#fonctionnalités)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Contributions](#contributions)

---

## Aperçu des branches

Ce projet comporte deux branches principales :

1. **Branch `TerminalV1`** :

   - Contient le code pour une application à exécuter dans le terminal.
   - Version simple et légère, idéale pour une utilisation en ligne de commande.

2. **Branch `CustomTkinterV1`** :
   - Contient le code pour une application graphique utilisant la bibliothèque `CustomTkinter`.
   - Version avec interface utilisateur graphique (GUI) pour une expérience plus intuitive.

Chaque branche est autonome et propose la même base fonctionnelle, mais avec des modes d’interaction différents.

## Fonctionnalités

- **Création d'utilisateurs** : Enregistrement sécurisé de chaque utilisateur avec un identifiant unique.
- **Ajout de mots de passe** : Enregistrement et sauvegarde de mots de passe associés à des sites ou services.
- **Chiffrement des données** : Stockage chiffré des informations pour une sécurité optimale.
- **Gestion des comptes** : Accès aux informations de connexion uniquement après vérification des identifiants.

---

## Installation

### Pré-requis

- **Python 3.x**
- **Modules nécessaires** : Installez les dépendances en exécutant :

  ```bash
  pip install -r requirements.txt
  ```

### Clonage du dépôt

1. Clonez le dépôt sur votre machine en utilisant la commande suivante :

```bash
git clone https://github.com/shadowforce78/SecretSave/
cd SecretSave
```

2. Accédez à la branche souhaitée en utilisant la commande :

- **Branch `TerminalV1`** :

  ```bash
  git checkout TerminalV1
  ```

- **Branch `CustomTkinterV1`** :

  ```bash
    git checkout CustomTkinterV1
  ```

---

## Utilisation

Version Terminal
Une fois la branche TerminalV1 sélectionnée :

```bash
python main.py
```


Version Graphique (CustomTkinter)
Après avoir changé pour la branche CustomTkinterV1 :

```bash
python main.py
```
L'interface graphique s'affichera et vous pourrez interagir avec le gestionnaire de mots de passe de manière intuitive.

---

## Contributions

Les contributions sont les bienvenues ! Pour contribuer, veuillez suivre ces étapes :

- Fork le dépôt.
- Créez une branche (`feature/ma-feature`).
- Commitez vos modifications.
- Poussez la branche.
- Créez une Pull Request.
