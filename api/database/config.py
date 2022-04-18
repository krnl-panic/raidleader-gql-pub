import os

from sqlalchemy.engine.url import URL, make_url
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.scoping import ScopedSession
from starlette.config import Config
from starlette.datastructures import Secret

_config = Config(".env")

DB_DRIVER = _config("DB_DRIVER", default="postgresql")
DB_HOST = _config("DB_HOST", default=None)
DB_PORT = _config("DB_PORT", cast=int, default=None)
DB_USER = _config("DB_USER", default=None)
DB_PASSWORD = _config("DB_PASSWORD", cast=Secret, default=None)
DB_DATABASE = _config("DB_DATABASE", default=None)
DB_DSN = os.getenv("DB_DSN") or _config(
    "DB_DSN",
    cast=make_url,
    default=URL(
        drivername=DB_DRIVER,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    ),
)
DB_POOL_MIN_SIZE = _config("DB_POOL_MIN_SIZE", cast=int, default=5)
DB_POOL_MAX_SIZE = _config("DB_POOL_MAX_SIZE", cast=int, default=20)
DB_ECHO = _config("DB_ECHO", cast=bool, default=False)
DB_SSL = _config("DB_SSL", default=None)
DB_USE_CONNECTION_FOR_REQUEST = _config(
    "DB_USE_CONNECTION_FOR_REQUEST", cast=bool, default=True
)
DB_RETRY_LIMIT = _config("DB_RETRY_LIMIT", cast=int, default=1)
DB_RETRY_INTERVAL = _config("DB_RETRY_INTERVAL", cast=int, default=1)

engine = create_async_engine(DB_DSN, future=True, echo=False)
Session = ScopedSession(sessionmaker(engine, expire_on_commit=False, class_=AsyncSession))
Base = declarative_base()
