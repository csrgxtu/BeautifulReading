SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `shaishufang` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `shaishufang` ;

-- -----------------------------------------------------
-- Table `mydb`.`Proxies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shaishufang`.`Proxies` (
  `ProxyID` INT NOT NULL,
  `Proxy` CHAR(21) NULL,
  PRIMARY KEY (`ProxyID`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;