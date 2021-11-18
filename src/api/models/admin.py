from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.types import DateTime
import datetime

from api.db.base_model import Base

class Admin(Base):
    __tablename__ = "admins"

    admin_id = Column(Integer, primary_key=True, index=False)
    admin_email = Column(String, unique=True, nullable=False)
    admin_password = Column(String, nullable=False)
    
    
    created_on = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    last_login = Column(DateTime(timezone=True), nullable=True)