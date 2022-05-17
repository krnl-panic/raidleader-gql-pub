import os
import ssl

from logging.config import fileConfig
from alembic import context
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool

load_dotenv()  # take environment variables from .env.

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

DB_SYNC_DSN = os.getenv("DB_SYNC_DSN", "Default://")
DB_USE_SSL = os.getenv("DB_USE_SSL", 0)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.


    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.


    """
    ssl_context = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH, cafile=".certs/sa.pem"
    )
    ssl_context.load_cert_chain(certfile=".certs/client.pem", keyfile=".certs/key.pem")
    args = {
        "sslrootcert": ".certs/sa.pem",
        "sslcert": ".certs/client.pem",
        "sslkey": ".certs/key.pem",
        "sslmode": "verify-ca",
    } if DB_USE_SSL == 1 else {}
    
    engine = create_engine(
        DB_SYNC_DSN, poolclass=pool.NullPool, echo=False, connect_args=args
    )

    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
