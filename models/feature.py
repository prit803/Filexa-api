from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from core.database import Base

class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)

    # backend control
    feature_key = Column(String, unique=True, index=True)  # pdf_merge
    is_active = Column(Boolean, default=True)
    category = Column(String)  # pdf / image

    # frontend tool config
    slug = Column(String, unique=True, index=True)          # merge-pdf
    name = Column(String)
    desc = Column(String)
    icon = Column(String)
    keywords = Column(JSON, nullable=True)
    seo_title = Column(String)
    seo_desc = Column(String)

    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
