from sqlalchemy import Boolean, Column, Integer, String
from repositorio.contexto.contexto import Base

class Usuario(Base):
    __tablename__ = "Usuarios"

    Id = Column("UsuarioID", Integer, primary_key=True, autoincrement=True, nullable=False)
    Nome = Column("Nome", String(100), nullable=False)
    Email = Column("Email", String(150), nullable=False, unique=True)
    Senha = Column("Senha", String(30), nullable=False)
    Ativo = Column("Ativo", Boolean, nullable=False, default=True)

    def __init__(self, nome, email, senha):
        self.Nome = nome
        self.Email = email
        self.Senha = senha
        self.Ativo = True