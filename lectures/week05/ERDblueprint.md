Monster Trucks VS Bumper Cars

User Class
- id
- firstName
- lastName
- createdAt
- updatedAt

Event Class
- id
- eventName
- location
- eventDate
- eventTime
- createdAt
- updatedAt

Truck Class
- id
- name
- color
- wheelSize
- fuelLevel
- createdAt
- updatedAt

Car Class
- id
- name
- color
- seatCount
- batteryCharge
- createdAt
- updatedAt

User table is always the one side
1:M = User creates Truck and Car and Event
M:M = Event has Trucks and Cars


# Insert = C
- add one = INSERT INTO <TableName> (<column01>, <column02>) VALUES (<column01Value>, <column02Value>);
- add multiple = INSERT INTO <TableName> (<column01>, <column02>) VALUES (<column01Value>, <column02Value>), (<column01Value>, <column02Value>);

# Select = R
- Get everything/all = SELECT * FROM <TableName>;
- Get one = SELECT * FROM <TableName> WHERE <XYX> = <xyz;>;

# Update = U
UPDATE <tableName> SET <columnName>=<newValue> WHERE <XYZ>=<xyz>;

# Delete = D
DELETE FROM <TableName> WHERE <XYZ>=<xyz>


# In flask
SELECT * FROM user WHERE id=%(id)s;

