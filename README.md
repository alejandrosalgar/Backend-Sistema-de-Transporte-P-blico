# Backend-Sistema-de-Transporte-Público

Desarrollo de un sistema de transporte público en Python aplicando Programación Orientada a Objetos (POO), buenas prácticas PEP 8 con Black formatter, y flujo Git con ramas protegidas (dev, qa, prod).

## Descripción del Proyecto

Sistema interactivo de administración de transportes (Metro y Bus) con funcionalidades de gestión de usuarios, recarga de saldo y registro de compras de pasajes.

## Requisitos Técnicos

- **Python 3.8+**
- **Git** (para el flujo de ramas)
- **Black** (formatter obligatorio para PEP 8)

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/alejandrosalgar/Backend-Sistema-de-Transporte-P-blico.git
   cd Backend-Sistema-de-Transporte-P-blico
   ```

2. **Instalar Black (opcional pero recomendado):**
   ```bash
   pip install black
   ```

## Ejecución

Para ejecutar el programa:

```bash
python main.py
```

## Estructura del Proyecto

```
Backend-Sistema-de-Transporte-Público/
├── src/
│   └── entities/
│       ├── __init__.py
│       ├── transporte.py      # Clase base Transporte
│       ├── metro.py           # Subclase Metro
│       ├── buses.py           # Subclase Bus
│       ├── persona.py         # Clase base Persona
│       ├── usuario.py         # Subclase Usuario (hereda de Persona)
│       └── vector.py          # Colección de transportes
├── main.py                     # Punto de entrada del programa
├── README.md                   # Este archivo
└── clases/                    # (Archivos antiguos, no usar)
```

## Características Implementadas

### 1. Programación Orientada a Objetos (POO)
- **Encapsulamiento**: Atributos privados con propiedades (getters)
- **Herencia**: 
  - `Metro` y `Bus` heredan de `Transporte`
  - `Usuario` hereda de `Persona`
- **Polimorfismo**: Método `imprimir_data()` implementado en clases hijas
- **Type Hints**: Todos los métodos tienen type hints completos

### 2. Buenas Prácticas (PEP 8)
- Código formateado con **Black** (línea máxima 88 caracteres)
- Variables y funciones en `snake_case`
- Clases en `PascalCase`
- Docstrings en módulos, clases y métodos
- Sin `try/except` innecesarios

### 3. Flujo Git
- **Ramas protegidas**: `dev`, `qa`, `prod`
- **Ramas de aporte**: `feat/cumplimiento-completo`
- **Commits descriptivos** en español
- **Pull Requests** desde feat hacia dev, qa y prod

### 4. Funcionalidades del Programa

**Menú Principal:**
1. Agregar nuevo Metro
2. Agregar nuevo Bus
3. Mostrar todos los vehículos
4. Agregar Usuario
5. Recargar saldo a usuario
6. Registrar compra de pasaje
7. Mostrar historial de compras
8. Salir

## Clases Principales

### Transporte (Clase Base)
- Atributos privados: `_marca`, `_modelo`, `_capacidad`
- Métodos: `imprimir_data()`, propiedades getter

### Metro (hereda de Transporte)
- Atributo adicional: `_numero_estaciones`
- Método de clase: `añadir_metro()`

### Bus (hereda de Transporte)
- Atributo adicional: `_placa`
- Método de clase: `añadir_bus()`

### Persona (Clase Base)
- Atributos privados: `_nombre`, `_documento`, `_edad`, `_telefono`
- Métodos: `imprimir_data()`, `crear_persona()` (clase)

### Usuario (hereda de Persona)
- Atributos privados adicionales: `_saldo`, `_historial_compras`
- Métodos: 
  - `consultar_saldo() -> float`
  - `recargar_tarjeta(monto: float) -> bool`
  - `registrar_compra(transporte_tipo: str, monto: float) -> bool`
  - `obtener_historial() -> list`
  - `crear_usuario() -> Usuario` (clase)

### Vector (Contenedor)
- Administra colección de transportes
- Métodos: 
  - `agregar_transporte(transporte: Transporte) -> None`
  - `mostrar_transporte() -> None`

## Formato del Código

El código cumple con PEP 8 y está listo para aplicar Black:

```bash
black .
```

## Flujo de Git

El proyecto sigue un flujo de ramas protegidas:

1. **Rama feat** se crea desde **prod**
2. Pull Request desde **feat** → **dev**
3. Pull Request desde **feat** → **qa**
4. Pull Request desde **feat** → **prod**

Esto asegura que los cambios se propagan ordenadamente entre ambientes.

## Autores

**Samuel** (usuario GitHub: @chimuelo1014)
**Simon Avila (usuario GitHub: @simon7717)

## Licencia

Proyecto educativo para el curso de Programación de Software.
