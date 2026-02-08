from fastapi import Request
from fastapi.responses import JSONResponse
from core.database import SessionLocal
from models.feature import Feature

async def feature_guard(request: Request, call_next):
    feature_key = request.headers.get("X-Feature-Key")

    if feature_key:
        db = SessionLocal()
        feature = db.query(Feature).filter(
            Feature.feature_key == feature_key,
            Feature.is_active == True
        ).first()
        db.close()

        if not feature:
            return JSONResponse(
                content={
                    "success": False,
                    "successMessage": None,
                    "data": None,
                    "errorMessage": "This feature is currently disabled",
                    "statusCode": "403"
                },
                status_code=403
            )

    return await call_next(request)
