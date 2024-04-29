-- SQLite
CREATE TABLE CLIENTE (
  id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_cliente VARCHAR(255) NOT NULL,
  endereco VARCHAR(255) NOT NULL,
  telefone VARCHAR(20) NOT NULL,
  email VARCHAR(50) NOT NULL
);
CREATE TABLE COMPRA (
  id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
  data_compra DATE NOT NULL,
  valor_total DECIMAL(10,2) NOT NULL,
  id_cliente INTEGER NOT NULL,
  id_funcionario INTEGER NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente),
  FOREIGN KEY (id_funcionario) REFERENCES FUNCIONARIO(id_funcionario)
);
CREATE TABLE FUNCIONARIO (
  id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_funcionario VARCHAR(255) NOT NULL,
  cargo VARCHAR(50) NOT NULL,
  data_admissao DATE NOT NULL,
  id_departamento INTEGER NOT NULL,
  FOREIGN KEY (id_departamento) REFERENCES DEPARTAMENTO(id_departamento)
);
CREATE TABLE DEPARTAMENTO (
  id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_departamento VARCHAR(50) NOT NULL,
  responsavel VARCHAR(50) NOT NULL
);
CREATE TABLE COMPANHIA (
  id_companhia INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_companhia VARCHAR(255) NOT NULL,
  cnpj VARCHAR(14) NOT NULL,
  endereco VARCHAR(255) NOT NULL
);
CREATE TABLE ITEM_DE_COMPRA (
  id_item_compra INTEGER PRIMARY KEY AUTOINCREMENT,
  id_compra INTEGER NOT NULL,
  id_produto INTEGER NOT NULL,
  quantidade INTEGER NOT NULL,
  valor_unitario DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (id_compra) REFERENCES COMPRA(id_compra),
  FOREIGN KEY (id_produto) REFERENCES PRODUTO(id_produto)
);
CREATE TABLE PRODUTO (
  id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_produto VARCHAR(255) NOT NULL,
  descricao TEXT NOT NULL,
  valor_unitario DECIMAL(10,2) NOT NULL,
  id_fornecedor INTEGER NOT NULL,
  FOREIGN KEY (id_fornecedor) REFERENCES FORNECEDOR(id_fornecedor)
);
CREATE TABLE FORNECEDOR (
  id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_fornecedor VARCHAR(255) NOT NULL,
  cnpj VARCHAR(14) NOT NULL,
  endereco VARCHAR(255) NOT NULL
);
CREATE TABLE ESTOQUE (
  id_estoque INTEGER PRIMARY KEY AUTOINCREMENT,
  id_produto INTEGER NOT NULL,
  quantidade_estoque INTEGER NOT NULL,
  data_atualizacao DATE NOT NULL,
  FOREIGN KEY (id_produto) REFERENCES PRODUTO(id_produto)
);


-- Inserir dados na tabela CLIENTE
INSERT INTO CLIENTE (nome_cliente, endereco, telefone, email) VALUES
('João Silva', 'Rua A, 123', '(00) 1234-5678', 'joao@example.com'),
('Maria Santos', 'Av. B, 456', '(00) 9876-5432', 'maria@example.com'),
('Pedro Oliveira', 'Rua C, 789', '(00) 2468-1357', 'pedro@example.com'),
('Ana Lima', 'Av. D, 321', '(00) 5555-5555', 'ana@example.com'),
('Lucas Pereira', 'Rua E, 654', '(00) 7777-7777', 'lucas@example.com');

-- Inserir dados na tabela DEPARTAMENTO
INSERT INTO DEPARTAMENTO (nome_departamento, responsavel) VALUES
('Vendas', 'José Silva'),
('RH', 'Ana Oliveira'),
('Financeiro', 'Mariana Santos'),
('TI', 'Paulo Lima'),
('Logística', 'Carlos Pereira');

-- Inserir dados na tabela FUNCIONARIO
INSERT INTO FUNCIONARIO (nome_funcionario, cargo, data_admissao, id_departamento) VALUES
('Fernanda Oliveira', 'Vendedor', '2023-01-15', 1),
('Rafael Santos', 'Analista de RH', '2022-03-20', 2),
('Mariana Lima', 'Analista Financeiro', '2021-05-10', 3),
('Paulo Pereira', 'Analista de Sistemas', '2020-07-25', 4),
('Carla Silva', 'Gerente de Logística', '2019-09-30', 5);

-- Inserir dados na tabela COMPANHIA
INSERT INTO COMPANHIA (nome_companhia, cnpj, endereco) VALUES
('Empresa A', '12345678901234', 'Av. X, 789'),
('Empresa B', '98765432109876', 'Rua Y, 654'),
('Empresa C', '56789012345678', 'Rua Z, 321'),
('Empresa D', '43210987654321', 'Av. W, 987'),
('Empresa E', '87654321098765', 'Rua V, 1234');

-- Inserir dados na tabela FORNECEDOR
INSERT INTO FORNECEDOR (nome_fornecedor, cnpj, endereco) VALUES
('Fornecedor 1', '09876543210987', 'Rua Fornecedora, 123'),
('Fornecedor 2', '67890123456789', 'Av. dos Fornecedores, 456'),
('Fornecedor 3', '34567890123456', 'Rua das Entregas, 789'),
('Fornecedor 4', '90123456789012', 'Av. das Vendas, 321'),
('Fornecedor 5', '12345678901234', 'Rua dos Produtos, 654');

-- Inserir dados na tabela PRODUTO
INSERT INTO PRODUTO (nome_produto, descricao, valor_unitario, id_fornecedor) VALUES
('Produto 1', 'Descrição do Produto 1', 100.00, 1),
('Produto 2', 'Descrição do Produto 2', 50.00, 2),
('Produto 3', 'Descrição do Produto 3', 75.00, 3),
('Produto 4', 'Descrição do Produto 4', 120.00, 4),
('Produto 5', 'Descrição do Produto 5', 80.00, 5);

-- Inserir dados na tabela COMPRA
INSERT INTO COMPRA (data_compra, valor_total, id_cliente, id_funcionario) VALUES
('2024-04-27', 250.00, 1, 1),
('2024-04-26', 200.00, 2, 2),
('2024-04-25', 300.00, 3, 3),
('2024-04-24', 180.00, 4, 4),
('2024-04-23', 150.00, 5, 5);

-- Inserir dados na tabela ITEM_DE_COMPRA
INSERT INTO ITEM_DE_COMPRA (id_compra, id_produto, quantidade, valor_unitario) VALUES
(1, 1, 2, 100.00),
(2, 2, 3, 50.00),
(3, 3, 4, 75.00),
(4, 4, 1, 120.00),
(5, 5, 2, 80.00);

-- Inserir dados na tabela ESTOQUE
INSERT INTO ESTOQUE (id_produto, quantidade_estoque, data_atualizacao) VALUES
(1, 10, '2024-04-28'),
(2, 20, '2024-04-28'),
(3, 15, '2024-04-28'),
(4, 8, '2024-04-28'),
(5, 12, '2024-04-28');
