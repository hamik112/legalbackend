import sqlalchemy
from app.db import metadata,database
from app.core.config import config
from app.models.track import TrackHit
from app.models.lead import Lead
from app.models.contact import ContactUs
from app.models.pingpost import PingPost
from app.models.ccpa import CCPA

import uuid
import asyncio
import pytest


def _setup_database():
    # if you do not have the database run this once
    engine = sqlalchemy.create_engine(config.SYNC_DB_URL)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    engine.dispose()


@pytest.mark.asyncio
async def create_hit():
    await database.connect()



    hit = await TrackHit.objects.create(ip_address = '72.128.0.1',
                                   user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
                                   s1 = 'creative1',
                                   referer = "http://www.google.com")
    await database.disconnect()

if __name__=="__main__":
    print(config.SYNC_DB_URL)
    _setup_database()
    asyncio.run(create_hit())
