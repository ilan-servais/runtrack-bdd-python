-- Ajouter Martin Dupuis à la table "etudiant"
INSERT INTO etudiant (nom, prenom, age, email) VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');

-- Récupérer les membres d'une même famille (Dupuis)
SELECT * FROM etudiant WHERE nom = 'Dupuis';