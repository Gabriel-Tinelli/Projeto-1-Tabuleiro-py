CREATE TABLE `tags` (
  `tag_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(30) NOT NULL,
  `type` enum('Mechanism','Theme','Other') NOT NULL DEFAULT 'Theme',
  PRIMARY KEY (`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;