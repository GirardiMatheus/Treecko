from fastapi import FastAPI
from app.api.v1 import accounts, debts, transactions

app = FastAPI(title="Treecko API", version="1.0.0")

# Register routes
app.include_router(accounts.router, prefix="/api/v1/accounts", tags=["Accounts"])
app.include_router(debts.router, prefix="/api/v1/debts", tags=["Debts"])
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["Transactions"])

@app.get("/")
def root():
    return {"message": "Treecko API is running!"}