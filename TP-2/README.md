# Générateur de Mots de Passe et Passphrases

Bienvenue dans le projet de génération de mots de passe et de passphrases. 
Cette application permet de créer des mots de passe sécurisés et des passphrases à partir d'une liste de mots. 
Elle calcule également l'entropie du mot de passe ou de la passphrase générée et évalue sa force.

## Fonctionnalités

1. **Générateur de Mots de Passe** : Génère des mots de passe sécurisés basés sur vos critères :
   - Longueur du mot de passe.
   - Inclusion de majuscules, chiffres et caractères spéciaux.
   - Calcul de l'entropie pour estimer la sécurité du mot de passe.
   - Évaluation de la force du mot de passe (Faible, Moyenne, Forte).

2. **Générateur de Passphrases** : Crée des passphrases basées sur une liste de mots prédéfinis (fichier `diceware_fr.txt`).
   - Vous pouvez spécifier le nombre de mots dans la passphrase.
   - Calcul de l'entropie pour évaluer la sécurité de la passphrase.

## Prérequis

- Python 3.x
- Tkinter pour l'interface graphique.
- Fichier de mots (`diceware_fr.txt`) pour la génération des passphrases.

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers du projet.

```bash
git clone https://github.com/Zoubidou457/ESIEE-IT_Python.git