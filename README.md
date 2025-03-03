# BankSimulation.v.1

# **Projet : Simulation de Banque (Version 1)**

## **Concept général**

Le projet consiste en la simulation d'une banque où les clients peuvent interagir entre eux, effectuer des transactions (dépôts, retraits, transferts), qu'ils soient clients de la même banque ou non. Il est également possible pour une personne extérieure d’envoyer de l’argent à un client existant sans posséder de compte bancaire.

---

## **Classes et relations principales**

### 1. **Banque**
- **Rôle** : Gère les clients, les comptes, et les transactions.
- **Attributs** :
  - `nom` : Le nom de la banque.
  - `listeClients` : Liste des clients de la banque.
  - `listeComptes` : Liste des comptes ouverts dans la banque.
  - `listeTransactions` : Liste des transactions effectuées dans la banque.
- **Méthodes** :
  - `ajouterClient(Client client)` : Ajoute un client à la banque.
  - `supprimerClient(Client client)` : Supprime un client de la banque.
  - `trouverClientParId(String idClient)` : Recherche un client en fonction de son identifiant.
  - `creerCompte(Client client, double soldeInitial)` : Crée un compte pour un client avec un solde initial.
  - `effectuerTransaction(Compte source, Compte destination, double montant)` : Effectue un transfert entre deux comptes.
  - `afficherTousClients()` : Affiche la liste de tous les clients.
  - `afficherToutesTransactions()` : Affiche l’historique de toutes les transactions.

---

### 2. **Personne**
- **Rôle** : Représente une personne générale dans le système, qu’elle ait ou non un compte bancaire.
- **Attributs** :
  - `nom`
  - `prenom`
  - `adresse`
  - `email`
  - `telephone`
- **Méthodes** :
  - `envoyerArgent(Client destinataire, double montant)` : Envoie de l’argent à un client.
  - `devenirClient(Banque banque)` : Devient un client en ouvrant un compte.
  - `afficherInfos()` : Affiche les informations de la personne.

---

### 3. **Client** (hérite de **Personne**)
- **Rôle** : Représente une personne ayant un ou plusieurs comptes bancaires.
- **Attributs supplémentaires** :
  - `listeComptes` : Liste des comptes du client.
  - `estClient` : Indique si la personne possède un compte.
- **Méthodes** :
  - `ouvrirCompte(Banque banque, double soldeInitial)` : Ouvre un compte bancaire.
  - `consulterComptes()` : Consulter les comptes du client.
  - `effectuerTransfert(Compte source, Compte destination, double montant)` : Effectuer un transfert d’argent.
  - `deposerArgent(Compte compte, double montant)` : Déposer de l'argent sur un compte.
  - `retirerArgent(Compte compte, double montant)` : Retirer de l’argent d’un compte.
  - `afficherHistoriqueTransactions()` : Afficher l'historique des transactions.

---

### 4. **Compte**
- **Rôle** : Représente un compte bancaire d’un client.
- **Attributs** :
  - `numeroCompte` : Numéro unique du compte.
  - `solde` : Solde actuel du compte.
- **Méthodes** :
  - `deposer(double montant)` : Ajoute un montant au solde.
  - `retirer(double montant)` : Retire un montant si le solde est suffisant.
  - `afficherSolde()` : Affiche le solde du compte.

---

### 5. **Transaction**
- **Rôle** : Représente un transfert d’argent entre deux comptes.
- **Attributs** :
  - `montant` : Montant de la transaction.
  - `dateTransaction` : Date de la transaction.
- **Méthodes** :
  - `executer()` : Exécute la transaction en mettant à jour les soldes des comptes.

---

## **Relations clés**

- **Banque → Client, Compte, Transaction (Composition)** : La banque gère les clients, comptes, et transactions.
- **Client → Compte (Association)** : Un client peut posséder plusieurs comptes.
- **Compte → Transaction (Association)** : Un compte est impliqué dans plusieurs transactions.
- **Personne → Client (Possibilité d’évolution)** : Une personne peut devenir client en ouvrant un compte.

---

## **Principaux concepts ajoutés**

### 1. **Personne sans compte**
- Une personne peut interagir avec la banque (envoyer de l’argent à un client) sans avoir de compte.

### 2. **Client sans compte au départ**
- Un client peut exister sans compte. Tant qu’il n'a pas de compte, il peut uniquement envoyer de l’argent ou ouvrir un compte pour bénéficier de toutes les fonctionnalités.

---

Fin de la première version du projet.

---
