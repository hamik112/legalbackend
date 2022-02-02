import ormar,datetime
from typing import Optional
from app.db import BaseMeta
from app.models.track import TrackHit
from app.enums.ccpa import CCPARequestType

class CCPA(ormar.Model):
    class Meta(BaseMeta):
        tablename = "ccpa"
    id: int = ormar.Integer(primary_key=True)
    created_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    email_address : str = ormar.String(max_length=100)
    first_name : str = ormar.String(max_length=25)
    phone_number : str =ormar.String(max_length=25)
    last_name : str = ormar.String(max_length=25)
    request_type:str = ormar.String(choices = list(CCPARequestType), max_length=50)
    ip_address:str = ormar.String(max_length=100)
    hit: Optional[TrackHit] = ormar.ForeignKey(TrackHit)


    # provide your custom init function
    def __init__(self, **kwargs):
        # add value for required field without default value
        # remember to call ormar.Model init!
        super().__init__(**kwargs)

