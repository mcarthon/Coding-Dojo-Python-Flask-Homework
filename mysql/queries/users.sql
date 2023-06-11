INSERT INTO users_schema.users
VALUES
(1, "Fizz", "Shark", "fizz@shark.edu", NOW(), NOW()),
(2, "Gragas", "Beer", "gragas@beer.woobon", NOW(), NOW()),
(3, "Fiora", "Frenchy", "fiora@frenchy.com", NOW(), NOW());

SELECT *
FROM users_schema.users;

SELECT *
FROM users_schema.users
WHERE email = 'fizz@shark.edu';

SELECT *
FROM users_schema.users
WHERE id = 3;

UPDATE users_schema.users 
SET last_name = "Pancakes"
WHERE id = 3;

DELETE FROM
users_schema.users
WHERE id = 2;

SELECT *
FROM users_schema.users
ORDER BY first_name ;

SELECT *
FROM users_schema.users
ORDER BY first_name DESC;