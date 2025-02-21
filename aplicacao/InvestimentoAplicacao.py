from repositorio.models import Investimento
from repositorio import InvestimentoRepositorio

class InvestimentoAplicacao:
    def __init__(self):
        self._investimentoRepositorio = InvestimentoRepositorio()

    def CriarInvestimento(self, investimento: Investimento):
        self._investimentoRepositorio.CriarInvestimento(investimento)