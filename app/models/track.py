import ormar,datetime
from typing import Optional
from app.db import BaseMeta

class TrackHit(ormar.Model):
    class Meta(BaseMeta):
        tablename = "trackhits"
    id: int = ormar.Integer(primary_key=True)
    created_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    ip_address:str = ormar.String(max_length=100)
    referer:str = ormar.String(max_length = 500,nullable = True)
    user_agent:str= ormar.String(max_length = 2000, nullable = True)
    s1:str = ormar.String(max_length = 250, nullable = True)
    s2:str = ormar.String(max_length = 250, nullable = True)
    s3:str = ormar.String(max_length = 250, nullable = True)

    # provide your custom init function
    def __init__(self, **kwargs):
        # add value for required field without default value
        # remember to call ormar.Model init!
        super().__init__(**kwargs)
