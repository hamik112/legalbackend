from fastapi import APIRouter, Depends, HTTPException, Request, Header, Cookie
from fastapi.responses import JSONResponse
from app.models.contact import ContactUs
from app.models.track import TrackHit
from typing import Optional
from app.core.logger import logger
from app.utils.dependencies import RequestsHeaders
from app.core.consts import CONTACT_ERROR_MESSAGE,CONTACT_SUCCESS_MESSAGE

contact_router = APIRouter()


@contact_router.post("/create")
async def contactform(*, request: Request, request_data: RequestsHeaders = Depends(RequestsHeaders)):
	body = await request.json()
	if request_data.hit:
		hit = await TrackHit.objects.get(request_data.hit)
	else:
		hit = await TrackHit(referer=request_data.referer,
		                     user_agent=request_data.user_agent,
		                     ip_address=request_data.ip_address).save()
	contact_us = await ContactUs(**body, ip_address=request_data.ip_address, hit=hit).save()
	logger.info(contact_us)
	try:
		contact_us = await ContactUs(**body, ip_address=request_data.ip_address, hit=hit).save()
		response = JSONResponse(status_code = 200 , content = {"success":True,"message":CONTACT_SUCCESS_MESSAGE})
	except:
		response = JSONResponse(status_code = 200 , content = {"success":True,"message":CONTACT_ERROR_MESSAGE})
	response.set_cookie("hit", hit.id)
	return response
