from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Community(Base):
    __tablename__ = 'communities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(Integer, nullable=False)
    owner_id = Column(Integer, nullable=False)  # Assuming this links to a User model

    def __repr__(self):
        return f"<Community(name={self.name}, owner_id={self.owner_id})>"