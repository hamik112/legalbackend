from fastapi import APIRouter, Depends, HTTPException

main_router = APIRouter()

@main_router.get("/test")
async def index(*, response: str = "Hello World!"):
	return response

