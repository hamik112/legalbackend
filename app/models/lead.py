import ormar,datetime
from ormar import Extra
from typing import Optional,List
from app.db import BaseMeta
from app.models.track import TrackHit
from app.enums.px import Gender,EntranceExists,Ownership,SquareFootage,ProInstallation,SecurityType,SecurityUsage,InstallationTimeFrame,HasSystem
from app.utils.defaults import generate_datetime
from app.core.logger import logger

class Lead(ormar.Model):
    class Meta(BaseMeta):
        tablename = "legalleads"
        extra = Extra.ignore
    # provide your custom init function
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    id: int = ormar.Integer(primary_key=True)
    created_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    first_name:str = ormar.String(max_length=25)
    last_name:str = ormar.String(max_length=25)
    email:str = ormar.String(max_length=100,unique=True)
    phone:str = ormar.String(max_length=50,unique=True)
    year: str = ormar.String(max_length=20)
    diagnosis: str = ormar.String(max_length = 50)
    formula: str = ormar.String(max_length = 50)
    injuries: List[str]  = ormar.JSON(default=dict)
    trusted_form: str = ormar.String(max_length=1000,nullable=True)
    original_url: str = ormar.String(max_length=255,default ="https://instanthomesecurityquotes.com")
    tcpa_text:str = ormar.String(max_length = 2000)
    hit: Optional[TrackHit] = ormar.ForeignKey(TrackHit)
