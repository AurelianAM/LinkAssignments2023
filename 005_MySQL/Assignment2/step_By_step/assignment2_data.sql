USE assignment;

CALL insertUser('John', 'Johanson', '2000-01-01', 'Chicago', 'john.johanson@email.com', 'jjohn', 'Something to remember');
CALL insertUser('Arthur', 'Ariston', '2002-02-02', 'Detroit', 'arthur.ariston@email.com', 'aarthur', 'Memories to remember');
CALL insertUser('Bob', 'Dilan', '2003-03-03', 'New York', 'bob.dilan@email.com', 'dbob', 'I am a singer');
CALL insertUser('Dan', 'Dumitru', '2005-03-14', 'Bucuresti', 'dan.dumitru@email.com', 'ddan', 'I am a writter');

CALL insertUser('Erwan', 'Ewing', NULL, NULL, 'erwan.ewing@email.com', 'eerwan', 'I am a programmer in Python');
CALL insertUser('Bob', 'Bing', NULL, NULL, 'bob.bing@email.com', 'bbob', 'I am a programmer in Python');
CALL insertUser('Boby', 'Billybob', NULL, NULL, 'boby.billybob@email.com', 'bboby', 'I am a freelancer');

CALL initiateFriendship(1, 2);
CALL initiateFriendship(2, 3);
CALL initiateFriendship(3, 4);
CALL initiateFriendship(4, 5);
CALL initiateFriendship(5, 1);
CALL initiateFriendship(5, 2);
CALL initiateFriendship(5, 3);
CALL initiateFriendship(5, 4);

CALL modifyFriendship(1, 2, 'accepted');
CALL modifyFriendship(2, 3, 'accepted');
CALL modifyFriendship(4, 3, 'rejected');
CALL modifyFriendship(4, 5, 'accepted');

CALL modifyFriendship(1, 2, 'accepted');
CALL modifyFriendship(2, 3, 'accepted');
CALL modifyFriendship(4, 3, 'rejected');
CALL modifyFriendship(4, 5, 'accepted');

CALL modifyFriendship(1, 5, 'accepted');
CALL modifyFriendship(5, 2, 'rejected');

CALL modifyUsersNames('ddan', 'Danut', 'Dumitrache');
CALL modifyUsersEmail('ddan', 'ddumitrache@email.com');
CALL modifyUsersEmail('ddan', 'john.johanson@email.com');
CALL modifyUsersEmail('ddan', 'danut.dumitrache@email.com');


SELECT * FROM users;
SELECT * FROM friendship;
SELECT getFriends('eerwan');

SELECT * FROM assignment.userview;