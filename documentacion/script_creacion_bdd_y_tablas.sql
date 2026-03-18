CREATE DATABASE IF NOT EXISTS gestor_de_turnos;
USE gestor_de_turnos;

-- Tabla paciente
CREATE TABLE paciente (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    obra_social VARCHAR(50) NOT NULL,
    telefono VARCHAR(20) NOT NULL
);

-- Tabla resonador
CREATE TABLE resonador (
    id_resonador INT AUTO_INCREMENT PRIMARY KEY,
    nombre_equipo VARCHAR(50)
);

-- Tabla turno
CREATE TABLE turno (
    id_turno INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_resonador INT NOT NULL,
    fecha DATETIME NOT NULL,
    nombre_estudio VARCHAR(50) NOT NULL,
    estado VARCHAR(20) NOT NULL,

    FOREIGN KEY (id_paciente) REFERENCES paciente(id_paciente),
    FOREIGN KEY (id_resonador) REFERENCES resonador(id_resonador)
);