🏥Sistema de gestión de turnos para estudios de resonancia magnética.

Sistema desarrollado en **Python** con **MySQL** para la gestión integral de turnos en estudios de resonancia magnética. Permite administrar pacientes y turnos de manera eficiente.
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
  - Ver Turnos confirmados y activos 
  - Confirmar turno
  - Cancelar turno
  - Reprogramar turno
     - Fecha
     - hora
     - Cambiar equipo
- **Ver turnos de un paciente por ID del paciente**
- **Ver informacion de turno especifico**: Busqueda por ID de turno
- **Mostrar turnos por día**:
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
│   └── menu_turnos_modificar.py      # Menú de modificacion de turnos
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
('1.5T #1'),
('1.5T #2'),
('3T');

-- Insertar pacientes de ejemplo

INSERT INTO paciente (nombre, apellido, edad, obra_social, telefono) VALUES
('Juan', 'Pérez', 35, 'OSDE', '1155551234'),
('María', 'González', 42, 'Swiss Medical', '1166665678'),
('Carlos', 'Rodríguez', 28, 'Particular', '1177779012'),
('Ana', 'Martínez', 51, 'Medicus', '1188883456'),
('Roberto', 'Sánchez', 63, 'PAMI', '1199997890');

-- Insertar turnos de ejemplo

INSERT INTO turno (id_paciente, id_resonador, fecha, nombre_estudio, estado) VALUES
(1, 1, '2026-12-10 09:00:00', 'Rm cerebro', 'activo'),
(2, 2, '2026-12-10 10:30:00', 'Rm de columna', 'activo'),
(3, 1, '2026-12-10 12:00:00', 'Rm de rodilla', 'activo'),
(4, 3, '2026-12-11 09:00:00', 'Rm de abdomen', 'activo'),
(1, 2, '2026-12-11 11:00:00', 'Rm de hombro', 'Cancelado');

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

**Lo que aprendi**

**0. Diseñar antes de codear**
- Aprender que diseñar el sistema antes de tirar código no es pérdida de tiempo, es la base de todo.
- Pensar primero: ¿qué entidades hay? (paciente, turno, resonador), ¿cómo se relacionan?, ¿qué operaciones necesita el usuario?
- Hacer el diagrama de clases y el modelo relacional antes de escribir una línea de código me ahorró horas de volver atrás.
- Entender que codear es la última parte. Antes viene entender el problema, diseñar la solución, y después recién escribir código.
- Esto no significa planificar todo al detalle desde el principio, pero tener un mapa claro del sistema ayuda a no perderse.

**1. Arquitectura de software**
- Separar en capas (DAO-Dominio,Servicio,Menu,Main,Test) es fundamental para poder recorrer el proyecto, encontrar la informacion que estas buscando, saber donde modificar y poder trabajar
de una manera adecuada. Permite refactorizar sin romper todo el proyecto.
- La responsabilidad de cada capa, dao: devuelve informacion de la base de datos, menu imprime imformacion y permite navegar por el menu, servicio valida las reglas y se comunica con el dao
- Las interfaces son un mapa del dao y excelente documentacion.
- Es fundamental que los nombres sean claros porque el codigo se lee mas veces de lo que escribe.
- El principio de responsabilidad unica tiene gran importancia para que una funcion no haga 10 tareas diferentes, tener esto como guia permite escribir codigo mas limpio
  
**2. Git como herramienta de trabajo**
- Aprendi a utilizar las ramas y su funcionalidad.
- La importancia de los commits para trabajar con tranquilidad y que quede registro de todo el trabajo.

**3. Validaciones, reglas de negocio y manejo de errores** 
- La importancia y dificultad de validar las reglas del negocio.
- Separar validaciones del menu y ponerlas en el servicio. El menu pregunta y el servicio decide.
- Utilizar try/except para manejar los errores, su importancia en el debugging y como influyen en la experiencia de usuario.

**4. Testing**
- Utilizar pytest
- Como crear una base de datos para testear, testear y borrarla para poder testear el dao correctamente sin que haya informacion previa.
- Que al correr los test despues de estar modificando lo trabajo, estos ya no funcionan y prestar atencion a que esta pasando.
**5. Manejo del tiempo, paciencia y frustacion**
  -Refactorizar puede llevar mucho tiempo
  -Solucionar problemas puede ser muy dificil
  -Aceptar que esto es parte del proceso y que en un comienzo no lo sepa como hacerlo es normal. Lo importante es que con paciencia y practica lo voy a resolver.

**6. Importancia de diseñar la base de datos y el diagrama de clases**
- Al tener el diseño previo, al momento de desarrollar la aplicacion se presentaron muchos problemas menos.
- Es fundamental para no tener incongruencia de datos.
- La importancia de las claves foraneas y las relaciones bien planteadas para evitar datos huerfanos y consultas raras.

**7. El codigo siempre se puede mejorar**
- Cada vez que lo leo, encuentro algo para pulir. El codigo perfecto no existe pero si es muy importante que sea mantenible.
- Saber cuando parar y darlo por terminado.

**Agradecimientos**

A mi profesora de Programación, Ivana Soledad Rojas Córsico, que me brindó contenido de excelente calidad para poder comprender todos los conocimientos aplicados en este proyecto. Su pasión por la enseñanza fue clave para que desarrolle este proyecto.

A mi profesor de Bases de Datos, Iván Gerlero, que me brindó todo el conocimiento que hoy está aplicado en este proyecto en lo relacionado a la base de datos.

A ambos gracias por explicarme las veces que hiciera falta, y por enseñarme que el software no es solo código, sino estructura, lógica y paciencia.

**Autor**

Lautaro Emanuel Villafañe - https://www.linkedin.com/in/lautarovillafa%C3%B1e/
