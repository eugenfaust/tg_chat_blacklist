from sqlalchemy import sql, Column, BigInteger, Boolean, Text

from .base import BaseModel


class User(BaseModel):
    # Model for already working project
    __tablename__ = 'users'

    query: sql.select

    u_id = Column(BigInteger, nullable=False, primary_key=True)
    u_status = Column(Boolean, nullable=False, default=True)
    u_username = Column(Text)
    u_last_active = Column(BigInteger, nullable=False)