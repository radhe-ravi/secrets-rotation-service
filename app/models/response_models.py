from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SecretResponse(BaseModel):
    name: str
    provider: str
    environment: str
    value: str
    last_rotated: Optional[datetime] = None
    version: Optional[str] = None


class AuditResponse(BaseModel):
    secret_name: str
    provider: str
    environment: str
    accessed_by: str
    accessed_at: datetime
    action: str
    notes: Optional[str] = None
