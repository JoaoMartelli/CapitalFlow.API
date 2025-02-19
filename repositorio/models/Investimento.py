from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float
from repositorio.contexto.contexto import Base

class Investimento(Base):
    __tablename__ = 'Investimentos'

    Id = Column("InvestimentoID", Integer, primary_key=True, autoincrement=True, nullable=False)
    PrecoMedio = Column("PrecoMedio", Integer, nullable=False)
    QuantidadeAcoes = Column("QuantidadeAcoes", Float, nullable=False, unique=True)
    AtivoId = Column("AtivoID", Integer, ForeignKey("Ativos.AtivoID"), nullable=False)
    UsuarioId = Column("UsuarioID", Integer, ForeignKey("Usuarios.UsuarioID"), nullable=False)
    Ativo = Column("Ativo", Boolean, nullable=False, default=True)

    def __init__(self, nome, email, senha):
        self.Nome = nome
        self.Email = email
        self.Senha = senha
        self.Ativo = True