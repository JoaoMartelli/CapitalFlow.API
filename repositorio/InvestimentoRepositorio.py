from repositorio.models import Investimento
from .contexto.contexto import session

class InvestimentoRepositorio:
    def __init__(self):
        self._contexto = session

    def CriarInvestimento(self, investimento: Investimento):
        self._contexto.add(investimento)
        self._contexto.commit()

    def AtualizarInvestimento(self, investimento: Investimento):
        self._contexto.merge(investimento)
        self._contexto.commit()

    def ObterTodosInvestimentos(self):
        return self._contexto.query(Investimento).filter_by(Ativo = True).all()
    
    def ObterInvestimentoPorId(self, id):
        return self._contexto.query(Investimento).filter_by(Id = id, Ativo = True).first()
