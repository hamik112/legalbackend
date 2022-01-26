from fastapi import APIRouter, Depends, HTTPException, Request, Header, Cookie
from fastapi.responses import JSONResponse
from app.models.lead import Lead
from app.models.track import TrackHit
from app.core.logger import logger
from app.utils.dependencies import RequestsHeaders
lead_router = APIRouter()


@lead_router.post("/create")
async def createlead(*, request:Request, request_data: RequestsHeaders = Depends(RequestsHeaders)):
	body = await request.json()
	if request_data.hit:
		hit = await TrackHit.objects.get(request_data.hit)
	else:
		hit = await TrackHit(referer=request_data.referer, user_agent=request_data.user_agent,ip_address=request_data.ip_address).save()
	lead = Lead(**body, hit = hit)
	await lead.save()
	response = JSONResponse(status_code=200, content={"message": "Lead created successfully"})
	response.set_cookie("hit", hit.id)
	return response