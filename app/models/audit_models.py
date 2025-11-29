from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SecretAuditAcess(BaseModel):
    secret_name: str
    environment: str
    provider: str
    accessed_by: str
    accessed_at: str
    action: str
    notes: Optional[str] = None
