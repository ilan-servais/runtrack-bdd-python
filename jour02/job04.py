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

# Requête SQL pour récupérer les noms et capacités de la table "salle"
query = "SELECT nom, capacite FROM salle"

# Exécution de la requête
cursor.execute(query)

# Récupération des résultats
result = cursor.fetchall()

# Affichage des résultats en console
for row in result:
    print(f"Nom: {row[0]}, Capacité: {row[1]}")

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
