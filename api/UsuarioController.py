from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from aplicacao import UsuarioAplicacao
from repositorio.models import Usuario

router = APIRouter(
    prefix="/usuario",
    tags=["Usuario"]
)

_usuarioAplicacao = UsuarioAplicacao()

class UsuarioCriar(BaseModel):
    nome: str
    email: str
    senha: str

class UsuarioAutenticar(BaseModel):
    email: str
    senha: str

@router.post("/criar")
def CriarUsuario(usuarioCriar: UsuarioCriar):
    try:
        usuario = Usuario(nome=usuarioCriar.nome, email=usuarioCriar.email, senha=usuarioCriar.senha)
        _usuarioAplicacao.CriarUsuario(usuario=usuario)
        return {"message": "Usuário criado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/autenticar")
def AutenticarUsuario(usuarioAtenticar: UsuarioAutenticar):
    try:
        usuarioId = _usuarioAplicacao.AutenticarUsuario(usuarioAtenticar.email, usuarioAtenticar.senha)
        return usuarioId
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# @router.get("/ListarUsuariosAtivos")
# def ObterTodosUsuarios(usuarioCriar: UsuarioCriar):
#     try:
#         usuario = Usuario(nome=usuarioCriar.nome, email=usuarioCriar.email, senha=usuarioCriar.senha)
#         _usuarioAplicacao.CriarUsuario(usuario=usuario)
#         return {"message": "Usuário criado com sucesso"}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
    
# @router.post("/criar")
# def CriarUsuario(usuarioCriar: UsuarioCriar):
#     try:
#         usuario = Usuario(nome=usuarioCriar.nome, email=usuarioCriar.email, senha=usuarioCriar.senha)
#         _usuarioAplicacao.CriarUsuario(usuario=usuario)
#         return {"message": "Usuário criado com sucesso"}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))