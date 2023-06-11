INSERT INTO names.names 
(id, name, created_at, updated_at)
VALUES(1010, "Mark", NOW(), NOW());

INSERT INTO names.names 
(id, name, created_at, updated_at)
VALUES
(1000, "Nocturne", NOW(), NOW()),
(2000, "Master Yi", NOW(), NOW()),
(3000, "Teemo Dreemo", NOW(), NOW()),
(4000, "Morgana", NOW(), NOW());

UPDATE names.names
SET name = "Morgana Tawanna", updated_at = NOW()
WHERE id = 4000;

DELETE FROM names.names
WHERE id = 3000;

SELECT *
FROM names.names;

