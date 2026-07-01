from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.company import Company
from schemas.company import CompanyCreate, CompanyUpdate, CompanyResponse

router = APIRouter(prefix="/company", tags=["Company"])


@router.post("/", response_model=CompanyResponse, status_code=status.HTTP_201_CREATED)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company(**company.model_dump())

    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company


@router.get("/", response_model=list[CompanyResponse])
def get_companies(db: Session = Depends(get_db)):
    return db.query(Company).all()


@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == company_id).first()

    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    return company


@router.put("/{company_id}", response_model=CompanyResponse)
def update_company(
    company_id: int,
    company: CompanyUpdate,
    db: Session = Depends(get_db)
):
    db_company = db.query(Company).filter(Company.id == company_id).first()

    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    for key, value in company.model_dump(exclude_unset=True).items():
        setattr(db_company, key, value)

    db.commit()
    db.refresh(db_company)

    return db_company


@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.id == company_id).first()

    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    db.delete(db_company)
    db.commit()

    return {"message": "Company deleted successfully"}