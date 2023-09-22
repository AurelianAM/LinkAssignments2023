USE `assignment`;
INSERT INTO user (firstName, lastName, email, username)
	VALUES ('John', 'Johnson', 'john.johnson@email.com', 'jhnj');
INSERT INTO user (firstName, lastName, email, username)
	VALUES ('Rohn', 'Rohnson', 'rohn.rohnson@email.com', 'rhnr');
INSERT INTO user (firstName, lastName, email, username)
	VALUES ('Don', 'Dohnson', 'don.dohnson@email.com', 'dhnd');

INSERT INTO status (userId, title)
	VALUES (1, 'online');
INSERT INTO status (userId, title)
	VALUES (2, 'traveling');
INSERT INTO status (userId, title)
	VALUES (3, 'working');

INSERT INTO friends (userId, friendId)
	VALUES (1, 2);
INSERT INTO friends (userId, friendId)
	VALUES (1, 3);
INSERT INTO friends (userId, friendId)
	VALUES (2, 3);

UPDATE friends
	SET status = 'accepted'
	WHERE userId = 1 AND friendId = 2;

-- SELECT * FROM user;
-- SELECT * FROM friends;
-- SELECT * FROM status;