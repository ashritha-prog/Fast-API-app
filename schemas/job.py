from pydantic import BaseModel
from typing import Optional

class JobBase(BaseModel):
    title:str
    description:str
    Salary:int
    company_id:int

class JobCreate(BaseModel):
    pass
    
class JobUpdate(BaseModel):
    title: Optional[str] = None
    Salary: Optional[int] = None
