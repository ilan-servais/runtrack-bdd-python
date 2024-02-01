try:
    import mysql.connector
    from getpass import getpass

    class Zoo:
        def __init__(self, user, password, database):
            self.connection = mysql.connector.connect(
                host="localhost",
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()

        def create_animal(self, nom, race, id_cage, date_naissance, pays_origine):
            query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
            values = (nom, race, id_cage, date_naissance, pays_origine)
            self.execute_query(query, values)

        def create_cage(self, superficie, capacite_max):
            query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
            values = (superficie, capacite_max)
            self.execute_query(query, values)

        def add_animal(self):
            nom = input("Nom de l'animal: ")
            race = input("Race de l'animal: ")
            id_cage = int(input("ID de la cage: "))
            date_naissance = input("Date de naissance de l'animal (format YYYY-MM-DD): ")
            pays_origine = input("Pays d'origine de l'animal: ")
            self.create_animal(nom, race, id_cage, date_naissance, pays_origine)

        def add_cage(self):
            superficie = int(input("Superficie de la cage: "))
            capacite_max = int(input("Capacité maximale de la cage: "))
            self.create_cage(superficie, capacite_max)

        def remove_animal(self):
            animal_id = int(input("ID de l'animal à supprimer: "))
            query = "DELETE FROM animal WHERE id = %s"
            values = (animal_id,)
            self.execute_query(query, values)

        def remove_cage(self):
            cage_id = int(input("ID de la cage à supprimer: "))
            query = "DELETE FROM cage WHERE id = %s"
            values = (cage_id,)
            self.execute_query(query, values)

        def modify_animal(self):
            animal_id = int(input("ID de l'animal à modifier: "))
            nom = input("Nouveau nom de l'animal: ")
            race = input("Nouvelle race de l'animal: ")
            id_cage = int(input("Nouvel ID de la cage: "))
            date_naissance = input("Nouvelle date de naissance de l'animal (format YYYY-MM-DD): ")
            pays_origine = input("Nouveau pays d'origine de l'animal: ")
            query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
            values = (nom, race, id_cage, date_naissance, pays_origine, animal_id)
            self.execute_query(query, values)

        def modify_cage(self):
            cage_id = int(input("ID de la cage à modifier: "))
            superficie = int(input("Nouvelle superficie de la cage: "))
            capacite_max = int(input("Nouvelle capacité maximale de la cage: "))
            query = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id = %s"
            values = (superficie, capacite_max, cage_id)
            self.execute_query(query, values)

        def get_animals(self):
            query = "SELECT * FROM animal"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)

        def get_cages(self):
            query = "SELECT * FROM cage"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)

        def display_animals_and_cages(self):
            print("Animaux dans le zoo:")
            self.get_animals()
            print("\nCages dans le zoo:")
            self.get_cages()

        def calculate_total_cage_area(self):
            query = "SELECT SUM(superficie) FROM cage"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            total_area = result[0] if result[0] is not None else 0
            print(f"La superficie totale de toutes les cages est de {total_area} m2.")

        def execute_query(self, query, values=None):
            self.cursor.execute(query, values)
            self.connection.commit()

        def close_connection(self):
            self.cursor.close()
            self.connection.close()

    # Exemple d'utilisation
    user_mysql = input("Nom d'utilisateur MySQL: ")
    password_mysql = getpass("Mot de passe MySQL: ")
    zoo_db = Zoo(user_mysql, password_mysql, "zoo")

    while True:
        print("\nOptions:")
        print("1. Ajouter un animal")
        print("2. Ajouter une cage")
        print("3. Supprimer un animal")
        print("4. Supprimer une cage")
        print("5. Modifier un animal")
        print("6. Modifier une cage")
        print("7. Afficher tous les animaux et cages")
        print("8. Calculer la superficie totale des cages")
        print("9. Quitter")

        choice = input("Choisissez une option (1-9): ")

        if choice == "1":
            zoo_db.add_animal()
        elif choice == "2":
            zoo_db.add_cage()
        elif choice == "3":
            zoo_db.remove_animal()
        elif choice == "4":
            zoo_db.remove_cage()
        elif choice == "5":
            zoo_db.modify_animal()
        elif choice == "6":
            zoo_db.modify_cage()
        elif choice == "7":
            zoo_db.display_animals_and_cages()
        elif choice == "8":
            zoo_db.calculate_total_cage_area()
        elif choice == "9":
            zoo_db.close_connection()
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")
except mysql.connector.Error as err:
    print(f"Erreur MySQL: {err}")
