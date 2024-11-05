# 🗄️ Script de Sauvegarde des Registres Windows

## 📋 Description
Ce projet contient un script Python pour sauvegarder de manière sécurisée des sections critiques du registre Windows (SAM et SYSTEM et adress IP et MAC). Il inclut également un script Batch automatisé qui garantit l’exécution du script Python avec les privilèges nécessaires, rendant le processus de sauvegarde à la fois simple et fiable.

## ✨ Fonctionnalités
- 🔑 **Gestion des privilèges** : Le script Python requiert des privilèges administratifs pour accéder et sauvegarder les hives de registre SAM et SYSTEM. Le script Batch se charge de relancer le script en mode administrateur si nécessaire.
- 🗂️ **Sauvegardes sécurisées** : Le script Python crée un dossier de sauvegarde unique à chaque exécution dans le répertoire Documents, contenant les fichiers `.save` des hives de registre.
- 🤖 **Automatisation avec Batch** : Le script Batch vérifie les permissions, exécute le script Python, et crée un fichier journal (`log`) pour tracer toutes les étapes du processus.

## 🛠️ Prérequis
- Python 3.6 ou supérieur
- Windows OS
- Privilèges administratifs pour l’exécution

## 🚀 Installation
1. Clonez ce dépôt pour obtenir les scripts Python et Batch.
2. Assurez-vous que Python est correctement installé et accessible via le PATH.

## 📂 Utilisation
Lancez simplement le script Batch pour démarrer le processus de sauvegarde automatisé. Ce script gérera les privilèges nécessaires, exécutera le script Python, et enregistrera les opérations dans un fichier journal.

## ⚠️ Avertissements
- 💾 **Sauvegarde du registre** : La manipulation du registre Windows est sensible. Utilisez ce script avec précaution et évitez de partager les fichiers de sauvegarde, car ils peuvent contenir des informations sensibles.
- 🔒 **Exécution en tant qu’administrateur** : Certaines actions nécessitent des privilèges élevés, ce que le script Batch prend en charge automatiquement.

## 🤝 Contribuer
Les contributions sont bienvenues ! Si vous avez des idées pour améliorer le script ou ajouter des fonctionnalités, n'hésitez pas à ouvrir une pull request.

## 📜 Licence
Pas de licence pour le moment. Consultez le fichier LICENSE pour plus de détails.
