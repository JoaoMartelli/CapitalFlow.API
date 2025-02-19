from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from aplicacao import UsuarioAplicacao
from repositorio.models import Usuario

router = APIRouter(
    prefix="/usuario",
    tags=["Usuario"]
)

_usuarioAplicacao = UsuarioAplicacao()

class UsuarioCriarRequest(BaseModel):
    nome: str
    email: str
    senha: str

class UsuarioAutenticarRequest(BaseModel):
    email: str
    senha: str

class UsuarioAtualizarInformacoesRequest(BaseModel):
    usuarioId:int
    nome: str

class UsuarioAtualizarSenhaRequest(BaseModel):
    usuarioId: int
    senhaAtual: str
    novaSenha: str

class UsuarioObterResponse(BaseModel):
    usuarioId: int
    nome: str
    email: str
    ativo: bool

class UsuarioListarResponse(BaseModel):
    usuarioId: int
    nome: str
    email: str
    ativo: bool

@router.post("/Criar")
def CriarUsuario(usuarioCriar: UsuarioCriarRequest):
    try:
        usuario = Usuario(nome=usuarioCriar.nome, email=usuarioCriar.email, senha=usuarioCriar.senha)
        _usuarioAplicacao.CriarUsuario(usuario=usuario)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/Autenticar")
def AutenticarUsuario(usuarioAtenticar: UsuarioAutenticarRequest):
    try:
        usuarioId = _usuarioAplicacao.AutenticarUsuario(usuarioAtenticar.email, usuarioAtenticar.senha)
        return usuarioId
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/ObterUsuarioPorId/{usuarioId}")
def ObterTodosUsuarios(usuarioId: int):
    try:
        obterUsuario = _usuarioAplicacao.ObterUsuarioPorId(usuarioId)

        usuario = UsuarioObterResponse(
                usuarioId=obterUsuario.Id,
                nome=obterUsuario.Nome,
                email=obterUsuario.Email,
                ativo=obterUsuario.Ativo
            )
        
        return usuario
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/ListarUsuariosAtivos")
def ObterTodosUsuarios():
    try:
        usuarios = _usuarioAplicacao.ObterTodosUsuarios()

        listaUsuarios = [
            UsuarioListarResponse(
                usuarioId=usuario.Id,
                nome=usuario.Nome,
                email=usuario.Email,
                ativo=usuario.Ativo
            ) 
            for usuario in usuarios
        ]

        return listaUsuarios
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/AtualizarInformacoes")
def AtualizarInformacoes(usuarioAtualizarInformacoes: UsuarioAtualizarInformacoesRequest):
    try:
        _usuarioAplicacao.AtualizarInformacoesUsuario(usuarioAtualizarInformacoes.usuarioId, usuarioAtualizarInformacoes.nome)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/AtualizarSenha")
def AtualizarSenha(usuarioAtualizarSenha: UsuarioAtualizarSenhaRequest):
    try:
        _usuarioAplicacao.AtualizarSenhaUsuario(usuarioAtualizarSenha.usuarioId, usuarioAtualizarSenha.senhaAtual, usuarioAtualizarSenha.novaSenha)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/Desativar/{usuarioId}")
def DesativarUsuario(usuarioId: int):
    try:
        _usuarioAplicacao.DesativarUsuario(usuarioId)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))