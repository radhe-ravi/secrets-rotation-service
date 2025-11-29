from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Secret(BaseModel):
    name: str
    value: str
    provider: str
    environment: str
    last_rotated: Optional[datetime] = None
    version: Optional[str] = None
