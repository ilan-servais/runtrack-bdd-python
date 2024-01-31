-- Récupérer les élèves dont l'âge est compris entre 18 et 25 ans, triés par l'âge en ordre croissant
SELECT * FROM etudiant WHERE age BETWEEN 18 AND 25 ORDER BY age ASC;