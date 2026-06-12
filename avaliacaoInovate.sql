CREATE DATABASE IF NOT EXISTS avaliacaoInovate;

USE avaliacaoInovate;

-- Criação das tabelas
CREATE TABLE produto(
	id_produto INT NOT NULL PRIMARY KEY,
	nome_produto VARCHAR(100) NOT NULL,
	preco_unitario DECIMAL(10,2) NOT NULL
);

CREATE TABLE compra(
	id_compra INT NOT NULL PRIMARY KEY,
	quantidade INT NOT NULL,
	fk_produto INT NOT NULL
);

-- Adicionando o relacionamento
ALTER TABLE compra ADD CONSTRAINT fk_compra_produto
FOREIGN KEY(fk_produto) REFERENCES produto(id_produto);

-- Inserindo os dados
-- (Dados dos produtos)
INSERT INTO produto (id_produto, nome_produto, preco_unitario) VALUES
(1, 'Arroz', 15.00), (2, 'Feijão', 8.00), (3, 'Óleo', 5.00);

-- (Dados das compras)
INSERT INTO compra (id_compra, quantidade, fk_produto) VALUES
(101, 2, 1), (102, 1, 2), (103, 3, 3);

-- Queries
-- (Questão 1)
SELECT 
	c.id_compra, p.nome_produto,
	c.quantidade, p.preco_unitario,
	(c.quantidade * p.preco_unitario) AS valor_total
FROM 
	compra c
INNER JOIN produto p ON c.fk_produto = p.id_produto
ORDER BY valor_total DESC;

-- (Questão 2)
SELECT
	p.id_produto, p.nome_produto,
	SUM(c.quantidade) AS qtd_comprada
FROM 
	compra c
INNER JOIN produto p ON c.fk_produto = p.id_produto
GROUP BY
	p.id_produto,
	p.nome_produto
ORDER BY qtd_comprada DESC
LIMIT 1;

-- (Questão 3)
SELECT
	p.id_produto, p.nome_produto,
	SUM(c.quantidade) AS qtd_comprada
FROM 
	produto p
LEFT JOIN compra c ON p.id_produto = c.fk_produto
GROUP BY
	p.id_produto,
	p.nome_produto
ORDER BY qtd_comprada DESC;
