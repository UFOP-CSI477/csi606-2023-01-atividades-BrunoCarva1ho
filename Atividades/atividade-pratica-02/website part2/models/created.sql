
/* COMANDOS EXECUTADOS PARA CRIAÇÃO DO BANCO DE DADOS (MySQL Workbench)*/

create table estados(
    id int primary key auto_increment,
    nome varchar(100),
    sigla varchar(2),
    created_at timestamp,
    updated_at timestamp
);

create table cidades(
    id int primary key auto_increment,
    nome varchar(60),
    estado_id int,
    foreign key(estado_id) references estados(id),
    created_at timestamp,
    updated_at timestamp
);

create table usuarios(
    id int primary key auto_increment,
    nome varchar(60),
    email varchar(100),
    senha varchar(50),
    created_at timestamp,
    updated_at timestamp
);

create table enderecos(
    id int primary key auto_increment,
    usuario_id int,
    foreign key (usuario_id) references usuarios(id),
    rua varchar(100),
    numero varchar(10),
    bairro varchar(100),
    cidade_id int,
    foreign key (cidade_id) references cidades(id),
    telefone varchar(20),
    created_at timestamp,
    updated_at timestamp
);

create table compras(
    id int primary key auto_increment,
    usuario_id int,
    foreign key (usuario_id) references usuarios(id),
    endereco_id int,
    foreign key (endereco_id) references enderecos(id),
    data_ datetime,
    created_at timestamp,
    updated_at timestamp
);

create table compras_produtos(
    id int primary key auto_increment,
    usuario_id int,
    foreign key (usuario_id) references usuarios(id),
    produto_id int,
    foreign key (produto_id) references produtos(id),
    quantidate int,
    valor_unitario float,
    created_at timestamp,
    updated_at timestamp
);

CREATE TABLE produtos(
  id int NOT NULL AUTO_INCREMENT,
  descricao varchar(60) DEFAULT NULL,
  valor_unitario float DEFAULT NULL,
  created_at timestamp NULL DEFAULT NULL,
  updated_at timestamp NULL DEFAULT NULL,
  PRIMARY KEY (id)
);