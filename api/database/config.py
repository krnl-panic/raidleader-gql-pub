import os

from sqlalchemy.engine.url import URL, make_url
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.scoping import ScopedSession
from starlette.config import Config
from starlette.datastructures import Secret

_config = Config(".env")


DB_DRIVER = _config("DB_DRIVER", default="postgresql+asyncpg")
DB_HOST = os.getenv("DB_HOST") or _config("DB_HOST", default=None)
DB_PORT = os.getenv("DB_PORT") or _config("DB_PORT", cast=int, default=None)
DB_USER = os.getenv("DB_USER") or _config("DB_USER", default=None)
DB_PASSWORD = os.getenv("DB_PASSWORD") or _config("DB_PASSWORD", default=None)
DB_DATABASE = os.getenv("DB_DATABASE") or _config("DB_DATABASE", default=None)

DB_SSL_AUTH = os.getenv("DB_SSL_AUTH") or False

DB_DSN = os.getenv("DB_DSN") or _config(
    "DB_DSN",
    cast=make_url,  # type: ignore
    default=URL(
        drivername=DB_DRIVER,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    ),  # type: ignore
)

DB_POOL_MIN_SIZE = _config("DB_POOL_MIN_SIZE", cast=int, default=5)
DB_POOL_MAX_SIZE = _config("DB_POOL_MAX_SIZE", cast=int, default=20)
DB_ECHO = _config("DB_ECHO", cast=bool, default=False)
DB_USE_CONNECTION_FOR_REQUEST = _config(
    "DB_USE_CONNECTION_FOR_REQUEST", cast=bool, default=True
)
DB_RETRY_LIMIT = _config("DB_RETRY_LIMIT", cast=int, default=1)
DB_RETRY_INTERVAL = _config("DB_RETRY_INTERVAL", cast=int, default=1)

args = {
    "host" : DB_HOST,
    "user": DB_USER,
    "dbname": DB_DATABASE,
    "sslcert": ".certs/client.pem",
    "sslkey": ".certs/key.pem",
    "sslrootcert": ".certs/sa.pem",
    "sslmode": "verify-full"
}
engine = create_async_engine(DB_DRIVER, future=True, echo=False, connect_args=args) if DB_SSL_AUTH else create_async_engine(DB_DSN, future=True, echo=False)
Session = ScopedSession(sessionmaker(engine, expire_on_commit=False, class_=AsyncSession))
Base = declarative_base()