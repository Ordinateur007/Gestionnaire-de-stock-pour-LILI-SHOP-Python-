_compteur_article_id = 0
_compteur_commande_id = 0
_compteur_client_id = 0

def  generer_id_article_id ():
    
    global _compteur_article_id
    _compteur_article_id+= 1
    return _compteur_article_id

def generer_id_commande ():
    
        global _compteur_commande_id
        _compteur_commande_id+= 1
        return _compteur_commande_id
def generer_id_client():

    global _compteur_client_id
    _compteur_client_id+= 1
    return _compteur_client_id

        
def creer_article(sku,nom,marque,pointure,prix,quantite,couleur,seuil_alerte,statut):
    """
    Crée et retourne un dictionnaire représentant un article.
    Note : L'ID article est indépendant.
    """
   
    return{ 
           "id": generer_id_article_id(),
           "sku":sku,
           "nom":nom,
           "marque":marque,
           "pointure":pointure,
           "prix":prix,
           "quantite":quantite,
           "couleur":couleur,
           "seuil_alerte":seuil_alerte,
           "statut":statut
           
           }  
def creer_commande(id_article,id_client,date_commande, articles_commandes,total,statut,adresse_livraison,moyen_paiement,numero_suivi):
     """
    Crée et retourne un dictionnaire représentant une commande
    Note : L'ID commande est indépendant.
    """
     return{
         "id_commande":generer_id_commande(),
         "id_article":id_article,
         "id_client":id_client,
         "date_commande":date_commande,
         "articles_commandes":articles_commandes,
         "total":total,
         "statut":statut,
         "adresse_livraison":adresse_livraison,
         "moyen_paiement":moyen_paiement,
         "numero_suivi":numero_suivi
         
         
     }
def creer_client(nom,prenom,email,telephone,adresse_defaut):
                                     
   """
    Crée et retourne un dictionnaire représentant un client
    Note : L'ID client est indépendant.
    """
   return{
         "id_client":generer_id_client(),
         "nom":nom,
         "prenom":prenom,
         "email":email,
         "telephone":telephone,
         "adresse_defaut":adresse_defaut
    }
 
        