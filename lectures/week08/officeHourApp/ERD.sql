-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema parkAnimals
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `parkAnimals` ;

-- -----------------------------------------------------
-- Schema parkAnimals
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `parkAnimals` DEFAULT CHARACTER SET utf8 ;
USE `parkAnimals` ;

-- -----------------------------------------------------
-- Table `parkAnimals`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `parkAnimals`.`user` ;

CREATE TABLE IF NOT EXISTS `parkAnimals`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(255) NULL,
  `lastName` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `createdAt` DATETIME NULL DEFAULT NOW(),
  `updatedAt` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parkAnimals`.`park`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `parkAnimals`.`park` ;

CREATE TABLE IF NOT EXISTS `parkAnimals`.`park` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `location` VARCHAR(255) NULL,
  `createdAt` DATETIME NULL DEFAULT NOW(),
  `updatedAt` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_park_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_park_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `parkAnimals`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parkAnimals`.`animal`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `parkAnimals`.`animal` ;

CREATE TABLE IF NOT EXISTS `parkAnimals`.`animal` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `species` VARCHAR(255) NULL,
  `appendages` INT NULL,
  `willToLive` TINYINT NULL,
  `isDead` TINYINT NULL,
  `health` VARCHAR(255) NULL,
  `createdAt` DATETIME NULL DEFAULT NOW(),
  `updatedAt` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_animal_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_animal_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `parkAnimals`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parkAnimals`.`color`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `parkAnimals`.`color` ;

CREATE TABLE IF NOT EXISTS `parkAnimals`.`color` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `color` VARCHAR(255) NULL,
  `createdAt` DATETIME NULL DEFAULT NOW(),
  `updatedAt` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parkAnimals`.`animal_has_color`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `parkAnimals`.`animal_has_color` ;

CREATE TABLE IF NOT EXISTS `parkAnimals`.`animal_has_color` (
  `animal_id` INT NOT NULL,
  `color_id` INT NOT NULL,
  PRIMARY KEY (`animal_id`, `color_id`),
  INDEX `fk_animal_has_color_color1_idx` (`color_id` ASC) VISIBLE,
  INDEX `fk_animal_has_color_animal1_idx` (`animal_id` ASC) VISIBLE,
  CONSTRAINT `fk_animal_has_color_animal1`
    FOREIGN KEY (`animal_id`)
    REFERENCES `parkAnimals`.`animal` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_animal_has_color_color1`
    FOREIGN KEY (`color_id`)
    REFERENCES `parkAnimals`.`color` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parkAnimals`.`weather`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `parkAnimals`.`weather` ;

CREATE TABLE IF NOT EXISTS `parkAnimals`.`weather` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `temp` DECIMAL NULL,
  `humidity` DECIMAL NULL,
  `description` TEXT NULL,
  `pressure` DECIMAL NULL,
  `icon` VARCHAR(255) NULL,
  `createdAt` DATETIME NULL DEFAULT NOW(),
  `updatedAt` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_weather_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_weather_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `parkAnimals`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parkAnimals`.`profile`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `parkAnimals`.`profile` ;

CREATE TABLE IF NOT EXISTS `parkAnimals`.`profile` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `lat` DECIMAL NULL,
  `lon` DECIMAL NULL,
  `createdAt` DATETIME NULL DEFAULT NOW(),
  `updatedAt` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_profile_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_profile_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `parkAnimals`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parkAnimals`.`park_has_animal`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `parkAnimals`.`park_has_animal` ;

CREATE TABLE IF NOT EXISTS `parkAnimals`.`park_has_animal` (
  `park_id` INT NOT NULL,
  `animal_id` INT NOT NULL,
  PRIMARY KEY (`park_id`, `animal_id`),
  INDEX `fk_park_has_animal_animal1_idx` (`animal_id` ASC) VISIBLE,
  INDEX `fk_park_has_animal_park1_idx` (`park_id` ASC) VISIBLE,
  CONSTRAINT `fk_park_has_animal_park1`
    FOREIGN KEY (`park_id`)
    REFERENCES `parkAnimals`.`park` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_park_has_animal_animal1`
    FOREIGN KEY (`animal_id`)
    REFERENCES `parkAnimals`.`animal` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
