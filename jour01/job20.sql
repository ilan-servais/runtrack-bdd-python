-- Compter le nombre d'étudiants mineurs en base de données (âge < 18)
SELECT COUNT(*) AS nombre_etudiants_mineurs FROM etudiant WHERE age < 18;