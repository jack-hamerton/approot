from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Safeguard(Base):
    __tablename__ = 'safeguards'

    id = Column(Integer, primary_key=True, index=True)
    ethical_check_name = Column(String, index=True)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    compliance_level = Column(String)  # e.g., 'high', 'medium', 'low'
    created_at = Column(String)  # Consider using DateTime for actual timestamps
    updated_at = Column(String)  # Consider using DateTime for actual timestamps

    def __repr__(self):
        return f"<Safeguard(id={self.id}, name={self.ethical_check_name}, active={self.is_active})>"