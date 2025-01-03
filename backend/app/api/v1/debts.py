from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_debts():
    return {"message": "Debts route is working!"}