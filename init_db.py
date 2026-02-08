from core.database import engine
from models.feature import Feature
from core.database import Base

Base.metadata.create_all(bind=engine)
print("Database initialized")
