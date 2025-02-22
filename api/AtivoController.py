from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from aplicacao import AtivoAplicacao
from repositorio.models import Ativo
from services.CotacaoServices import CotacaoServico

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

class AtivoListarComCotacaoResponse(BaseModel):
    ativoId: int
    nome: str
    tag: str
    ativo: bool
    cotacao: float

class InvestimentosDeUmUsuario(BaseModel):
    ativoId: int
    investimentoId: int
    nomeAtivo: str
    tag: str
    quantidadeAcoes: int
    precoMedio: float
    cotacao: float
    rendimento: float
    totalInvestido: float
    rendimentoTotal: float

@router.post("/Criar")
def CriarAtivo(ativoCriar: AtivoCriarRequest):
    try:
        ativo = Ativo(nome=ativoCriar.nome, tag=ativoCriar.tag)
        _ativoAplicacao.CriarAtivo(ativo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/ListarAtivosComCotacao", response_model=list[AtivoListarComCotacaoResponse])
def ObterAtivosComCotacao():
    try:
        ativos = _ativoAplicacao.ObterTodosAtivos()
        
        listaAtivos = [
            AtivoListarComCotacaoResponse(
                ativoId=ativo.Id,
                nome=ativo.Nome,
                tag=ativo.Tag,
                ativo=ativo.Ativo,
                cotacao=CotacaoServico.ObterCotacaoAtualPorTag(ativo.Tag)
            ) 
            for ativo in ativos
        ]

        return listaAtivos
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/ListarAtivos")
def ObterTodosAtivos():
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
def ObterAtivoPorId(ativoId: int):
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

@router.get("/ObterAtivosPorUsuarioId/{usuarioId}")
def ObterAtivosPorUsuarioId(usuarioId: int):
    try:
        
        investimentos = _ativoAplicacao.ObterAtivosPorUsuarioId(usuarioId)

        investimentosResposta = []

        for investimento, ativo in investimentos:
            cotacaoAtual = CotacaoServico.ObterCotacaoAtualPorTag(ativo.Tag)
            investimentosResposta.append(
                InvestimentosDeUmUsuario(
                    ativoId = ativo.Id,
                    investimentoId = investimento.Id,
                    nomeAtivo = ativo.Nome,
                    tag = ativo.Tag,
                    quantidadeAcoes = investimento.QuantidadeAcoes,
                    precoMedio = investimento.PrecoMedio,
                    cotacao = cotacaoAtual,
                    rendimento = round(((cotacaoAtual - investimento.PrecoMedio) / investimento.PrecoMedio) * 100, 2),
                    totalInvestido = round(investimento.PrecoMedio * investimento.QuantidadeAcoes, 2),
                    rendimentoTotal = round(cotacaoAtual * investimento.QuantidadeAcoes, 2)
                )
            )

        return investimentosResposta
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/AtualizarInformacoes")
def AtualizarInformacoes(ativoAtualizarInformacoes: AtivoAtualizarInformacoesRequest):
    try:
        _ativoAplicacao.AtualizarInformacoesAtivo(ativoAtualizarInformacoes.ativoId, ativoAtualizarInformacoes.nome, ativoAtualizarInformacoes.tag)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/Desativar/{ativoId}")
def DesativarAtivo(ativoId: int):
    try:
        _ativoAplicacao.DesativarAtivo(ativoId)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
