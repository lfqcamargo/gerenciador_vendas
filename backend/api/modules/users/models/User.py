import uuid
from datetime import date, datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Integer, Date, DateTime, LargeBinary, func, Column
from sqlalchemy.orm import Mapped, mapped_column

from api.shared.database.connection import Base

def test():
    print("Teste")

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)
    cpf_cnpj: Mapped[str] = mapped_column(String(14), nullable=False, unique=True)
    whatsapp: Mapped[str] = mapped_column(String(14), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    sex: Mapped[str] = mapped_column(String(1), nullable=False)
    data_birthday: Mapped[date] = mapped_column(Date(), nullable=False)
    date_created: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=func.now())
    status: Mapped[int] = mapped_column(Integer(), nullable=False, default=1)
    profile_photo: Mapped[bytes] = mapped_column(LargeBinary(), nullable=True)
    date_login: Mapped[datetime] = mapped_column(Date(), nullable=True)
    
class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String)