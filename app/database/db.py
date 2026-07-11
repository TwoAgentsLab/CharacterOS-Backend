from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config.config import DATABASE_URL

# Create the SQLAlchemy engine using the DATABASE_URL from the config
engine = create_engine(
    DATABASE_URL,
    echo=True
    )

# Create a configured "Session" class
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# Create a base class for declarative class definitions
class Base(DeclarativeBase):
    pass