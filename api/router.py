from fastapi import APIRouter

from utils.amo_utils import create_turnkey_asphalt_lead
from dtos.turnkey_asphalt import TurnkeyAsphaltForm

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"msg": "pong", "status": 200}

@router.post("/turnkey-asphalt-lead")
async def lead_endpoint(data: TurnkeyAsphaltForm):
    return await create_turnkey_asphalt_lead(data)