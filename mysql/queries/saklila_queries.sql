USE sakila;

SELECT customer.first_name,
	   customer.last_name,
       customer.email,
       address.address
FROM 
address JOIN customer
ON address.address_id = customer.address_id
WHERE address.city_id = 312;

SELECT film.title,
	   film.description,
       film.release_year,
       film.rating,
       film.special_features,
       category.name
FROM
film JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON category.category_id = film_category.category_id;

SELECT actor.actor_id,
       actor.first_name,
       actor.last_name,
       film.title,
       film.description,
       film.release_year
FROM
actor JOIN film_actor
ON actor.actor_id = film_actor.actor_id
JOIN film
ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

SELECT customer.first_name,
       customer.last_name,
       customer.email,
       address.address
FROM
customer JOIN address
ON customer.address_id = address.address_id
JOIN city
ON city.city_id = address.city_id
WHERE city.city_id in (1, 42, 312, 459);

SELECT film.title,
       film.description,
       film.release_year,
       film.rating,
       film.special_features
FROM 
film JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 15
AND film.special_features LIKE "%behind%"
AND film.rating = "G";

SELECT film.film_id,
	   film.title,
       film_actor.actor_id,
       actor.first_name,
       actor.last_name
FROM 
film JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

SELECT film.title,
	   film.description,
       film.release_year,
       film.rating,
       film.special_features,
       category.name AS genre
FROM
film JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON category.category_id = film_category.category_id
WHERE category.name LIKE "%drama%"
AND film.rental_rate = 2.99;

SELECT film.title,
	   film.description,
       film.release_year,
       film.rating,
       film.special_features,
       category.name AS genre,
       actor.first_name,
       actor.last_name
FROM
film JOIN film_category
ON film.film_id = film_category.film_id
JOIN film_actor 
ON film_actor.film_id = film.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
JOIN category
ON film_category.category_id = category.category_id
WHERE actor.first_name LIKE "%sandra%"
AND actor.last_name LIKE "kilmer"
AND category.name LIKE "action";