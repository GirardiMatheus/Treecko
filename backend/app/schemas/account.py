from pydantic import BaseModel

class AccountBase(BaseModel):
  name: str
  account_type: str

class AccountCreate(AccountBase):
  balance: float = 0.0

class Account(AccountBase):
  id: int
  balance: float

class Config:
  orm_mode = True