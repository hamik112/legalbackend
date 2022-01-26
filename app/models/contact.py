

import ormar,datetime
from typing import Optional
from app.db import BaseMeta
from app.models.track import TrackHit

class ContactUs(ormar.Model):
    class Meta(BaseMeta):
        tablename = "contact"
    id: int = ormar.Integer(primary_key=True)
    created_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    email_address : str = ormar.String(max_length=100)
    first_name : str = ormar.String(max_length= 50)
    last_name : str = ormar.String(max_length = 50)
    message:str = ormar.String(max_length=1000)
    ip_address:str = ormar.String(max_length=100)
    hit: Optional[TrackHit] = ormar.ForeignKey(TrackHit)

    # provide your custom init function
    def __init__(self, **kwargs):
        # add value for required field without default value
        # remember to call ormar.Model init!
        super().__init__(**kwargs)


ContactRequest = ContactUs.get_pydantic(exclude={"ip_address": ..., "hit":...})
