import asyncio

from gino.crud import CRUDModel
from sqlalchemy import Column, Integer, func, DateTime, and_
from functools import reduce


class LoaderBase(CRUDModel):
    """ """

    def to_json(self):
        """ """
        pass

    @classmethod
    async def batch_loader(cls, keys):
        field_ids = [int(key) for key in keys]
        field_id = getattr(cls, "id")
        query = cls.query.where(and_(field_id.in_(field_ids), cls.deleted_at.is_(None)))
        rows = await query.gino.all()
        return [_.to_json() for _ in rows]

    @classmethod
    async def child_batch_loader(cls, keys, parent_id_field):
        parent_ids = [int(key) for key in keys]
        field_parent_id = getattr(cls, parent_id_field)
        query = cls.query.where(
            and_(field_parent_id.in_(parent_ids), cls.deleted_at.is_(None))
        ).order_by(field_parent_id)
        rows = await query.gino.all()

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
        result = [parent_child_map.get(key) for key in keys]
        return result

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
