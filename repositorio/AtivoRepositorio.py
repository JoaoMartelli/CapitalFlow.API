from repositorio.models import Ativo
from repositorio.models import Investimento
from .contexto.contexto import session

class AtivoRepositorio:
    def __init__(self):
        self._contexto = session
    
    def CriarAtivo(self, ativo: Ativo):
        self._contexto.add(ativo)
        self._contexto.commit()

    def AtualizarAtivo(self, ativo: Ativo):
        self._contexto.merge(ativo)
        self._contexto.commit()

    def ObterTodosAtivos(self):
        return self._contexto.query(Ativo).filter_by(Ativo = True).all()
    
    def ObterAtivoPorId(self, id):
        return self._contexto.query(Ativo).filter_by(Id = id, Ativo = True).first()
    
    def ObterAtivosPorUsuarioId(self, usuarioId: int):
        return (
            self._contexto.query(Investimento, Ativo)
            .join(Ativo, Investimento.AtivoId == Ativo.Id)
            .filter(Investimento.UsuarioId == usuarioId, Investimento.Ativo == True)
            .all()
        )