USE assignment;

DELIMITER //
CREATE PROCEDURE insertUser(firstName VARCHAR(50), lastName VARCHAR(50), 
	dateOfBirth DATE, placeOfBirth VARCHAR(50), email VARCHAR(50), username VARCHAR(50), shortCV TEXT)
	MODIFIES SQL DATA
	BEGIN
		DECLARE usernameCount INT;
        SELECT count(id) FROM users WHERE users.username = username OR users.email = email INTO usernameCount;
        IF usernameCount < 1
			THEN
				INSERT INTO users (firstName, lastName, dateOfBirth, email, username, shortCV)
				VALUES (firstName, lastName, dateOfBirth, email, username, shortCV);
		END IF;
	END //
    DELIMITER ;

DELIMITER //
CREATE PROCEDURE initiateFriendship(user INT, friend INT)
MODIFIES SQL DATA
BEGIN
	DECLARE friendshipCount INT;
    SELECT count(idFriendship) FROM friendship WHERE 
    (friendship.idUser = user AND friendship.idFriend = friend) OR
    (friendship.idUser = friend AND friendship.idFriend = user)
    INTO friendshipCount;
    IF friendshipCount < 1
		THEN
			INSERT INTO friendship (idUser, idFriend, createdAt, updatedAt)
            VALUES (user, friend, current_timestamp, current_timestamp);
	END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE modifyUsersNames(usr VARCHAR(50), newFirstName VARCHAR(50), newLastName VARCHAR(50))
MODIFIES SQL DATA
BEGIN
	DECLARE usersCount, x INT;
    SELECT count(id) FROM users WHERE username = usr INTO usersCount;
    IF usersCount < 1
		THEN
			SELECT 'Username does not exists in the database' AS 'Error message';
		ELSE
			SELECT id FROM users WHERE username = usr INTO x;
			UPDATE users SET firstName = newFirstName, lastName = newLastName
				WHERE id = x;
	END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE modifyUsersEmail(usr VARCHAR(50), newEmail VARCHAR(50))
MODIFIES SQL DATA
BEGIN
	DECLARE usersCount, emailCount, x INT;
    SELECT count(id) FROM users WHERE username = usr INTO usersCount;
    IF usersCount < 1
		THEN
			SELECT 'Username does not exists in the database' AS 'Error message';
		ELSE
			SELECT count(id) FROM users WHERE email = newEmail INTO emailCount;
				IF emailCount < 1
					THEN
						SELECT id FROM users WHERE username = usr INTO x;
						UPDATE users SET email = newEmail WHERE id = x;
					ELSE
						SELECT 'Email address already assigned to another user' AS 'Error message';
				END IF;
	END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE modifyFriendship(user INT, friend INT, newStatus ENUM('waiting', 'accepted', 'rejected'))
MODIFIES SQL DATA
BEGIN
	UPDATE friendship SET status = newStatus, updatedAt = CURRENT_TIMESTAMP
		WHERE (friendship.idUser = user AND friendship.idFriend = friend)
        OR (friendship.idUser = friend AND friendship.idFriend = user);
END //
DELIMITER ;

DELIMITER $$
CREATE FUNCTION getFriends(usr VARCHAR(50)) RETURNS INT
    DETERMINISTIC
BEGIN
		DECLARE userCount, friendsCount, x INT;
        SELECT count(id) FROM users WHERE username = usr INTO userCount;
        IF userCount < 1
			THEN
                RETURN NULL;
			ELSE
				SELECT id FROM users WHERE username = usr INTO x;
				SELECT count(*) FROM friendship WHERE (idUser = x XOR idFriend = x) and status = 'accepted'
					INTO friendsCount;
				RETURN friendsCount;
		END IF;
	END$$
DELIMITER ;