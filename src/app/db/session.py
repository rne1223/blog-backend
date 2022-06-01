from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"

SQLALCHEMY_DATABASE_URI = "postgresql://postgres@localhost/app"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # required for sqlite
    # connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)