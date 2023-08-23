CREATE TABLE `final_Web1`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `estado` VARCHAR(45) NULL,
  `cidade` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `final_Web1`.`dados_leite_diario` (
  `id_dados_diarios` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT NOT NULL,
  `quantidade_leite` DOUBLE NOT NULL,
  `quantidade_racao` DOUBLE NULL,
  `tempo_gasto` DOUBLE NOT NULL,
  `clima` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_dados_diarios`));
