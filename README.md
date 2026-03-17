🏥Sistema de gestión de turnos para estudios de resonancia magnética.

Sistema desarrollado en **Python** con **MySQL** para la gestión integral de turnos en estudios de resonancia magnética. Permite administrar pacientes y turnos de manera eficiente, con funcionalidades específicas para centros médicos.
Se divide en dos módulos principales

Modulo pacientes:
- **Crear paciente**: Registro de nuevos pacientes con sus datos personales
- **Modificar paciente**: Actualizacion de informacion de pacientes existentes
- **Eliminar paciente**: Baja de pacientes del sistema
- **Mostrar paciente por ID**: Busqueda especifica de un paciente
- **Mostrar todos los pacientes**: Listado completo de pacientes registrados

Modulo turnos:
- **Registrar turno**
- **Modificar turno**:
  - Cancelar turno
  - Reprogramar turno
  - Cambiar equipo
- **Ver turnos de un paciente por ID del paciente**
- **Ver informacion de turno especifico**: Busqueda por ID de turno
- **Mostrar turnos por dí**a:
  - Permite usar la fecha actual o ingresar una manual
  - Los turnos se muestran ordenados cronológicamente
  - Se agrupan por resonador

 Tecnologias:
 -**Python**
 -**MySQL**
 -**Pytest**
 -**mysql-connector**

## 📁 Estructura del proyecto

```
Proyecto-gestor-de-turnos/
│
├── main.py                          # Punto de entrada de la aplicación
├── .gitignore                       # Archivos ignorados por git
│
├── dao/                             # Capa de acceso a datos
│   ├── __init__.py
│   ├── paciente_dao.py              # Operaciones CRUD de pacientes
│   ├── turno_dao.py                 # Operaciones CRUD de turnos
│   └── interfaz_dao/                 # Interfaces abstractas
│       ├── __init__.py
│       ├── interfaz_paciente_dao.py # Interfaz para paciente DAO
│       └── interfaz_turno_dao.py    # Interfaz para turno DAO
│
├── db/                               # Configuración de base de datos
│   ├── __init__.py
│   ├── db_conn.py                    # Conexión a MySQL
│   ├── config.ini                    # Configuración de BD (crear uno)
│   ├── config.example.ini            # Ejemplo de configuración
│   └── test_config.ini               # Configuración para pruebas
│
├── dominio/                          # Capa de modelos/entidades
│   ├── __init__.py
│   ├── paciente.py                   # Clase Paciente
│   └── turno.py                      # Clase Turno
│
├── menus/                            # Capa de presentación
│   ├── __init__.py
│   ├── menu_pacientes.py             # Menú de operaciones de pacientes
│   └── menu_turnos.py                # Menú de operaciones de turnos
│
├── servicio/                         # Capa de lógica de negocio
│   ├── __init__.py
│   ├── servicio_paciente.py          # Lógica de negocio para pacientes
│   └── servicio_turno.py             # Lógica de negocio para turnos
│
├── test_tdd/                         # Pruebas unitarias con Pytest
│   ├── __init__.py
│   ├── test_dao_paciente.py          # Tests del DAO de pacientes
│   ├── test_dao_turno.py             # Tests del DAO de turnos
│   ├── test_paciente.py              # Tests del modelo Paciente
│   └── test_turno.py                 # Tests del modelo Turno
│
└── documentation/                    # Documentación adicional
    ├── diagrama_de_clases_GDT.png    # Diagrama de clases UML
    ├── modelo_relacional_GDT.png     # Modelo relacional de la BD
    ├── schema.sql                    # Esquema de la base de datos
    └── script_creacion_bdd_y_tablas.sql # Script completo de creación
```




## Instalación:
Sigue estos pasos para instalar y ejecutar el proyecto localmente:

### Prerrequisitos:

 -Python 3.8 o superior instalado

 -MySQL Server 8.0 o superior instalado

 -pip (gestor de paquetes de python)

1. **Clonar el repositorio**:
   git clone https://github.com/lautiiv/Proyecto-gestor-de-turnos

   cd Proyecto-gestor-de-turnos
   
2. **Crear y activar entorno virtual**:
   (Windows)
   
   python -m venv venv
   
   venv\Scripts\activate
   
3. **Instalar dependencias**

   pip install -r requirements.txt

4. **Configurar la base de datos**:

- Accede a MySQL y crea la base de datos manualmente:
  
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

5. **Realizar unos inserts para tener informacion en la base de datos**


-- Insertar resonadores
INSERT INTO resonador (nombre_equipo) VALUES 
('Resonador 1 - 1.5T'),
('Resonador 2 - 3.0T'),
('Resonador 3 - Abierto');

-- Insertar pacientes de ejemplo

INSERT INTO paciente (nombre, apellido, edad, obra_social, telefono) VALUES
('Juan', 'Pérez', 35, 'OSDE', '1155551234'),
('María', 'González', 42, 'Swiss Medical', '1166665678'),
('Carlos', 'Rodríguez', 28, 'Particular', '1177779012'),
('Ana', 'Martínez', 51, 'Medicus', '1188883456'),
('Roberto', 'Sánchez', 63, 'PAMI', '1199997890');

-- Insertar turnos de ejemplo

INSERT INTO turno (id_paciente, id_resonador, fecha, nombre_estudio, estado) VALUES
(1, 1, '2024-12-10 09:00:00', 'Rm cerebro', 'activo'),
(2, 2, '2024-12-10 10:30:00', 'Rm de columna', 'activo'),
(3, 1, '2024-12-10 12:00:00', 'Rm de rodilla', 'activo'),
(4, 3, '2024-12-11 09:00:00', 'Rm de abdomen', 'activo'),
(1, 2, '2024-12-11 11:00:00', 'Rm de hombro', 'Cancelado');

6. **Configurar la conexión a la base de datos**:

Edita el archivo db/config.ini con tus credenciales:

[database]

host = localhost

user = tu_usuario

port = 3306

password = tu_contraseña

database = gestor_de_turnos

7. **Configurar la conexión a la base de datos para los tests**:

Edita el archivo db/test_config.ini

[database]

host = localhost

user = tu_usuario

port = 3306

password = tu_contraseña

database = test_turnos

 8. **Ejecutar la aplicación**:

(bash)

py main.py

 9. **Ejecutar pruebas**:

pytest test_tdd/ -v

📊 **Diagramas**
Los diagramas UML y modelo relacional están disponibles en la carpeta documentation/:

diagrama_de_clases_GDT.png

modelo_relacional_GDT.png

**Autor**
Lautaro E. Villafañe - 
