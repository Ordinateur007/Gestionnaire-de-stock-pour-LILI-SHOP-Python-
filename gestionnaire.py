#*********************************************************************
# GESTIONNAIRE.PY - Logique métier, stockage JSON et Menu CLI LILI-SHOP
#*********************************************************************

import json
import os
from structure import creer_article, calculer_statut

FICHIER_STOCK = "stock.json"
stock_articles = []


# **** PERSISTANCE DES DONNÉES (JSON) ****

def sauvegarder_stock():
    """Enregistre le stock actuel dans le fichier JSON."""
    try:
        with open(FICHIER_STOCK, "w", encoding="utf-8") as f:
            json.dump(stock_articles, f, ensure_ascii=False, indent=4)
        print("💾 Stock sauvegardé avec succès.")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")


def charger_stock():
    """Charge le stock depuis le fichier JSON s'il existe."""
    global stock_articles
    if not os.path.exists(FICHIER_STOCK):
        print("ℹ️ Aucun fichier 'stock.json' trouvé. Démarrage avec un stock vide.")
        return

    try:
        with open(FICHIER_STOCK, "r", encoding="utf-8") as f:
            stock_articles = json.load(f)
        print(f"📂 {len(stock_articles)} article(s) chargé(s) depuis la base de données.")
    except Exception as e:
        print(f"❌ Erreur lors du chargement : {e}")


# **** FONCTIONS DE GESTION DU STOCK ****

def ajouter_article(sku, nom, marque, pointure, prix, quantite, couleur, seuil_alerte=3):
    """Crée un nouvel article et le sauvegarde."""
    article = creer_article(sku, nom, marque, pointure, prix, quantite, couleur, seuil_alerte)
    stock_articles.append(article)
    sauvegarder_stock()
    print(f"✅ Article '{nom}' (ID: {article['id']}) ajouté avec succès !")


def afficher_stock():
    """Affiche la liste complète des articles du stock."""
    if not stock_articles:
        print("\n📦 Le stock est actuellement vide.")
        return

    print("\n************* 📦 STOCK ACTUEL LILI-SHOP *************")
    for art in stock_articles:
        indicateur = ""
        if art['statut'] == "Rupture de stock":
            indicateur = " 🔴 [RUPTURE]"
        elif art['statut'] == "Stock bas":
            indicateur = " ⚠️ [STOCK BAS]"

        print(f"ID: {art['id']} | SKU: {art['sku']} | Nom: {art['nom']} ({art['marque']}){indicateur}")
        print(f"   ├─ Pointure: {art['pointure']} | Couleur: {art['couleur']} | Prix: {art['prix']} FCFA")
        print(f"   ├─ Quantité: {art['quantite']} paires (Seuil alerte: {art['seuil_alerte']})")
        print(f"   └─ Statut: {art['statut']}")
        print("********************************" * 2)
    print("********************************\n")


def reapprovisionner_article(id_article, quantite_ajoutee):
    """Ajoute une quantité reçue au stock d'un article et met à jour son statut."""
    if quantite_ajoutee <= 0:
        print("❌ La quantité ajoutée doit être supérieure à 0.")
        return

    for art in stock_articles:
        if art['id'] == id_article:
            art['quantite'] += quantite_ajoutee
            art['statut'] = calculer_statut(art['quantite'], art['seuil_alerte'])
            sauvegarder_stock()
            print(f"✅ Réapprovisionnement réussi ! Nouveau stock pour '{art['nom']}' : {art['quantite']} paires ({art['statut']}).")
            return

    print(f"❌ Aucun article trouvé avec l'ID {id_article}.")


def enregistrer_vente(id_article, quantite_vendue=1):
    """Diminue la quantité d'un article suite à une vente."""
    for art in stock_articles:
        if art['id'] == id_article:
            if art['quantite'] < quantite_vendue:
                print(f"❌ Stock insuffisant ! Seulement {art['quantite']} disponible(s).")
                return
            art['quantite'] -= quantite_vendue
            art['statut'] = calculer_statut(art['quantite'], art['seuil_alerte'])
            sauvegarder_stock()
            print(f"🛍️ Vente enregistrée ! Reste pour '{art['nom']}' : {art['quantite']} paires ({art['statut']}).")
            return

    print(f"❌ Aucun article trouvé avec l'ID {id_article}.")


def afficher_alertes():
    """Affiche uniquement les articles nécessitant un réapprovisionnement."""
    alertes = [art for art in stock_articles if art['statut'] in ["Stock bas", "Rupture de stock"]]

    if not alertes:
        print("\n✅ Tout est sous contrôle ! Aucun article en alerte de stock.")
        return

    print("\n⚠️ ******************** ALERTE RÉAPPROVISIONNEMENT ******************** ⚠️")
    for art in alertes:
        print(f"• ID {art['id']} | {art['nom']} ({art['marque']}) - Reste: {art['quantite']} paires | Statut: {art['statut']}")
    print("**********************************\n")


