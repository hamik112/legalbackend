import ormar,datetime
from ormar import Extra
from typing import Optional
from app.db import BaseMeta
from app.models.track import TrackHit
from app.enums.px import Gender,EntranceExists,Ownership,SquareFootage,ProInstallation,SecurityType,SecurityUsage,InstallationTimeFrame,HasSystem
from app.utils.defaults import generate_datetime
from app.core.logger import logger

class Lead(ormar.Model):
    class Meta(BaseMeta):
        tablename = "leads"
        extra = Extra.ignore
    # provide your custom init function
    def __init__(self, **kwargs):
        logger.info(kwargs)
        property_type = kwargs.get('propertytype')
        servicetype = kwargs.get('servicetype')
        installation_type = kwargs.get('installation')

        if property_type == "rental":
            kwargs['security_usage'] = SecurityUsage.Residential.value
            kwargs['ownership'] =  Ownership.Rented.value
        if property_type == "home":
            kwargs['security_usage'] = SecurityUsage.Residential.value
            kwargs['ownership'] =  Ownership.Owned.value
        if property_type == "commercial":
            kwargs['security_usage'] = SecurityUsage.Commercial.value
            kwargs['ownership'] =  Ownership.Rented.value

        if servicetype == "newinstallation":
            kwargs['has_system'] = HasSystem.No.value
        if servicetype == "reactivateexisting":
            kwargs['has_system'] = HasSystem.Yes.value
        if servicetype == "equipmentonly":
            kwargs['has_system'] = HasSystem.No.value

        if installation_type == "professional":
            kwargs['pro_install'] = ProInstallation.Yes.value
        if installation_type == "selfinstall":
            kwargs['pro_install'] = ProInstallation.No.value
        if installation_type == "nopreference":
            kwargs['pro_install'] = ProInstallation.Yes.value
        logger.info(kwargs)
        super().__init__(**kwargs)

    id: int = ormar.Integer(primary_key=True)
    created_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    first_name:str = ormar.String(max_length=25)
    last_name:str = ormar.String(max_length=25)
    email:str = ormar.String(max_length=100)
    phone_number:str = ormar.String(max_length=50)
    universal_leadid:str = ormar.String(max_length=250,nullable=True)
    trusted_form: str = ormar.String(max_length=1000,nullable=True)
    original_url: str = ormar.String(max_length=255,default ="https://instanthomesecurityquotes.com")
    tcpa_text:str = ormar.String(max_length = 2000)
    session_length:int = ormar.Integer()
    street_address:str= ormar.String(max_length = 250)
    city:str= ormar.String(max_length = 75)
    state:str= ormar.String(max_length = 2)
    zip_code: str= ormar.String(max_length = 10)
    dob: str= ormar.DateTime(nullable = True, default = generate_datetime())
    gender:str = ormar.String(max_length = 15, choices = list(Gender),default = Gender.male)
    installation_time_frame:str = ormar.String(max_length=50, choices = list(InstallationTimeFrame),default = InstallationTimeFrame.Immediately)
    security_usage:str = ormar.String(max_length=50, choices = list(SecurityUsage))
    security_type:str = ormar.String(max_length=50, choices = list(SecurityType),default = SecurityType.OnlyBurglar)
    pro_install:str = ormar.String(max_length=50, choices = list(ProInstallation))
    square_footage:str = ormar.String(max_length=50, choices = list(SquareFootage),default = SquareFootage.TwoThousandFiveHundredToFiveThousand)
    has_system:str = ormar.String(max_length=30, choices = list(HasSystem))
    entrances_exits:str  = ormar.String(max_length=10, choices = list(EntranceExists),default = EntranceExists.Two)
    ownership:str = ormar.String(max_length=30, choices = list(Ownership))
    hit: Optional[TrackHit] = ormar.ForeignKey(TrackHit)
