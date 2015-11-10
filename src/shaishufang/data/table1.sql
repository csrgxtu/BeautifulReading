SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `shaishufang` ;
USE `shaishufang` ;

-- -----------------------------------------------------
-- Table `shaishufang`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shaishufang`.`Users` (
  `UserID` INT NOT NULL,
  `UserName` TEXT NULL DEFAULT NULL,
  `Location` TEXT NULL DEFAULT NULL,
  `TotalBooks` INT NULL DEFAULT NULL,
  `State` TINYINT(1) NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE INDEX `UserID_UNIQUE` (`UserID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `shaishufang`.`Books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shaishufang`.`Books` (
  `ISBN` VARCHAR(13) NULL,
  `BookName` TEXT NULL DEFAULT NULL,
  `UserID` INT NULL DEFAULT NULL,
  `BookID` INT NOT NULL AUTO_INCREMENT,
  `State` TINYINT(1) NULL,
  INDEX `FK_Users_UserID_idx` (`UserID` ASC),
  PRIMARY KEY (`BookID`),
  CONSTRAINT `FK_Users_UserID`
    FOREIGN KEY (`UserID`)
    REFERENCES `shaishufang`.`Users` (`UserID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
