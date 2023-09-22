CREATE SCHEMA `assignment`
	DEFAULT CHARACTER SET utf8 
    COLLATE utf8_unicode_ci;

CREATE TABLE `assignment`.`user` (
`id` INT NOT NULL AUTO_INCREMENT,
`firstName` VARCHAR(50) NULL DEFAULT NULL,
`lastName` VARCHAR(50) NULL DEFAULT NULL,
`dateOfBirth` DATE NULL DEFAULT NULL,
`placeOfBirth` VARCHAR(50) NULL DEFAULT NULL,
`email` VARCHAR(50) NULL,
`username` VARCHAR(50) NOT NULL,
`shortCV` TEXT NULL DEFAULT NULL,
`picture` BLOB NULL DEFAULT NULL,
PRIMARY KEY (`id`),
-- define username and email and index in ascending order
UNIQUE INDEX `uq_username` (`username` ASC),
UNIQUE INDEX `uq_email` (`email` ASC));

CREATE TABLE `assignment`.`friends` (
`id` INT NOT NULL AUTO_INCREMENT,
`userId` INT NOT NULL,
`friendId` INT NOT NULL,
`createdAt` DATETIME NOT NULL DEFAULT NOW(),
`updatedAt` DATETIME NULL DEFAULT NULL,
`status` ENUM('waiting', 'accepted', 'rejected') NOT NULL DEFAULT 'waiting',
PRIMARY KEY (`id`),
-- define as unique userId and friendId
UNIQUE `uq_friend` (`userId`, `friendId`),
-- define two indxes and sort in ascenting order
INDEX `idx_friend_userId` (`userId` ASC),
INDEX `idx_friendId` (`friendId` ASC),
-- define first foreign key
CONSTRAINT `fk_friend_userId`
	FOREIGN KEY (`userId`)
    REFERENCES `assignment`.`user`(`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
-- define second foreign key
CONSTRAINT `fk_friend_friendId`
	FOREIGN KEY (`friendId`)
    REFERENCES `assignment`.`user`(`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


CREATE TABLE `assignment`.`status` (
`id` INT NOT NULL AUTO_INCREMENT,
`userId` INT NOT NULL,
`title` VARCHAR(20) NOT NULL,
`description` VARCHAR(50) NULL DEFAULT NULL,
`changedAt` DATETIME NOT NULL DEFAULT NOW(),
PRIMARY KEY (`id`),
-- define index and set for ascending order
INDEX `idx_status_userId` (`userId` ASC),
-- define foreign key
CONSTRAINT `fk_status_userId`
	FOREIGN KEY (`userId`)
    REFERENCES `assignment`.`user`(`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
