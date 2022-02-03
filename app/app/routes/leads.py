from fastapi import APIRouter, Depends, HTTPException, Request, Header, Cookie
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.models.lead import Lead
from app.models.track import TrackHit
from app.core.logger import logger
from app.utils.dependencies import RequestsHeaders
import ormar

lead_router = APIRouter()


@lead_router.get('/lead/create')
async def leads(*, request: Request, request_data: RequestsHeaders = Depends(RequestsHeaders)):
	data = {
		"referer": request_data.referer,
		"user_agent": request_data.user_agent,
		"ip_address": request_data.ip_address,
		"hit": request_data.hit
	}
	response = JSONResponse(status_code=200, content={
		"requestData": data})
	return response


@lead_router.post("/lead/create")
async def createlead(*, request: Request, request_data: RequestsHeaders = Depends(RequestsHeaders)):
	body = await request.json()
	if request_data.hit:
		hit = await TrackHit.objects.get(id=request_data.hit)
	else:
		hit = await TrackHit(referer=request_data.referer, user_agent=request_data.user_agent,ip_address=request_data.ip_address).save()
	try:
		lead = Lead(**body, hit=hit)
		await lead.save()
		logger.info(f"Lead Saved ")
		response = JSONResponse(status_code=200, content={"message": "Lead created successfully","success": True})
	except:
		logger.info(f"Error saving lead {body}")
		response = JSONResponse(status_code=200, content={"message": "Lead already exists","success": False})
	finally:
		response.set_cookie("hit", hit.id)
	return response
