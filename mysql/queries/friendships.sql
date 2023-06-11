USE friendship_schema;

INSERT INTO users
VALUES
(1, "Frank", "Ribery", NOW(), NOW()),
(2, "Floyd", "Mayweather", NOW(), NOW()),
(3, "Arjen", "Robben", NOW(), NOW()),
(4, "Robert", "Lewandowski", NOW(), NOW()),
(5, "Jerome", "Boateng", NOW(), NOW()),
(6, "Thomas", "Mueller", NOW(), NOW());

INSERT INTO friendships
VALUES
(1, 1, 2, NOW(), NOW()),
(2, 1, 4, NOW(), NOW()),
(3, 1, 6, NOW(), NOW()),
(4, 2, 1, NOW(), NOW()),
(5, 2, 3, NOW(), NOW()),
(6, 2, 5, NOW(), NOW()),
(7, 4, 3, NOW(), NOW()),
(8, 5, 1, NOW(), NOW()),
(9, 5, 6, NOW(), NOW()),
(10, 6, 2, NOW(), NOW()),
(11, 6, 3, NOW(), NOW());

SELECT users.first_name,
	   users.last_name,
	   users2.first_name AS friend_first_name,
       users2.last_name AS friend_last_name
FROM
users JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users AS users2
ON friendships.friend_id = users2.id;	

SELECT users.first_name,
       users.last_name
FROM
users JOIN friendships
ON users.id = friendships.user_id
WHERE friendships.friend_id = 1;       

SELECT COUNT(id)
FROM friendships;

SELECT users.first_name,
       users.last_name,
       COUNT(friendships.user_id) AS num_friends
FROM
users JOIN friendships
ON users.id = friendships.user_id
GROUP BY user_id       
ORDER BY num_friends DESC
LIMIT 2;

-- I forgot to assign friends to user 3 in the beginning 
INSERT INTO friendships
VALUES
(12, 3, 2, NOW(), NOW()),
(13, 3, 5, NOW(), NOW());

SELECT users2.first_name,
       users2.last_name
FROM 
users JOIN friendships
ON users.id = friendships.user_id
JOIN users AS users2
ON users2.id = friendships.friend_id
WHERE friendships.user_id = 3;