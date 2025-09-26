from sqlmodel import SQLModel
from app.db.session import engine
from app.models import gold_models 
def create_db_and_tables():
    print("Creating database and tables...")
    SQLModel.metadata.create_all(engine)
    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_db_and_tables()