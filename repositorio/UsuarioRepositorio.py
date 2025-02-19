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

    def ObterTodosUsuarios(self):
        return self._contexto.query(Usuario).filter_by(ativo = True).all()
    
    def ObterUsuarioPorId(self, id):
        return self._contexto.query(Usuario).filter_by(id = id, ativo = True).first()