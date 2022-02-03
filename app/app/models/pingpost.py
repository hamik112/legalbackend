
import ormar,datetime
from typing import Optional
from app.db import BaseMeta
from app.models.lead import Lead
from app.enums.px import UnsoldReason

class PingPost(ormar.Model):
    class Meta(BaseMeta):
        tablename = "pingposts"
    id: int = ormar.Integer(primary_key=True)
    created_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    lead: Optional[Lead] = ormar.ForeignKey(Lead)
    price_sold = ormar.Float(nullable= True,default = 0.00,precision=2)
    sold = ormar.Boolean(default=False)
    transaction_id:str = ormar.String(max_length=100,nullable = True)
    winning_vendor = ormar.String(max_length=50, default = 'PX')
    ping_requests = ormar.JSON(default = {})
    ping_responses = ormar.JSON(default = {})
    post_requests = ormar.JSON(default = {})
    post_responses = ormar.JSON(default = {})