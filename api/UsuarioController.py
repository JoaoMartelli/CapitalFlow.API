from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from aplicacao import UsuarioAplicacao
from repositorio.models import Usuario

router = APIRouter()
_usuarioAplicacao = UsuarioAplicacao()

class UsuarioCriar(BaseModel):
    nome: str
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