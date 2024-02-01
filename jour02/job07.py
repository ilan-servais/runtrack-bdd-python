import mysql.connector
from getpass import getpass

class Employe:
    def __init__(self, user, password, database):
        self.conn = mysql.connector.connect(
            host="localhost",
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()

    def read_employes(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def update_employe(self, employe_id, new_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salaire, employe_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

# Exemple d'utilisation de la classe Employe
user_mysql = input("Nom d'utilisateur MySQL: ")
password_mysql = getpass("Mot de passe MySQL: ")
employe_db = Employe(user_mysql, password_mysql, "Entreprise")

# Exemples d'opérations CRUD
employe_db.create_employe("Dujardin", "Jean", 3800.00, 2)
print(employe_db.read_employes())

employe_db.update_employe(1, 4200.00)
print(employe_db.read_employes())

employe_db.delete_employe(2)
print(employe_db.read_employes())

# Fermeture de la connexion
employe_db.close_connection()
