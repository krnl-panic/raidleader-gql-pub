import os
import ssl

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

DB_DSN = os.getenv("DB_DSN") or None

DB_POOL_MIN_SIZE = _config("DB_POOL_MIN_SIZE", cast=int, default=5)
DB_POOL_MAX_SIZE = _config("DB_POOL_MAX_SIZE", cast=int, default=20)
DB_ECHO = _config("DB_ECHO", cast=bool, default=False)
DB_RETRY_LIMIT = _config("DB_RETRY_LIMIT", cast=int, default=1)
DB_RETRY_INTERVAL = _config("DB_RETRY_INTERVAL", cast=int, default=1)


# Load CA bundle for server certificate verification,
# equivalent to sslrootcert= in DSN.
try:
    sslctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=".certs/sa.pem")

    sslctx.check_hostname = False

    # Load client certificate and private key for client
    # authentication, equivalent to sslcert= and sslkey= in
    # DSN.
    sslctx.load_cert_chain(
        ".certs/client.pem",
        keyfile=".certs/key.pem",
    )
    connect_args = {"ssl": sslctx}
except:
    connect_args = None

engine = create_async_engine(
    DB_DSN, future=True, echo=False, connect_args=connect_args
)
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
