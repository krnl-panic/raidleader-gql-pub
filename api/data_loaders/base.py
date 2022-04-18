from aiodataloader import DataLoader
from sqlalchemy.ext.asyncio import AsyncSession


class BaseLoader(DataLoader):
    __abstract__ = True

    def __init__(self, db_session: AsyncSession):
        super(BaseLoader, self).__init__()
        self.db_session = db_session
