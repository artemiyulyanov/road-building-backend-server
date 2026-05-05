from typing import Optional
from pydantic import BaseModel

TURNKEY_ASPHALT_FIELD_MAP = {
    "type": "ASPHALT_TYPE",
    "contact": "CONTACT",
    "description": "DESCRIPTION",
    "weight": "WEIGHT",
    "organization": "ORGANIZATION",
    "taxNumber": "TAX_NUMBER",
}

class TurnkeyAsphaltForm(BaseModel):
    type: str
    contact: str
    description: Optional[str] = None
    weight: Optional[int] = None
    organization: Optional[str] = None
    taxNumber: Optional[str] = None