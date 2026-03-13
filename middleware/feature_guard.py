from fastapi import Request
from fastapi.responses import JSONResponse
from core.database import SessionLocal
from models.feature import Feature


EXCLUDED_PATHS = [
    "/docs",
    "/redoc",
    "/openapi.json",
]


def extract_feature_key(path: str) -> str | None:
    parts = path.strip("/").split("/")

    if len(parts) >= 2:
        category = parts[0]
        action = parts[1].replace("-", "_")

        # remove duplicate category prefix
        if action.startswith(category + "_"):
            action = action[len(category) + 1:]

        return f"{category}_{action}"

    return None


async def feature_guard(request: Request, call_next):
    path = request.url.path

    # Skip docs endpoints
    for excluded in EXCLUDED_PATHS:
        if path.startswith(excluded):
            return await call_next(request)

    # Skip admin APIs
    if path.startswith("/admin"):
        return await call_next(request)

    # Extract feature key
    feature_key = extract_feature_key(path)

    if not feature_key:
        return await call_next(request)

    db = SessionLocal()

    try:
        feature = db.query(Feature).filter(
            Feature.feature_key == feature_key
        ).first()

        if not feature or not feature.is_active:
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

    finally:
        db.close()

    return await call_next(request)