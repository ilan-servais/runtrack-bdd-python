-- Création de la base de données
CREATE DATABASE IF NOT EXISTS zoo;
USE zoo;

-- Création de la table "animal"
CREATE TABLE IF NOT EXISTS animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    race VARCHAR(255),
    id_cage INT,
    date_naissance DATE,
    pays_origine VARCHAR(255)
);

-- Création de la table "cage"
CREATE TABLE IF NOT EXISTS cage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    superficie INT,
    capacite_max INT
);
