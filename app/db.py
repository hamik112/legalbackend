import ormar
import databases
import sqlalchemy
from app.core.config import config


database = databases.Database(config.DATABASE_URL)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


