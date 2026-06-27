from pydantic import BaseModel
from typing import Optional

class CompanyBase(BaseModel):
    name:str
    email:str
    phone:str
    

class CompanyCreate(BaseModel):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    