# import yfinance as yf

# class CotacaoServico:
#     @staticmethod
#     def ObterCotacaoAtualPorTag(tag: str):
#         try:
#             ativo = yf.Ticker(tag)
#             cotacao = ativo.history(period="1d")["Close"].iloc[-1]
#             return {"ativo": tag, "cotacao": cotacao}
#         except Exception as e:
#             return {"erro": f"Erro ao obter cotação: {str(e)}"}
        
#     @staticmethod
#     def ObterCotacaoAtualPorLista(ativos: list[str]):
#         resultados = []
#         for tag in ativos:
#             resultados.append(CotacaoServico.ObterCotacaoAtualPorTag(tag))
#         return resultados