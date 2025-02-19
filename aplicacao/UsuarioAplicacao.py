from repositorio.models import Usuario
from repositorio import UsuarioRepositorio

class UsuarioAplicacao:
    def __init__(self):
        self._usuarioRepositorio = UsuarioRepositorio()

    def CriarUsuario(self, usuario: Usuario):
        self._usuarioRepositorio.CriarUsuario(usuario)

    def AutenticarUsuario(self, email, senha):
        usuario = self._usuarioRepositorio.ObterUsuarioPorEmail(email)

        if not usuario:
            raise Exception("Email ou senha incorreto.")

        if usuario.Senha != senha:
            raise Exception("Email ou senha incorreto.")
        
        return usuario.Id
    
    def AtualizarInformacoesUsuario(self, usuarioId, nome):
        usuario = self._usuarioRepositorio.ObterUsuarioPorId(usuarioId)

        if not usuario:
            raise Exception("Usuário não encontrado!")
        
        usuario.Nome = nome

        self._usuarioRepositorio.AtualizarUsuario(usuario)

    def AtualizarSenhaUsuario(self, usuarioId, senhaAtual, novaSenha):
        usuario = self._usuarioRepositorio.ObterUsuarioPorId(usuarioId)
        
        if not usuario:
            raise Exception("Usuário não encontrado!")
        
        if usuario.Senha != senhaAtual:
            raise Exception("Senha atual incorreta!")
        
        usuario.Senha = novaSenha

        self._usuarioRepositorio.AtualizarUsuario(usuario)

    def DesativarUsuario(self, usuarioId):
        usuario = self._usuarioRepositorio.ObterUsuarioPorId(usuarioId)
        
        if not usuario:
            raise Exception("Usuário não encontrado!")
        
        usuario.Ativo = False

        self._usuarioRepositorio.AtualizarUsuario(usuario)

    def ObterTodosUsuarios(self):
        return self._usuarioRepositorio.ObterTodosUsuarios()
    
    def ObterUsuarioPorId(self, usuarioId: int):
        usuario = self._usuarioRepositorio.ObterUsuarioPorId(usuarioId)
        
        if not usuario:
            raise Exception("Usuário não encontrado!")
        
        return usuario