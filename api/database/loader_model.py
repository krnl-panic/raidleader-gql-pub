from datetime import datetime
from functools import reduce
from zoneinfo import ZoneInfo

from sqlalchemy import Column, Integer, func, DateTime, and_, update, insert
from sqlalchemy.future import select
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class LoaderBase(Base):
    """ """

    def __init__(self, **kwargs):
        """ """
        super(LoaderBase, self).__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

    __abstract__ = True

    def to_json(self):
        """ """
        pass

    id = Column(Integer, primary_key=True)


class TimestampMixin(object):
    """ """

    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
    deleted_at = Column(DateTime(timezone=True))


class BaseModel(LoaderBase, TimestampMixin):
    """ """

    __abstract__ = True

    @classmethod
    async def batch_loader(cls, keys, db_session):
        field_ids = [int(key) for key in keys]
        field_id = getattr(cls, "id")

        query = select(cls).where(and_(field_id.in_(field_ids), cls.deleted_at == None))
        result = await db_session.execute(query)
        rows = result.scalars().all()

        data = []
        for idx, _ in enumerate(field_ids):
            data.append(rows[idx].to_json() if idx < len(rows) else None)
        return data

    @classmethod
    async def child_batch_loader(cls, keys, parent_id_field, db_session):
        parent_ids = [int(key) for key in keys]
        field_parent_id = getattr(cls, parent_id_field)

        query = select(cls).where(and_(field_parent_id.in_(parent_ids), cls.deleted_at == None)).order_by(
            field_parent_id)
        result = await db_session.execute(query)
        rows = result.scalars().all()

        def reduce_children(value, element):
            """

            :param value:
            :param element:

            """
            parent_id = element[parent_id_field]
            children = value.get(parent_id, [])
            value[parent_id] = children + [element]
            return value

        parent_child_map = reduce(reduce_children, [_.to_json() for _ in rows], {})
        data = [parent_child_map.get(key) for key in parent_ids]
        return data

    async def create(self, db_session):
        db_session.add(self)
        await db_session.flush()

    async def update(self, db_session, **kwargs):
        q = update(self.__class__).where(and_(self.__class__.id == self.id, self.__class__.deleted_at == None))
        q = q.values(**kwargs)
        q.execution_options(synchronize_session=True)
        await db_session.execute(q)
        return self

    async def delete(self, db_session):
        q = update(self.__class__).where(and_(self.__class__.id == self.id, self.__class__.deleted_at == None))
        q = q.values(deleted_at=datetime.now(tz=ZoneInfo("America/New_York")))
        q.execution_options(synchronize_session=True)
        await db_session.execute(q)
        return self

    @classmethod
    async def get(cls, db_session, id):
        q = await db_session.execute(select(cls).where(and_(cls.id == id, cls.deleted_at == None)))
        return q.scalars().first()

    @classmethod
    async def get_all(cls, db_session):
        q = await db_session.execute(select(cls).where(cls.deleted_at == None).order_by(cls.id))
        return q.scalars().all()
