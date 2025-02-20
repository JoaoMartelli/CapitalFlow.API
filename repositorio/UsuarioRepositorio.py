from repositorio.models import Usuario
from .contexto.contexto import session

class UsuarioRepositorio:
    def __init__(self):
        self._contexto = session
    
    def CriarUsuario(self, usuario: Usuario):
        self._contexto.add(usuario)
        self._contexto.commit()

    def AtualizarUsuario(self, usuario: Usuario):
        self._contexto.merge(usuario)
        self._contexto.commit()

    x
    
    def ObterUsuarioPorId(self, id):
        return self._contexto.query(Usuario).filter_by(Id = id, Ativo = True).first()
    
    def ObterUsuarioPorEmail(self, email):
        return self._contexto.query(Usuario).filter_by(Email = email, Ativo = True).first()