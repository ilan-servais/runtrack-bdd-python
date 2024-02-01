import mysql.connector
from getpass import getpass

# Demander le nom d'utilisateur
user = input("Nom d'utilisateur MySQL: ")

# Demander le mot de passe de manière sécurisée
password = getpass("Mot de passe MySQL: ")

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="LaPlateforme"
)

# Création d'un curseur
cursor = conn.cursor()

# Requête SQL pour calculer la capacité totale des salles
query = "SELECT SUM(capacite) AS capacite_totale FROM salle"

# Exécution de la requête
cursor.execute(query)

# Récupération du résultat
result = cursor.fetchone()

# Affichage du résultat en console
capacite_totale = result[0]
print(f"La capacité totale des salles est de {capacite_totale} places")

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
