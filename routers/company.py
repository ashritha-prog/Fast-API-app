from fastapi import APIRouter
router =APIRouter(prefix="/company",tags=["company"])

@router.get("/")
def read_company():
    return {"company": "company root"}

@router.get("/{Company_id}")
def read_company(Company_id: int):
    return {"company_id": "company_id"}
