from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Account(Base):
	__tablename__ = "accounts"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	balance = Column(Float, default=0.0)
	account_type = Column(String)