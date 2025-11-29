from datetime import datetime, timedelta
import jwt
from core.settings import settings
from core.exceptions import UnauthorizedException


def create_access_token(data: dict, expires_delta: int = 3000) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(seconds=expires_delta)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, settings.jwt_secret, algorithm=settings.jwt_algorithm
    )
    return encode_jwt


def verify_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
        )
        return payload
    except jwt.ExpiredSignature:
        raise UnauthorizedException("Token Has Expired")
    except jwt.InvalidTokenError:
        raise UnauthorizedException("Invalid Token")
