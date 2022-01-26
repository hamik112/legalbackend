from typing import Optional
from fastapi import Request,Header,Depends,Cookie

class IpAddressUseragent:
    def __init__(self,request:Request, user_agent: Optional[str] = Header(None)):
        self.ip_address = request.client.host
        self.user_agent = user_agent


class RequestsHeaders:
    def __init__(self,request:Request,
                 referer: Optional[str] = Header(None),
                 user_agent: Optional[str] = Header(None),
                 hit: Optional[str] = Cookie(None),
                 conversion: Optional[str] = Cookie(False)
                 ):
        self.ip_address = request.client.host
        self.user_agent = user_agent
        self.hit = hit
        self.referer = referer
        self.conversion = conversion

