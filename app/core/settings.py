from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Secrets Rotation Service"
    environment: str = "development"
    debug: bool = True

    # Database
    postgres_url: str
    mongo_url: str

    # Redis
    redis_host: str
    redis_port: int

    # JWT / Security
    jwt_secret: str
    jwt_algorithm: str = "HS256"

    # Celery
    celery_broker_url: str
    celery_backend_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
