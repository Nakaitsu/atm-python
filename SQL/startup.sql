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

CREATE TABLE IF NOT EXISTS `caixa_eletronico`.'cedulas' (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  valor DECIMAL(10,2) NOT NULL
  quantidade INT NOT NULL
);