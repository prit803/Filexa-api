from fastapi import APIRouter
from fastapi.responses import JSONResponse
from core.database import SessionLocal
from models.feature import Feature

router = APIRouter(prefix="/admin/features", tags=["Admin"])

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from core.database import SessionLocal
from models.feature import Feature

router = APIRouter(prefix="/features", tags=["Features"])

@router.get("")
def list_all_features():
    try:
        db = SessionLocal()

        features = db.query(Feature).order_by(Feature.id.asc()).all()

        data = [
            {
                "id": f.id,
                "feature_key": f.feature_key,
                "slug": f.slug,
                "name": f.name,
                "desc": f.desc,
                "icon": f.icon,
                "keywords": f.keywords,
                "type": f.category,
                "is_active": f.is_active,
                "seoTitle": f.seo_title,
                "seoDesc": f.seo_desc,
                "updated_at": f.updated_at.isoformat() if f.updated_at else None
            }
            for f in features
        ]

        db.close()

        return JSONResponse(
            content={
                "success": True,
                "successMessage": "All features fetched successfully",
                "data": data,
                "errorMessage": None,
                "statusCode": "200"
            },
            status_code=200
        )

    except Exception as e:
        return JSONResponse(
            content={
                "success": False,
                "successMessage": None,
                "data": None,
                "errorMessage": str(e),
                "statusCode": "500"
            },
            status_code=500
        )

@router.post("/{feature_key}/toggle")
def toggle_feature(feature_key: str, is_active: bool):
    try:
        db = SessionLocal()
        feature = db.query(Feature).filter(Feature.feature_key == feature_key).first()

        if not feature:
            return JSONResponse(
                content={
                    "success": False,
                    "successMessage": None,
                    "data": None,
                    "errorMessage": "Feature not found",
                    "statusCode": "404"
                },
                status_code=404
            )

        feature.is_active = is_active
        db.commit()
        db.close()

        return JSONResponse(
            content={
                "success": True,
                "successMessage": "Feature status updated",
                "data": {"feature": feature_key, "is_active": is_active},
                "errorMessage": None,
                "statusCode": "200"
            },
            status_code=200
        )

    except Exception as e:
        return JSONResponse(
            content={
                "success": False,
                "successMessage": None,
                "data": None,
                "errorMessage": str(e),
                "statusCode": "500"
            },
            status_code=500
        )


