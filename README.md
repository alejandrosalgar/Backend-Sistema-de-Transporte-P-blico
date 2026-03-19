# Backend-Sistema-de-Transporte-Público

Sistema de administración de transporte público desarrollado en Python con SQLAlchemy ORM, base de datos PostgreSQL en Neon, migraciones con Alembic y flujo Git con ramas protegidas.

## Descripción del Proyecto

Sistema interactivo para gestionar entidades de transporte público con trazabilidad de auditoría, persistencia en base de datos en la nube (Neon) y operaciones CRUD completas.

## Entidades

| Entidad | Descripción | Auditoría |
|---|---|---|
| Usuario | Usuario del sistema | — |
| Tarjeta | Tarjeta de transporte del usuario | ✅ |
| Ruta | Ruta de transporte | ✅ |
| Viaje | Viaje realizado en una ruta | ✅ |
| Vehiculo | Vehículo que opera la ruta | — |
| Estacion | Estación de origen o destino | — |

## Relaciones

- Usuario 1 → N Tarjeta
- Ruta 1 → N Viaje
- Vehiculo 1 → N Viaje
- Estacion 1 → N Viaje (como origen y como destino)
- Usuario referenciado en auditoría de Tarjeta, Ruta y Viaje

## Requisitos Técnicos

- Python 3.8+
- PostgreSQL en Neon (base de datos en la nube)
- SQLAlchemy (ORM)
- Alembic (migraciones)
- python-dotenv (variables de entorno)

## Instalación

1. Clonar el repositorio:
bash
   git clone https://github.com/alejandrosalgar/Backend-Sistema-de-Transporte-P-blico.git
   cd Backend-Sistema-de-Transporte-P-blico


2. Crear entorno virtual e instalar dependencias:
bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt


3. Configurar variables de entorno:
bash
   cp .env.example .env
   # Editar .env y agregar tu DATABASE_URL de Neon


4. Ejecutar migraciones:
bash
   python -m alembic upgrade head


## Ejecución
bash
python main.py


## Flujo Git

1. Rama feat/* se crea desde dev
2. Pull Request: feat → dev
3. Pull Request: feat → qa
4. Pull Request: feat → prod

## Autores

- Samuel (@chimuelo1014)
- Simon Avila (@simon7717)

## Video demostrativo

🎥 URL del video: (agregar aquí la URL cuando esté grabado)

## Licencia

Proyecto educativo para el curso de Programación de Software.