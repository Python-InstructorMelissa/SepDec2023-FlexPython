-- Insert a User into the db
INSERT INTO user (firstName, lastName) VALUES ("Betty", "Wilson");
-- Insert an event into the db
INSERT INTO event (eventName, location, eventDate, eventTime, user_id) VALUES ("Rocking and Smashing", "Zoom, Online", "2023-09-28", "20:00:00", 2);
-- Update a event
UPDATE event SET eventName="Rough Ride" WHERE id=2;
-- Remove a truck
INSERT INTO truck (name, wheelSize, color, fuelLevel, user_id) VALUES ("Nobody", 3, "Rainbow", 20, 14);
DELETE FROM truck WHERE id =6;
-- view a users EVENTS
SELECT * FROM user LEFT JOIN event on user.id = event.user_id WHERE user.id = 4;
-- view the events trucks and cars
SELECT * FROM user
LEFT JOIN event on user.id = event.user_id
LEFT JOIN eventLineup on event.id = eventLineup.event_id
LEFT JOIN truck on eventLineup.truck_id = truck.id
WHERE user.id = 1;
-- view 1 user
SELECT * FROM user WHERE id = 14;
-- view 1 car
SELECT * FROM car WHERE id = 2;