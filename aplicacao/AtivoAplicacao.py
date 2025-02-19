from repositorio.models import Ativo
from repositorio import AtivoRepositorio

class AtivoAplicacao:
    def __init__(self):
        self._ativoRepositorio = AtivoRepositorio()

    def CriarAtivo(self, ativo: Ativo):
        self._ativoRepositorio.CriarAtivo(ativo)

    def AtualizarInformacoesAtivo(self, ativoId, nome, tag):
        ativo = self._ativoRepositorio.ObterAtivoPorId(ativoId)

        if not ativo:
            raise Exception("Ativo não encontrado!")
        
        ativo.Nome = nome
        ativo.Tag = tag

        self._ativoRepositorio.AtualizarAtivo(ativo)

    def DesativarAtivo(self, ativoId):
        ativo = self._ativoRepositorio.ObterAtivoPorId(ativoId)
        
        if not ativo:
            raise Exception("Ativo não encontrado!")
        
        ativo.Ativo = False

        self._ativoRepositorio.AtualizarAtivo(ativo)

    def ObterTodosAtivos(self):
        return self._ativoRepositorio.ObterTodosAtivos()
    
    def ObterAtivoPorId(self, ativoId: int):
        ativo = self._ativoRepositorio.ObterAtivoPorId(ativoId)
    
        if not ativo:
            raise Exception("Ativo não encontrado!")
        
        return ativo