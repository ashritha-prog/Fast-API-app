from sqlalchemy import Column,Integer,String,enum,realtionship
from database import Base, engine,SessionLocal


class CompanyBase(Base):
    __tablename__="companies"
    id = Column(Integer,primary_key=True,index=True)
    name= Column(String,nullable=False,index=True)
    email = Column(String,unique=True)
    phone = Column(String,unique=True)
    jobs=realtionship("JobBase",back_populates="company")
    