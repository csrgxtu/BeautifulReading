SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

USE `shaishufang` ;

-- -----------------------------------------------------
-- Table `mydb`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shaishufang`.`Users` (
  `UserID` INT NOT NULL,
  `UserName` TEXT NULL,
  `Location` TEXT NULL,
  `TotalBooks` INT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE INDEX `UserID_UNIQUE` (`UserID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shaishufang`.`Books` (
  `ISBN` VARCHAR(13) NOT NULL,
  `BookName` TEXT NULL,
  `UserID` INT NULL,
  PRIMARY KEY (`ISBN`),
  INDEX `FK_Users_UserID_idx` (`UserID` ASC),
  CONSTRAINT `FK_Users_UserID`
    FOREIGN KEY (`UserID`)
    REFERENCES `shaishufang`.`Users` (`UserID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
