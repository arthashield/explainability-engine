from pydantic import BaseSettings

class Settings(BaseSettings):
    MINIO_ENDPOINT: str = "127.0.0.1:9000"
    MINIO_ACCESS_KEY: str = "admin"
    MINIO_SECRET_KEY: str = "password"
    MINIO_BUCKET: str = "arthashield-audit-logs"
    MINIO_SECURE: bool = False

settings = Settings()
