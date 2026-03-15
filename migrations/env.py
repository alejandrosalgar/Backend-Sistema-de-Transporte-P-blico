"""
Alembic env.py: conecta con DATABASE_URL del .env y los modelos del proyecto.
"""

import os
import sys

from dotenv import load_dotenv

# Proyecto raíz (donde está alembic.ini y .env)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

load_dotenv(os.path.join(project_root, ".env"))

from alembic import context
from sqlalchemy import create_engine
from sqlalchemy import pool

from src.database.config import Base

# Importar todos los modelos para que Base.metadata los conozca (autogenerate)
import src.entities.estacion  # noqa: F401
import src.entities.ruta  # noqa: F401
import src.entities.tarjeta  # noqa: F401
import src.entities.usuario  # noqa: F401
import src.entities.vehiculo  # noqa: F401
import src.entities.viaje  # noqa: F401

config = context.config
target_metadata = Base.metadata


def get_url():
    """Obtener DATABASE_URL desde .env (ya cargado)."""
    url = os.getenv("DATABASE_URL")
    if not url:
        raise ValueError("DATABASE_URL no está definida en el entorno (.env)")
    return url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        get_url(),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
