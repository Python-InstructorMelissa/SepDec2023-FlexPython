SELECT * FROM user;
INSERT INTO user (firstName, lastName) VALUES ("Melissa", "Longenberger"), ("Eric","Perrigo"), ("George","Feeny"), ("Bob","Ross");
INSERT INTO user (firstName, lastName) VALUES ("Kevin", "Gayyyyyda");
UPDATE user SET	lastName="Gayda" WHERE id=5;
DELETE FROM user WHERE id=6;
INSERT INTO user (firstName, lastName) VALUES ("Jane", "Doe");

SELECT * FROM truck;
INSERT INTO truck (name, wheelSize, color, fuelLevel, user_id) VALUES ("Fred",10, "Red", 100,1), ("Mentor",10,"Green",100,2), ("CardboardBox",0,"Brown",100,3), ("Black Peral",2 ,"Black", 30,1);

SELECT * FROM mayhamEvents.car;
INSERT INTO car (name, color, seatCount, batteryCharge, user_id) VALUES ("Sweet Tooth", "Pink",2,100,7), ("IceCream Van", "Rainbow", 1, 80,5), ("Captain Jack Sparrow", "Black with Scull and bones",8, 30, 3), ("Lightening McQueen", "Red", 0, 100, 2);

SELECT * FROM mayhamEvents.car;
INSERT INTO car (name, color, seatCount, batteryCharge, user_id) VALUES ("Sweet Tooth", "Pink",2,100,7), ("IceCream Van", "Rainbow", 1, 80,5), ("Captain Jack Sparrow", "Black with Scull and bones",8, 30, 3), ("Lightening McQueen", "Red", 0, 100, 2);

SELECT * FROM mayhamEvents.eventLineup;
INSERT INTO eventLineup (truck_id, car_id, event_id) VALUES (1,2,1), (1,3,2), (2,4,3), (4,4,4),(2,2,1), (4,3,2), (3,1,3), (4,1,4);

SELECT * FROM user LEFT JOIN truck on user.id = truck.user_id WHERE user.id = 1;
-- get all from one table join in the many on the one table id = many tables's forgein key id where one table id = xyz 
SELECT * FROM user LEFT JOIN truck on user.id = truck.user_id;
SELECT * FROM user LEFT JOIN car on user.id = car.user_id;
select * from user left join event on user.id = event.user_id 
left join eventLineup on event.id = eventLineup.event_id 
left join truck on eventLineup.truck_id = truck.id 
left join car on eventLineup.car_id = car.id where user.id = 2;
-- get all  from user where event = user.id= event_userid bring in the line up match evnet to lineup then truck to lineup and car to lineup