from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float
from repositorio.contexto.contexto import Base

class Investimento(Base):
    __tablename__ = 'Investimentos'

    Id = Column("InvestimentoID", Integer, primary_key=True, autoincrement=True, nullable=False)
    PrecoMedio = Column("PrecoMedio", Float, nullable=False)
    QuantidadeAcoes = Column("QuantidadeAcoes", Float, nullable=False)
    AtivoId = Column("AtivoID", Integer, ForeignKey("Ativos.AtivoID"), nullable=False)
    UsuarioId = Column("UsuarioID", Integer, ForeignKey("Usuarios.UsuarioID"), nullable=False)
    Ativo = Column("Ativo", Boolean, nullable=False, default=True)

    def __init__(self, precoMedio, quantidadeAcoes, ativoId, usuarioId):
        self.AtivoId = ativoId
        self.UsuarioId = usuarioId
        self.PrecoMedio = precoMedio
        self.QuantidadeAcoes = quantidadeAcoes
        self.Ativo = True