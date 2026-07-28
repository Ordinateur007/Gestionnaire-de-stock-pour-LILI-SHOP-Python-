from structure import creer_article, creer_client, creer_commande, calculer_statut

# Base de données temporaires (Stockage en mémoire)
stock_articles = []
liste_clients = []
liste_commandes = []


def ajouter_article(sku, nom, marque, pointure, prix, quantite, couleur, seuil_alerte=3):
    """
    Crée un article et l'ajoute au stock global.
    """
    article = creer_article(sku, nom, marque, pointure, prix, quantite, couleur, seuil_alerte)
    stock_articles.append(article)
    print(f"✅ Article '{nom}' (ID: {article['id']}) ajouté au stock !")
    return article


def afficher_stock():
    """
    Affiche tous les articles du stock avec leur état et leurs informations complètes.
    """
    if not stock_articles:
        print("\n📦 Le stock est actuellement vide.")
        return

    print("\n********** 📦 STOCK ACTUEL LILI-SHOP **********")
    for art in stock_articles:
        # Indication visuelle si le stock est bas ou en rupture
        indicateur = ""
        if art['statut'] == "Rupture de stock":
            indicateur = " 🔴 [RUPTURE]"
        elif art['statut'] == "Stock bas":
            indicateur = " ⚠️ [STOCK BAS]"

        print(f"ID: {art['id']} | SKU: {art['sku']} | Nom: {art['nom']} ({art['marque']}){indicateur}")
        print(f"   ├─ Pointure: {art['pointure']} | Couleur: {art['couleur']} | Prix: {art['prix']} FCFA")
        print(f"   ├─ Quantité: {art['quantite']} paires (Seuil alerte: {art['seuil_alerte']})")
        print(f"   └─ Statut: {art['statut']}")
        print("-" * 65)
    print("***********************************************\n")


def rechercher_article_par_id(id_article):
    """
    Recherche un article dans le stock via son ID unique.
    """
    for art in stock_articles:
        if art["id"] == id_article:
            return art
    return None


def modifier_quantite(id_article, nouvelle_quantite):
    """
    Met à jour la quantité d'un article et recalcule automatiquement son statut.
    """
    article = rechercher_article_par_id(id_article)
    if article is None:
        print(f"❌ Article avec ID {id_article} introuvable.")
        return

    article["quantite"] = nouvelle_quantite
    # Ajustement automatique du statut
    article["statut"] = calculer_statut(article["quantite"], article["seuil_alerte"])
    print(f"🔄 Quantité mise à jour pour '{article['nom']}'. Nouveau statut : {article['statut']}")


def afficher_alertes():
    """
    Affiche uniquement les articles qui nécessitent un réapprovisionnement.
    """
    alertes = [art for art in stock_articles if art["quantite"] <= art["seuil_alerte"]]

    if not alertes:
        print("\n✅ Aucun article en alerte de stock.")
        return

    print("\n⚠️ *************ALERTE RÉAPPROVISIONNEMENT *************⚠️")
    for art in alertes:
        print(f"• ID {art['id']} | {art['nom']} ({art['marque']}) - Restant : {art['quantite']} paires (Statut: {art['statut']})")
    print("***********************************************\n")


# ***** ZONE DE TEST DES FONCTIONNALITÉS *****
if __name__ == "__main__":
    print("***** TEST DU GESTIONNAIRE LILI-SHOP *****")

    # 1. Ajout de 3 articles (Stock normal, Stock bas, Rupture)
    ajouter_article("CHAUSS-001", "Basket Nike Air", "Nike", 42, 35000, 10, "Noir", seuil_alerte=3)
    ajouter_article("CHAUSS-002", "Mocassin Cuir", "Zara", 41, 25000, 2, "Marron", seuil_alerte=5)
    ajouter_article("CHAUSS-003", "Escarpin Rouge", "Aldo", 38, 30000, 0, "Rouge", seuil_alerte=2)

    # 2. Affichage complet
    afficher_stock()

    # 3. Affichage des alertes
    afficher_alertes()

    # 4. Modification de quantité (Réapprovisionnement de l'escarpin)
    print("🚚 Réapprovisionnement de l'escarpin rouge (ID 3) +10 paires...")
    modifier_quantite(3, 10)

    # 5. Vérification après mise à jour
    afficher_stock()