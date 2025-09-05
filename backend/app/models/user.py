from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    account_type = Column(String)  # e.g., 'admin', 'user'
    usage_intent = Column(String)   # e.g., 'personal', 'commercial'
    consent_flags = Column(Boolean, default=False)  # User consent for data usage

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email}, account_type={self.account_type})>"