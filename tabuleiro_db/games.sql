CREATE TABLE
    `tabuleirodb`.`games` (
        `game_id` INT NOT NULL AUTO_INCREMENT,
        `category_id` INT NOT NULL,
        `name` VARCHAR(200) NOT NULL,
        `description` TEXT NULL,
        `release_year` TINYINT NULL,
        `difficulty` TINYINT NULL,
        `lenght` TINYINT NULL,
        `required_players` VARCHAR(10) NULL,
        `thumbnail_url` VARCHAR(400) NULL,
        `designer` VARCHAR(100) NULL,
        `deleted` BOOLEAN NOT NULL DEFAULT FALSE,
        PRIMARY KEY (`game_id`),
        CONSTRAINT `games_category_id_fk`
        FOREIGN KEY (`category_id`) REFERENCES categories(`category_id`)
    ) ENGINE = InnoDB;