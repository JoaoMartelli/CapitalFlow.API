from sqlalchemy import Boolean, Column, Integer, String
from repositorio.contexto.contexto import Base

class Ativo(Base):
    __tablename__ = 'Ativos'

    Id = Column("AtivoID", Integer, primary_key=True, autoincrement=True, nullable=False)
    Nome = Column("Nome", String(50), nullable=False)
    Tag = Column("Tag", String(20), nullable=False, unique=True)
    Ativo = Column("Ativo", Boolean, nullable=False, default=True)

    def __init__(self, nome, tag):
        self.Nome = nome
        self.Tag = tag
        self.Ativo = True