def reinitialiser_stock():
    """Vide entièrement le stock actuel et réinitialise le fichier JSON."""
    global stock_articles
    print("\n⚠️ ATTENTION : Cette action supprimera TOUS les articles du stock.")
    confirmation = input("Êtes-vous sûr de vouloir continuer ? (oui/non) : ").strip().lower()
    
    if confirmation == "oui":
        stock_articles = []
        sauvegarder_stock()
        print("🗑️ Le stock a été entièrement réinitialisé !")
    else:
        print("❌ Réinitialisation annulée.")


# **** MENU INTERACTIF (CLI) ****   

def afficher_menu():
    print("\n******************************************************")
    print("        🛍️  GESTIONNAIRE LILI-SHOP  🛍️        ")
    print("******************************************************")
    print("1. Afficher tout le stock")
    print("2. Ajouter un nouvel article")
    print("3. Enregistrer une vente (Sortie de stock)")
    print("4. Réapprovisionner un article (Entrée de stock)")
    print("5. Voir les alertes de réapprovisionnement")
    print("6. 🗑️ Réinitialiser / Vider le stock")
    print("7. Quitter")
    print("******************************************************")


def lancer_application():
    charger_stock()

    while True:
        afficher_menu()
        choix = input("👉 Choisissez une option (1-7) : ").strip()

        if choix == "1":
            afficher_stock()

        elif choix == "2":
            print("\n***Ajout d'un nouvel article ***")
            print("💡 (Tapez '0' à tout moment pour annuler et revenir au menu principal)")
            
            sku = input("SKU (ex: LILI-BSK-N-42) : ").strip()
            if sku == "0":
                print("↩️ Opération annulée, retour au menu.")
                continue

            nom = input("Nom du modèle : ").strip()
            if nom == "0":
                print("↩️ Opération annulée, retour au menu.")
                continue

            marque = input("Marque : ").strip()
            if marque == "0":
                print("↩️ Opération annulée, retour au menu.")
                continue

            try:
                p_input = input("Pointure : ").strip()
                if p_input == "0":
                    print("↩️ Opération annulée, retour au menu.")
                    continue
                pointure = int(p_input)

                prix_input = input("Prix (FCFA) : ").strip()
                if prix_input == "0":
                    print("↩️ Opération annulée, retour au menu.")
                    continue
                prix = float(prix_input)

                qte_input = input("Quantité initiale : ").strip()
                if qte_input == "0":
                    print("↩️ Opération annulée, retour au menu.")
                    continue
                quantite = int(qte_input)

            except ValueError:
                print("❌ Erreur : Veuillez entrer un nombre valide pour la pointure, le prix et la quantité.")
                continue

            couleur = input("Couleur : ").strip()
            if couleur == "0":
                print("↩️ Opération annulée, retour au menu.")
                continue

            ajouter_article(sku, nom, marque, pointure, prix, quantite, couleur)

        elif choix == "3":
            afficher_stock()
            if not stock_articles:
                continue
            
            print("💡 (Tapez '0' pour annuler)")
            try:
                saisie_id = input("Entrez l'ID de l'article vendu : ").strip()
                if saisie_id == "0":
                    print("↩️ Opération annulée, retour au menu.")
                    continue
                id_art = int(saisie_id)

                saisie_qte = input("Nombre de paires vendues (ex: 1) : ").strip()
                if saisie_qte == "0":
                    print("↩️ Opération annulée, retour au menu.")
                    continue
                qte = int(saisie_qte)

                enregistrer_vente(id_art, qte)
            except ValueError:
                print("❌ Erreur : Veuillez entrer des identifiants et quantités valides.")

        elif choix == "4":
            afficher_stock()
            if not stock_articles:
                continue

            print("💡 (Tapez '0' pour annuler)")
            try:
                saisie_id = input("Entrez l'ID de l'article à réapprovisionner : ").strip()
                if saisie_id == "0":
                    print("↩️ Opération annulée, retour au menu.")
                    continue
                id_art = int(saisie_id)

                saisie_qte = input("Nombre de paires reçues du fournisseur : ").strip()
                if saisie_qte == "0":
                    print("↩️ Opération annulée, retour au menu.")
                    continue
                qte = int(saisie_qte)

                reapprovisionner_article(id_art, qte)
            except ValueError:
                print("❌ Erreur : Veuillez entrer des chiffres valides.")

        elif choix == "5":
            afficher_alertes()

        elif choix == "6":
            reinitialiser_stock()

        elif choix == "7":
            print("\n👋 Merci d'avoir utilisé le Gestionnaire LILI-SHOP ! À bientôt.")
            break

        else:
            print("❌ Option invalide. Veuillez taper un chiffre entre 1 et 7.")


if __name__ == "__main__":
    lancer_application()