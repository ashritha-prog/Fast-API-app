from sqlalchemy import Column,Integer,String,Enum,ForeignKey,relationship
from models.company import CompanyBase
from database import Base,engine,Sessionlocal

class JobBase(Base):
    __tablename__="jobs"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    description=Column(String)
    Salary=Column(Integer)
    company_id=Column(Integer,ForeignKey("companies.id"))
    company=relationship("CompanyBase",back_populates="jobs")
    