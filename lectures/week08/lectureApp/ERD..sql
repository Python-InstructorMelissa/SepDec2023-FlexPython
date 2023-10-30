-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema anime
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema anime
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `anime` DEFAULT CHARACTER SET utf8 ;
USE `anime` ;

-- -----------------------------------------------------
-- Table `anime`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `anime`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(255) NULL,
  `lastName` VARCHAR(255) NULL,
  `username` VARCHAR(255) NULL,
  `createdAt` DATETIME NULL DEFAULT NOW(),
  `updatedAt` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `anime`.`anime`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `anime`.`anime` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `tvShow` VARCHAR(255) NULL,
  `alignment` VARCHAR(255) NULL,
  `power` VARCHAR(255) NULL,
  `createdAt` DATETIME NULL DEFAULT NOW(),
  `updatedAt` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_anime_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_anime_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `anime`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
