INSERT INTO owner (firstName, lastName) VALUES ("Melissa", "Longenberger"), ("Corey", "W"), ("Geoffrey", "Zeylar"), ("Kevin", "Gayda"), ("Lydia", ""), ("Delvon", "Johnson"), ("Eric", "Perrigo"), ("Keith", ""), ("Lawrence", "Curry"), ("Wynter", "Greene"), ("Stephanie", "M");
SELECT * FROM owner LIMIT 100;
INSERT INTO pet (name, age, owner_id) VALUES ("Pebbles", 11, 7), ("Matt", 2, 5), ("Cumberdale", 7, 10), ("Max",1 ,9), ("Corky", 15, 8), ("Cheese", 1,2 ), ("Nacho",4,2), ("Rocky", 9, 6), ("Bobby", 4, 3), ("Lucy", 7, 11), ("Abby", 7, 1);
SELECT * FROM pet LIMIT 100

INSERT INTO friends (name, age, owner_id) VALUES ("Frog",11 , 10), ("Lucy", 3, 7), ("Mr Tucker", 1, 1), ("Copper Tone", 2, 11), ("Speedy", 55, 7), ("Octavie", 26, 8);
SELECT * FROM friends LIMIT 100

INSERT INTO pet_has_friends (pet_id, friends_id) VALUES (1,1), (2,2), (11,6), (3,5), (7,2), (10, 3), (4,6), (5,1),(6,6), (8, 3), (10, 2), (9,6), (11, 4), (2, 4);
SELECT * FROM pet_has_friends LIMIT 100

SELECT * FROM pet LEFT JOIN pet_has_friends on pet.id = pet_has_friends.pet_id LEFT JOIN friends on pet_has_friends.friends_id = friends.id;
SELECT * FROM friends LEFT JOIN pet_has_friends on friends.id = pet_has_friends.friends_id LEFT JOIN pet on pet_has_friends.pet_id = pet.id