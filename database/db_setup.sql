CREATE DATABASE helpdesk_db;

-- so a vm do backend tem acesso
CREATE USER 'user_api'@'10.20.30.2' IDENTIFIED BY 'j1j2m3';
GRANT ALL PRIVILEGES ON helpdesk_db.* TO 'user_api'@'10.20.30.2';
FLUSH PRIVILEGES;

USE helpdesk_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    departamento VARCHAR(50) NOT NULL
);

CREATE TABLE chamados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT NOT NULL,
    status ENUM('Aberto', 'Em Andamento', 'Resolvido') DEFAULT 'Aberto',
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

INSERT INTO usuarios (nome, departamento) VALUES ('Mike', 'Engenharia'), ('Ana', 'RH');
INSERT INTO chamados (titulo, descricao, usuario_id) VALUES ('Internet caindo', 'Cabo com mau contato', 1);