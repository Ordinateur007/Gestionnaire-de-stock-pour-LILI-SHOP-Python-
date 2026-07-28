# On importe les fonctions de création construites dans structure.py
from structure import creer_article, creer_client, creer_commande

# Nos bases de données temporaires (en mémoire RAM)
stock_articles = []
liste_clients = []
liste_commandes = []

# --- FONCTIONS DE GESTION DU STOCK ---

def ajouter_article(sku, nom, marque, pointure, prix, quantite, couleur, seuil_alerte=3, statut="disponible"):
    """
    Crée un article et l'ajoute au stock.
    """
    article = creer_article(sku, nom, marque, pointure, prix, quantite, couleur, seuil_alerte, statut)
    stock_articles.append(article)
    print(f"✅ Article '{nom}' (ID: {article['id']}) ajouté avec succès au stock LILI-SHOP !")
    return article

def afficher_stock():
    """
    Affiche l'ensemble des articles présents dans le stock.
    """
    if not stock_articles:
        print("📦 Le stock est actuellement vide.")
        return

    print("\n*** 📦 STOCK ACTUEL LILI-SHOP ***")
    for art in stock_articles:
        print(f"ID: {art['id']} | SKU: {art['sku']} | Nom: {art['nom']} | Pointure: {art['pointure']} | Prix: {art['prix']} FCFA | Qté: {art['quantite']}")
    print("*************************************\n")

def rechercher_article_par_id(id_article):
    """
    Recherche et retourne un article par son ID.
    """
    for art in stock_articles:
        if art["id"] == id_article:
            return art
    return None

# --- TEST DE L'ALGORITHME---
if __name__ == "__main__":
    # Test d'ajout
    ajouter_article("CHAUSS-001", "Basket Nike Air", "Nike", 42, 35000, 10, "Noir")
    ajouter_article("CHAUSS-002", "Mocassin Cuir", "Zara", 41, 25000, 5, "Marron")
    
    # Test d'affichage
    afficher_stock()