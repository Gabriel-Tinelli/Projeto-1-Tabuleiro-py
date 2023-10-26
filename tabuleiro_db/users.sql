CREATE TABLE
    `tabuleirodb`.`users` (
        `user_id` INT NOT NULL AUTO_INCREMENT,
        `username` VARCHAR(30) NOT NULL,
        `password_hash` VARBINARY(64) NOT NULL,
        `password_salt` VARBINARY(64) NOT NULL,
        `person_name` VARCHAR(100) NOT NULL,
        `email` VARCHAR(320) NOT NULL,
        `blocked` BOOLEAN NOT NULL DEFAULT FALSE,
        `deleted` BOOLEAN NOT NULL DEFAULT FALSE,
        PRIMARY KEY (`user_id`)
    ) ENGINE = InnoDB;