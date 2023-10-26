CREATE TABLE
    `tabuleirodb`.`users_games` (
        `user_id` INT NOT NULL,
        `game_id` INT NOT NULL,
        `score` TINYINT NULL,
        `favorite_status` BOOLEAN NOT NULL DEFAULT FALSE,
        `owned_status` BOOLEAN NOT NULL DEFAULT FALSE,
        `played_status` BOOLEAN NOT NULL DEFAULT FALSE,
        `want_status` BOOLEAN NOT NULL DEFAULT FALSE,
        CONSTRAINT `users_games_game_id_fk`
        FOREIGN KEY (`game_id`) REFERENCES `games`(`game_id`)
    ) ENGINE = InnoDB;