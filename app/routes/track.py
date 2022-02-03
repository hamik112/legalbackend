from fastapi import APIRouter, Depends, HTTPException,Cookie
from fastapi import Header,Request
from fastapi.responses import JSONResponse
from typing import Optional
from app.models.track import TrackHit
from app.core.logger import logger
from app.utils.dependencies import RequestsHeaders


tracker_router = APIRouter()


@tracker_router.get("/track/create")
async def index(*, request:Request, request_data: RequestsHeaders = Depends(RequestsHeaders)):
	hit_params = await request.form()
	if not request_data.hit:
		new_hit = await TrackHit(**hit_params,user_agent=request_data.user_agent,ip_address=request_data.ip_address).save()
		hit = new_hit.id
	response = JSONResponse( {"hit" : hit})
	response.set_cookie('hit',hit)
	return response
