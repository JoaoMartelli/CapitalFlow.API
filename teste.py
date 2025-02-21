from repositorio import AtivoRepositorio

_ativoRepositorio = AtivoRepositorio()

investimentos = _ativoRepositorio.ObterAtivosPorUsuarioId(1)

# Exibir os dados de forma mais legível
for investimento, ativo in investimentos:
    print(f"Ativo ID: {ativo.Id}, Nome: {ativo.Nome}, Tag: {ativo.Tag}")
