from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from aplicacao import AtivoAplicacao
from repositorio.models import Ativo

router = APIRouter(
    prefix="/ativo",
    tags=["Ativo"]
)

_ativoAplicacao = AtivoAplicacao()

class AtivoCriarRequest(BaseModel):
    nome: str
    tag: str

class AtivoAtualizarInformacoesRequest(BaseModel):
    ativoId: int
    nome: str
    tag: str

class AtivoObterResponse(BaseModel):
    ativoId: int
    nome: str
    tag: str
    ativo: bool

class AtivoListarResponse(BaseModel):
    ativoId: int
    nome: str
    tag: str
    ativo: bool

@router.post("/Criar")
def CriarUsuario(ativoCriar: AtivoCriarRequest):
    try:
        ativo = Ativo(nome=ativoCriar.nome, tag=ativoCriar.tag)
        _ativoAplicacao.CriarAtivo(ativo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/ListarAtivosAtivos")
def ObterTodosUsuarios():
    try:
        ativos = _ativoAplicacao.ObterTodosAtivos()

        listaAtivos = [
            AtivoListarResponse(
                ativoId=ativo.Id,
                nome=ativo.Nome,
                tag=ativo.Tag,
                ativo=ativo.Ativo
            ) 
            for ativo in ativos
        ]

        return listaAtivos
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/ObterAtivoPorId/{ativoId}")
def ObterTodosUsuarios(ativoId: int):
    try:
        obterAtivo = _ativoAplicacao.ObterAtivoPorId(ativoId)

        usuario = AtivoObterResponse(
                ativoId=obterAtivo.Id,
                nome=obterAtivo.Nome,
                tag=obterAtivo.Tag,
                ativo=obterAtivo.Ativo
            )
        
        return usuario
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/AtualizarInformacoes")
def AtualizarInformacoes(ativoAtualizarInformacoes: AtivoAtualizarInformacoesRequest):
    try:
        _ativoAplicacao.AtualizarInformacoesAtivo(ativoAtualizarInformacoes.ativoId, ativoAtualizarInformacoes.nome, ativoAtualizarInformacoes.tag)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/Desativar/{ativoId}")
def DesativarUsuario(ativoId: int):
    try:
        _ativoAplicacao.DesativarAtivo(ativoId)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))