-- Création de la base de données
CREATE DATABASE IF NOT EXISTS Entreprise;
USE Entreprise;

-- Création de la table "employe"
CREATE TABLE employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10, 2),
    id_service INT
);

-- Insertion de quelques employés
INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
    ('Doe', 'John', 3500.00, 1),
    ('Smith', 'Alice', 4000.00, 2),
    ('Jones', 'Bob', 2800.00, 1);

-- Requête pour récupérer les employés dont le salaire est supérieur à 3 000 €
SELECT * FROM employe WHERE salaire > 3000;

-- Création de la table "service"
CREATE TABLE service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255)
);

-- Insertion de quelques services
INSERT INTO service (nom) VALUES
    ('Ressources Humaines'),
    ('Développement'),
    ('Comptabilité');

-- Requête pour récupérer tous les employés avec leur service respectif
SELECT employe.*, service.nom AS service_nom
FROM employe
JOIN service ON employe.id_service = service.id;
