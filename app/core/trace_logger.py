from minio import Minio
import json, datetime
from app.config import settings

client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=settings.MINIO_SECURE
)

def store_audit_trace(trace):
    timestamp = datetime.datetime.utcnow().isoformat()
    object_name = f"{timestamp}.json"
    data = json.dumps(trace).encode("utf-8")
    client.put_object(
        bucket_name=settings.MINIO_BUCKET,
        object_name=object_name,
        data=data,
        length=len(data),
        content_type="application/json"
    )
