CREATE TABLE
    `tabuleirodb`.`games_pictures` (
        `picture_id` INT NOT NULL AUTO_INCREMENT,
        `game_id` INT NOT NULL,
        `url` VARCHAR(400) NOT NULL,
        `type` ENUM ('Main', 'Box', 'Background', 'Gallery', 'Other') NOT NULL DEFAULT 'Gallery',
        PRIMARY KEY (`picture_id`),
        CONSTRAINT `games_pictures_game_id_fk`
        FOREIGN KEY (`game_id`) REFERENCES `games`(`game_id`)
    ) ENGINE = InnoDB;