USE books_schema;

INSERT INTO users
VALUES
(1, "Dennis", "Prager", NOW(), NOW()),
(2, "Thomas", "Sowell", NOW(), NOW()),
(3, "Jim", "Dillingham", NOW(), NOW()),
(4, "Ben", "Shapiro", NOW(), NOW()),
(5, "Jordan", "Peterson", NOW(), NOW()),
(6, "Robert", "Kiyosaki", NOW(), NOW()),
(7, "Peter", "Schiff", NOW(), NOW()),
(8, "Milton", "Friedman", NOW(), NOW());

INSERT INTO books
VALUES
(1, "Still the Best Hope", NOW(), NOW()),
(2, "Race and Culture: A World View", NOW(), NOW()),
(3, "Pray in This Way", NOW(), NOW()),
(4, "Primetime Propoganda", NOW(), NOW()),
(5, "Twelve Rules for Life", NOW(), NOW()),
(6, "Rich Dad Poor Dad", NOW(), NOW()),
(7, "The Real Crash: America's Coming Bankruptcy", NOW(), NOW()),
(8, "Free to Choose", NOW(), NOW());

UPDATE books
SET name = "Twelve More Rules for Life"
WHERE id = 5;

UPDATE users
SET first_name = "Ben (Bill)"
WHERE id = 4;

INSERT INTO orders
VALUES
(1, 1, 1, NOW(), NOW()),
(2, 1, 2, NOW(), NOW()),
(3, 2, 1, NOW(), NOW()),
(4, 2, 2, NOW(), NOW()),
(5, 2, 3, NOW(), NOW()),
(6, 3, 1, NOW(), NOW()),
(7, 3, 2, NOW(), NOW()),
(8, 3, 3, NOW(), NOW()),
(9, 3, 4, NOW(), NOW()),
(10, 4, 1, NOW(), NOW()),
(11, 4, 2, NOW(), NOW()),
(12, 4, 3, NOW(), NOW()),
(13, 4, 4, NOW(), NOW()),
(14, 4, 5, NOW(), NOW()),
(15, 4, 6, NOW(), NOW()),
(16, 4, 7, NOW(), NOW()),
(17, 4, 8, NOW(), NOW());

SELECT * 
FROM 
users LEFT JOIN orders
ON users.id = orders.user_id
WHERE orders.book_id = 3;

SELECT * 
FROM 
users JOIN orders
ON users.id = orders.user_id
WHERE orders.book_id = 3;

DELETE FROM orders 
WHERE user_id = 2;
DELETE FROM users
WHERE id = 2;

INSERT INTO orders
VALUES
(18, 5, 2, NOW(), NOW());

SELECT books.name 
FROM 
books JOIN orders
ON books.id = orders.book_id
WHERE orders.user_id = 3;

SELECT users.first_name, users.last_name, books.name
FROM 
books JOIN orders
ON books.id = orders.book_id
JOIN users
ON users.id = orders.user_id
WHERE orders.book_id = 5;