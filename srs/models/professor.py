from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

DATABASE_URL = "sqlite:///university.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

class Professor(Base):
    __tablename__ = "Professor"  

    pID = Column(String, primary_key=True)      
    pname = Column(String, nullable=False)      
    password = Column("pass", String, nullable=False)  
   
Base.metadata.create_all(engine)
