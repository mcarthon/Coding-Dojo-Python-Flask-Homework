USE dojos_and_ninjas_schema;

INSERT INTO dojos
VALUES
(1, "Isaiah Smith", NOW(), NOW()),
(2, "Aaron Hsu", NOW(), NOW()),
(3, "Shakira Java", NOW(), NOW());

DELETE FROM dojos
WHERE id IN (1,2,3);

INSERT INTO dojos
VALUES
(1, "Isaiah Smith", NOW(), NOW()),
(2, "Aaron Hsu", NOW(), NOW()),
(3, "Shakira Java", NOW(), NOW());

INSERT INTO ninjas
VALUES
(1, "Teemo", "Dreemo", 30, NOW(), NOW(), 1),
(2, "Veigar", "Master of Evil", 50, NOW(), NOW(), 1),
(3, "Garen", "Demacia", 25, NOW(), NOW(), 1),
(4, "Draven", "Executioner", 23, NOW(), NOW(), 2),
(5, "Miss", "Fortune", 33, NOW(), NOW(), 2),
(6, "Brand", "Burning Vengeance", 40, NOW(), NOW(), 2),
(7, "Java", "Fun", 100, NOW(), NOW(), 3),
(8, "C-Sharp", "Bad", 500, NOW(), NOW(), 3),
(9, "Apple", "Dev", 10, NOW(), NOW(), 3);

SELECT *
FROM ninjas
WHERE dojo_id = 1;

SELECT *
FROM ninjas
WHERE dojo_id = 3;

SELECT * 
FROM 
dojos JOIN ninjas
ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 6;

SELECT *
FROM dojos JOIN ninjas
ON dojos.id = ninjas.dojo_id;