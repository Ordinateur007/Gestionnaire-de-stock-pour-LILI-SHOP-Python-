# 👟 LILI-SHOP — Gestionnaire de Stock & E-Commerce (Python)

Bienvenue dans le dépôt du projet **LILI-SHOP**, un système complet de gestion de stock, d'articles, de clients et de commandes conçu spécifiquement pour une boutique e-commerce de chaussures et sneakers.

---

## 📌 Présentation du Projet

Ce projet a pour objectif de fournir un outil simple, léger et modulaire pour administrer le catalogue et les ventes de **LILI-SHOP**. Il permet d'effectuer l'ensemble des opérations CRUD (Création, Lecture, Mise à jour, Suppression) sur les articles, de gérer le suivi des clients et de traiter les commandes en temps réel.

### 🎯 Fonctionnalités Principales
- **Gestion des Articles / Stock :**
  - Ajout d'articles avec génération automatique d'identifiants uniques (`ID` et `SKU`).
  - Suivi des caractéristiques clés : marque, pointure, couleur, prix, quantité et seuil d'alerte de stock.
  - Recherche rapide par SKU ou critère.
  - Mise à jour du stock lors des réapprovisionnements ou des ventes.
- **Gestion des Clients :**
  - Création de fiches clients avec coordonnés (nom, prénom, e-mail, téléphone, adresse).
  - Génération automatique d'ID client.
- **Gestion des Commandes :**
  - Enregistrement des commandes associant articles et clients.
  - Calcul automatique du montant total.
  - Suivi du statut de livraison et moyen de paiement.
- **Persistance des Données :**
  - Sauvegarde et chargement automatique du stock au format JSON (`stock.json`).

---

## 🏗️ Architecture du Projet

Le projet est structuré selon les principes de séparation des responsabilités afin d'assurer un code propre, lisible et maintenable :

```text
lili_shop/
│
├── structure.py          # Modèles de données & Générateurs d'identifiants uniques
├── gestionnaire.py       # Logique métier (Fonctions d'ajout, recherche, mise à jour, persistance JSON)
├── main.py               # Interface utilisateur CLI (Menu interactif en ligne de commande)
├── stock.json            # Base de données locale (Fichier de persistance des données)
└── README.md             # Documentation du projet
