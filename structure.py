# --- COMPTEURS D'IDENTIFIANTS UNIQUES ---
_compteur_article_id = 0
_compteur_commande_id = 0
_compteur_client_id = 0


def generer_id_article_id():
    """Génère un ID unique incrémenté pour chaque article."""
    global _compteur_article_id
    _compteur_article_id += 1
    return _compteur_article_id


def generer_id_commande():
    """Génère un ID unique incrémenté pour chaque commande."""
    global _compteur_commande_id
    _compteur_commande_id += 1
    return _compteur_commande_id


def generer_id_client():
    """Génère un ID unique incrémenté pour chaque client."""
    global _compteur_client_id
    _compteur_client_id += 1
    return _compteur_client_id


# --- LOGIQUE MÉTIER / CALCUL AUTOMATIQUE ---

def calculer_statut(quantite, seuil_alerte):
    """
    Détermine automatiquement le statut selon la quantité réelle et le seuil fixé.
    """
    if quantite <= 0:
        return "Rupture de stock"
    elif quantite <= seuil_alerte:
        return "Stock bas"
    else:
        return "Disponible"


# --- CONSTRUCTEURS DE DICTIONNAIRES ---

def creer_article(sku, nom, marque, pointure, prix, quantite, couleur, seuil_alerte=3):
    """
    Crée et retourne un dictionnaire représentant un article.
    Le statut est calculé AUTOMATIQUEMENT.
    """
    return { 
        "id": generer_id_article_id(),
        "sku": sku,
        "nom": nom,
        "marque": marque,
        "pointure": pointure,
        "prix": prix,
        "quantite": quantite,
        "couleur": couleur,
        "seuil_alerte": seuil_alerte,
        "statut": calculer_statut(quantite, seuil_alerte)
    }


def creer_commande(id_article, id_client, date_commande, articles_commandes, total, statut, adresse_livraison, moyen_paiement, numero_suivi):
    """
    Crée et retourne un dictionnaire représentant une commande.
    """
    return {
        "id_commande": generer_id_commande(),
        "id_article": id_article,
        "id_client": id_client,
        "date_commande": date_commande,
        "articles_commandes": articles_commandes,
        "total": total,
        "statut": statut,
        "adresse_livraison": adresse_livraison,
        "moyen_paiement": moyen_paiement,
        "numero_suivi": numero_suivi
    }


def creer_client(nom, prenom, email, telephone, adresse_defaut):
    """
    Crée et retourne un dictionnaire représentant un client.
    """
    return {
        "id_client": generer_id_client(),
        "nom": nom,
        "prenom": prenom,
        "email": email,
        "telephone": telephone,
        "adresse_defaut": adresse_defaut
    }