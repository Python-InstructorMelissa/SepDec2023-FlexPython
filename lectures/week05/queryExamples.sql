INSERT INTO tableName (columnName, columnName, columnName) 
VALUES (%(columnNameValue)s, %(columnNameValue)s, %(columnNameValue)s);

SELECT * 
FROM tableName;

SELECT * 
FROM tableName 
WHERE id = %(id)s;

SELECT * 
FROM tableName 
WHERE email = %(email)s;

UPDATE tableName 
SET columnName="%(columnNameValue)s" 
WHERE id=%(id)s;

DELETE FROM tableName 
WHERE id = %(id)s;


SELECT * FROM tableOne    -- Select * from user
LEFT JOIN tableTwo on tableOne.id = tableTwo.tableOne_id  -- left join movie on user.id = movie.user_id
WHERE tableOne.id = %(id)s; -- where user.id = ?

SELECT * FROM tableOne 
LEFT JOIN tableTwo on tableOne.id = tableTwo.tableOne_id 
LEFT JOIN tableThree on tableTwo.id = tableThree.tableTwo_id 
LEFT JOIN tableFour on tableThree.tableFour_id = tableFour.id 
WHERE tableOne.id = %(id)s;

-- view the users events and the participating trucks
SELECT * FROM user
LEFT JOIN event on user.id = event.user_id
LEFT JOIN eventLineup on event.id = eventLineup.event_id
LEFT JOIN truck on eventLineup.truck_id = truck.id
WHERE user.id = 1;

SELECT * FROM actor
LEFT JOIN movie_has_actor ON actor.id = movie_has_actor.actor_id
LEFT JOIN movie ON movie_has_actor.movie_id = movie.id
WHERE actor.id = %(id)s;