from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from app.databases.db import Base, DATABASE_URL
from app.models.user import User
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.consulting_room import ConsultingRoom
from app.models.appointment import Appointment
from app.models.doctor_room import DoctorRoom

config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)
else:
    raise ValueError("DATABASE_URL is not set. Check your environment variables.")


target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
