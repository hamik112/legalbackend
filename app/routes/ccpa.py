from fastapi import APIRouter, Request,Header,Depends,Cookie
from app.models.ccpa import CCPA
from fastapi.responses import JSONResponse

from app.models.track import TrackHit
from app.utils.dependencies import RequestsHeaders
from app.core.logger import logger
from app.core.consts import CCPA_SUCCESS_MESSAGE, CCPA_ERROR_MESSAGE



ccpa_route = APIRouter()


@ccpa_route.post("/create")
async def ccpa_create(*, request:Request, request_data: RequestsHeaders = Depends(RequestsHeaders)):
	body = await request.json()
	if request_data.hit:
		hit = await TrackHit.objects.get(request_data.hit)
	else:
		hit = await TrackHit(referer=request_data.referer, user_agent=request_data.user_agent,ip_address=request_data.ip_address).save()
	logger.info(body)
	try:
		ccpa_request = await CCPA(**body,ip_address=request_data.ip_address, hit = hit).save()
		response = JSONResponse(status_code = 200 , content = {"success":True,"message":CCPA_SUCCESS_MESSAGE})
	except:
		response = JSONResponse(status_code = 200 , content = {"success":False,"message":CCPA_ERROR_MESSAGE})
	response.set_cookie("hit", hit.id)
	return response