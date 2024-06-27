from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from SQL_Engine import engine

Base = declarative_base()

class PessoaDB(Base):
    __tablename__ = 'pessoas'
    matricula = Column(Integer(), primary_key=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer(), nullable=False)
    

if __name__ == "__main__":
    Base.metadata.create_all(engine)