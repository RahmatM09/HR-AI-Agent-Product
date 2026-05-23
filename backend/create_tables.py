from app.core.database import Base, engine
from app.models.job import Job
from app.models.application import Application
from app.models.user import User

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    create_tables()
