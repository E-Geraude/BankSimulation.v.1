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

### Relations :
- **Composition** : La banque possède une relation de composition avec **Client**, **Compte** et **Transaction**, car elle gère leur cycle de vie.

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

### Relations :
- **Association** avec **Client** : Une personne peut devenir client (sans forcément avoir de compte au départ) ou interagir avec un client en envoyant de l’argent.

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

### Relations :
- **Association** avec **Compte** : Un client peut avoir plusieurs comptes.
- **Association** avec **Transaction** : Un client peut initier ou recevoir plusieurs transactions.

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

### Relations :
- **Association** avec **Client** : Un compte appartient à un client.
- **Association** avec **Transaction** : Un compte peut être impliqué dans plusieurs transactions (en tant que source ou destination).

---

### 5. **Transaction**
- **Rôle** : Représente un transfert d’argent entre deux comptes.
- **Attributs** :
  - `montant` : Montant de la transaction.
  - `dateTransaction` : Date de la transaction.
  - `source` : Compte source d'où provient l'argent.
  - `destination` : Compte destinataire de la transaction.
  - `etat` : État de la transaction (en attente, réussie, échouée).
- **Méthodes** :
  - `executer()` : Exécute la transaction en mettant à jour les soldes des comptes.
  - `annuler()` : Annule une transaction, si nécessaire, et effectue les remboursements.
  - `verifierFondsSuffisants()` : Vérifie si le compte source a suffisamment de fonds pour la transaction.
  - `afficherDetails()` : Affiche les détails complets de la transaction.
  - `confirmer()` : Confirme l’exécution réussie de la transaction.
  - `enregistrerHistorique()` : Enregistre la transaction dans l’historique des comptes concernés.
  - `calculerFrais()` : Calcule les frais associés à la transaction, s'il y en a.

### Relations :
- **Association** avec **Compte** : Une transaction implique toujours deux comptes (source et destination).
- **Association** avec **Client** : Un client est toujours l'initiateur ou le destinataire d'une transaction.
- **Dépendance** : La transaction dépend des états des comptes impliqués pour pouvoir s'exécuter correctement.

---

## **Relations clés**

- **Banque → Client, Compte, Transaction (Composition)** : La banque gère les clients, comptes, et transactions.
- **Client → Compte (Association)** : Un client peut posséder plusieurs comptes.
- **Compte → Transaction (Association)** : Un compte est impliqué dans plusieurs transactions.
- **Transaction → Client, Compte (Association)** : Une transaction implique toujours des comptes et des clients.
- **Personne → Client (Possibilité d’évolution)** : Une personne peut devenir client en ouvrant un compte.

---

## **Principaux concepts ajoutés**

### 1. **Personne sans compte**
- Une personne peut interagir avec la banque (envoyer de l’argent à un client) sans avoir de compte.

### 2. **Client sans compte au départ**
- Un client peut exister sans compte. Tant qu’il n'a pas de compte, il peut uniquement envoyer de l’argent ou ouvrir un compte pour bénéficier de toutes les fonctionnalités.

---

Fin de la première version du projet.
