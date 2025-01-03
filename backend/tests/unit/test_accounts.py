from app.schemas.account import AccountCreate

def test_account_create_schema():
    account_data = {"name": "Savings", "account_type": "savings", "balance": 100.0}
    account = AccountCreate(**account_data)
    assert account.name == "Savings"
    assert account.account_type == "savings"
    assert account.balance == 100.0
