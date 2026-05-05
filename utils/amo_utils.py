import httpx
import os

from dtos.turnkey_asphalt import TURNKEY_ASPHALT_FIELD_MAP
from utils.dto_utils import build_custom_fields

AMO_DOMAIN = os.getenv("AMO_DOMAIN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

async def create_turnkey_asphalt_lead(data):
    global ACCESS_TOKEN

    payload = [
        {
            "name": "Заявка с сайта",
            "custom_fields_values": build_custom_fields(data.dict(), TURNKEY_ASPHALT_FIELD_MAP),
        }
    ]

    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"https://{AMO_DOMAIN}/api/v4/leads",
            json=payload,
            headers={
                "Authorization": f"Bearer {ACCESS_TOKEN}",
                "Content-Type": "application/json",
            },
        )

        return res.json()