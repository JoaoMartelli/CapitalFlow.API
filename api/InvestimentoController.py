from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from aplicacao import InvestimentoAplicacao
from repositorio.models import Investimento

router = APIRouter(
    prefix="/investimento",
    tags=["Investimento"]
)

_investimentoAplicacao = InvestimentoAplicacao()

class InvestimentoCriarRequest(BaseModel):
    precoMedio: float
    quantidadeAcoes: float
    ativoId: int
    usuarioId: int

@router.post("/Criar")
def CriarUsuario(investimentoCriar: InvestimentoCriarRequest):
    try:
        investimento = Investimento(precoMedio=investimentoCriar.precoMedio, quantidadeAcoes=investimentoCriar.quantidadeAcoes, ativoId=investimentoCriar.ativoId, usuarioId=investimentoCriar.usuarioId)
        _investimentoAplicacao.CriarInvestimento(investimento)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))