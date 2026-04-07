# API Sistema de Transporte Público

## Descripción General

API REST desarrollada con **FastAPI** para gestionar un sistema completo de transporte público. Incluye gestión de usuarios, tarjetas, estaciones, vehículos, rutas y viajes.

## Cambios Realizados

### 1. Actualización de `src/api/app.py`
- ✅ Se reemplazaron los imports incorrectos de módulos de e-commerce por los correctos del transporte
- ✅ Se importan ahora: `usuario`, `tarjeta`, `estacion`, `vehiculo`, `ruta`, `viaje`
- ✅ Se registran la todas las entidades en el lifespan
- ✅ Se incluyen todos los routers con `app.include_router()`
- ✅ Se mejoró la descripción y título de la API

### 2. Creación de Routers
Se crearon 6 nuevos archivos router en `src/api/`:

#### `usuario.py`
- **POST** `/usuarios/` - Crear usuario
- **GET** `/usuarios/{id_usuario}` - Obtener usuario por ID
- **GET** `/usuarios/` - Obtener todos los usuarios
- **PUT** `/usuarios/{id_usuario}` - Actualizar usuario
- **POST** `/usuarios/login` - Login con credenciales

#### `tarjeta.py`
- **POST** `/tarjetas/` - Crear tarjeta
- **GET** `/tarjetas/{id_tarjeta}` - Obtener tarjeta por ID
- **GET** `/tarjetas/` - Obtener todas las tarjetas
- **GET** `/tarjetas/usuario/{id_usuario}` - Obtener tarjetas de un usuario
- **PUT** `/tarjetas/{id_tarjeta}` - Actualizar tarjeta
- **DELETE** `/tarjetas/{id_tarjeta}` - Eliminar tarjeta

#### `estacion.py`
- **POST** `/estaciones/` - Crear estación
- **GET** `/estaciones/{id_estacion}` - Obtener estación por ID
- **GET** `/estaciones/` - Obtener todas las estaciones
- **PUT** `/estaciones/{id_estacion}` - Actualizar estación
- **DELETE** `/estaciones/{id_estacion}` - Eliminar estación

#### `vehiculo.py`
- **POST** `/vehiculos/` - Crear vehículo
- **GET** `/vehiculos/{id_vehiculo}` - Obtener vehículo por ID
- **GET** `/vehiculos/` - Obtener todos los vehículos
- **PUT** `/vehiculos/{id_vehiculo}` - Actualizar vehículo
- **DELETE** `/vehiculos/{id_vehiculo}` - Eliminar vehículo

#### `ruta.py`
- **POST** `/rutas/` - Crear ruta
- **GET** `/rutas/{id_ruta}` - Obtener ruta por ID
- **GET** `/rutas/` - Obtener todas las rutas
- **GET** `/rutas/activas` - Obtener solo rutas activas
- **GET** `/rutas/codigo/{codigo}` - Obtener ruta por código
- **PUT** `/rutas/{id_ruta}` - Actualizar ruta

#### `viaje.py`
- **POST** `/viajes/` - Crear viaje
- **GET** `/viajes/{id_viaje}` - Obtener viaje por ID
- **GET** `/viajes/` - Obtener todos los viajes
- **GET** `/viajes/ruta/{id_ruta}` - Obtener viajes de una ruta
- **GET** `/viajes/vehiculo/{id_vehiculo}` - Obtener viajes de un vehículo
- **GET** `/viajes/estacion/origen/{id_estacion}` - Obtener viajes que salen de una estación
- **GET** `/viajes/estacion/destino/{id_estacion}` - Obtener viajes que llegan a una estación
- **PUT** `/viajes/{id_viaje}` - Actualizar viaje
- **DELETE** `/viajes/{id_viaje}` - Eliminar viaje

### 3. Mejoras en CRUDs

#### `src/crud/tarjeta_crud.py`
- ✅ Se mejoró la documentación
- ✅ Se añadieron funciones `obtener_por_usuario()` y `obtener_activas()`
- ✅ Se normalizó la firma del método `actualizar()`
- ✅ Se añadieron parámetros `tipo` y `activo` 

### 4. Actualización de `src/api/__init__.py`
- ✅ Se añadieron imports de todos los routers
- ✅ Se creó `__all__` para exportar módulos

### 5. Actualización de `requirements.txt`
- ✅ Se añadió `fastapi>=0.104.0`
- ✅ Se añadió `uvicorn[standard]>=0.24.0`

## Cómo Ejecutar la API

### Instalación de dependencias
```bash
pip install -r requirements.txt
```

### Configurar variables de entorno
Crear un archivo `.env` con:
```
DATABASE_URL=postgresql://usuario:contraseña@host:puerto/basedatos
```

### Ejecutar el servidor
```bash
uvicorn src.api.app:app --reload --host 0.0.0.0 --port 8000
```

### Acceder a la documentación
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Estructura de Datos

### Usuario
```json
{
  "id_usuario": "uuid",
  "nombre_usuario": "string",
  "rol": "string",
  "activo": true
}
```

### Tarjeta
```json
{
  "id_tarjeta": "uuid",
  "saldo": 100.00,
  "tipo": "string | null",
  "activo": true,
  "id_usuario": "uuid"
}
```

### Estación
```json
{
  "id_estacion": "uuid",
  "nombre": "string",
  "direccion": "string | null"
}
```

### Vehículo
```json
{
  "id_vehiculo": "uuid",
  "placa": "string",
  "modelo": "string | null",
  "capacidad": "int | null"
}
```

### Ruta
```json
{
  "id_ruta": "uuid",
  "codigo": "string",
  "nombre": "string | null",
  "activo": true
}
```

### Viaje
```json
{
  "id_viaje": "uuid",
  "id_ruta": "uuid",
  "id_vehiculo": "uuid",
  "id_estacion_origen": "uuid",
  "id_estacion_destino": "uuid",
  "fecha_hora_salida": "2024-01-01T10:00:00"
}
```

## Testing

Puedes usar herramientas como:
- **Postman** - Para hacer requests HTTP
- **curl** - Desde terminal
- **Thunder Client** - Extensión de VSCode

Ejemplo con curl:
```bash
# Obtener todos los usuarios
curl http://localhost:8000/usuarios/

# Obtener documentación
curl http://localhost:8000/docs
```

## Notas Importantes

1. ✅ Todos los CRUDs son funcionales y se sincronizaron con los routers
2. ✅ La API usa SQLAlchemy ORM con PostgreSQL
3. ✅ Incluye validación automática con Pydantic
4. ✅ La documentación interactiva está disponible en `/docs`
5. ✅ El endpoint `/health` verifica el estado de la API

## Próximos Pasos (Recomendaciones)

1. Implementar autenticación JWT
2. Añadir paginación a los endpoints GET
3. Implementar filtros avanzados en búsquedas
4. Añadir tests unitarios
5. Configurar CORS si es necesario
