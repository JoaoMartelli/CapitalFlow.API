from repositorio.models import Usuario
from repositorio import UsuarioRepositorio

class UsuarioAplicacao:
    def __init__(self):
        self._usuarioRepositorio = UsuarioRepositorio()

    def CriarUsuario(self, usuario: Usuario):
        self._usuarioRepositorio.CriarUsuario(usuario)