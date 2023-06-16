USE books_schema;

INSERT INTO users
(name)
VALUES
("Dennis Prager"),
("Thomas Sowell"),
("Jim Dillingham"),
("Ben Shapiro"),
("Jordan Peterson"),
("Robert Kiyosaki"),
("Peter Schiff"),
("Milton Friedman");

INSERT INTO books
(name)
VALUES
("Still the Best Hope"),
("Race and Culture: A World View"),
("Pray in This Way"),
("Primetime Propoganda"),
("Twelve Rules for Life"),
("Rich Dad Poor Dad"),
("The Real Crash: America's Coming Bankruptcy"),
("Free to Choose");

-- UPDATE books
-- SET name = "Twelve More Rules for Life"
-- WHERE id = 5;

-- UPDATE users
-- SET first_name = "Ben (Bill)"
-- WHERE id = 4;

INSERT INTO orders
(user_id, book_id)
VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(2, 3),
(3, 1),
(3, 2),
(3, 3),
(3, 4),
( 4, 1),
( 4, 2),
( 4, 3),
( 4, 4),
( 4, 5),
( 4, 6),
( 4, 7),
( 4, 8);

-- SELECT * 
-- FROM 
-- users LEFT JOIN orders
-- ON users.id = orders.user_id
-- WHERE orders.book_id = 3;

-- SELECT * 
-- FROM 
-- users JOIN orders
-- ON users.id = orders.user_id
-- WHERE orders.book_id = 3;

-- DELETE FROM orders 
-- WHERE user_id = 2;
-- DELETE FROM users
-- WHERE id = 2;

INSERT INTO orders
(user_id, book_id)
VALUES
(5, 2);

-- SELECT books.name 
-- FROM 
-- books JOIN orders
-- ON books.id = orders.book_id
-- WHERE orders.user_id = 3;

-- SELECT users.first_name, users.last_name, books.name
-- FROM 
-- books JOIN orders
-- ON books.id = orders.book_id
-- JOIN users
-- ON users.id = orders.user_id
-- WHERE orders.book_id = 5;