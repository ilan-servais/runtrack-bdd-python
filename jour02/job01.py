import mysql.connector

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Remplacez par votre nom d'utilisateur
    password="Ilansl1234_",  # Remplacez par votre mot de passe
    database="LaPlateforme"
)

# Créer un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exécuter la requête SQL pour récupérer tous les étudiants
query = "SELECT * FROM etudiant"
cursor.execute(query)

# Récupérer les résultats de la requête
students = cursor.fetchall()

# Afficher les résultats en console
for student in students:
    print(student)

# Fermer le curseur et la connexion
cursor.close()
conn.close()
