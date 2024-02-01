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

# Requête SQL pour calculer la superficie totale des étages
query = "SELECT SUM(superficie) AS superficie_totale FROM etage"

# Exécution de la requête
cursor.execute(query)

# Récupération du résultat
result = cursor.fetchone()

# Affichage du résultat en console
superficie_totale = result[0]
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
