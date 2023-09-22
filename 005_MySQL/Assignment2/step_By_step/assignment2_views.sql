USE assignment;

CREATE VIEW userView AS
	SELECT users.lastName, users.firstName, users.dateOfBirth, users.placeOfBirth
    FROM users;