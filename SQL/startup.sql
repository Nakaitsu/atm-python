CREATE DATABASE IF NOT EXISTS caixa_eletronico;

use caixa_eletronico;

CREATE TABLE IF NOT EXISTS `caixa_eletronico`.`users` (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cpf VARCHAR(14) NOT NULL,
  endereco VARCHAR(100) NOT NULL,
  senha VARCHAR(100) NOT NULL,
  saldo DECIMAL(10,2) NOT NULL
);