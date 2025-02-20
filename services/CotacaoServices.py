import yfinance as yf

class CotacaoServico:
    @staticmethod
    def ObterCotacaoAtualPorTag(tag: str):
        try:
            ativo = yf.Ticker(tag)
            cotacao = ativo.history(period="1d")["Close"].iloc[-1]
            return round(cotacao, 2)
        
        except Exception:
            return None