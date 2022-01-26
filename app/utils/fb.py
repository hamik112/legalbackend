import time
from facebook_business.adobjects.serverside.action_source import ActionSource
from facebook_business.adobjects.serverside.content import Content
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request_async import EventRequestAsync
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.api import FacebookAdsApi



async def fire_fb_pixel(access_token,pixel_id,event_source_url,conversion_value,ip_address, user_agent,fbc,fbp):
    FacebookAdsApi.init(access_token=access_token)
    user_data = UserData(fbc =  fbc, fbp = fbp , client_ip_address=ip_address, client_user_agent=user_agent)
    custom_data = CustomData(currency="usd", value=conversion_value)
    event = Event(
        event_name="Lead",
        event_time=int(time.time()),
        user_data=user_data,
        custom_data=custom_data,
        data_processing_options=[],
        event_source_url=event_source_url,
        action_source=ActionSource.WEBSITE
    )
    event_request_async = EventRequestAsync(events=[event],pixel_id=pixel_id)
    return await event_request_async.execute()



