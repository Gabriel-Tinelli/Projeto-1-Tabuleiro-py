CREATE TABLE
    `tabuleirodb`.`games_tags` (
        `game_id` INT,
        `tag_id` INT,
        CONSTRAINT `games_tags_game_id_fk`
        FOREIGN KEY (`game_id`) REFERENCES games (`game_id`),
        CONSTRAINT `games_tags_tag_id_fk`
        FOREIGN KEY (`tag_id`) REFERENCES tags (`tag_id`),
        PRIMARY KEY (`game_id`, `tag_id`)
    );