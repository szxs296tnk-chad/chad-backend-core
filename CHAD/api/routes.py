from fastapi import APIRouter
from brain.orchestrator import handle_request

router = APIRouter()

@router.post("/execute")
async def execute(data: dict):
    return await handle_request(data)
