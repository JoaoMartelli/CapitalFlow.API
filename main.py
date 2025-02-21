from fastapi import FastAPI
from api import usuario_router, ativo_router, investimento_router
from repositorio.contexto.contexto import Base, contexto
import uvicorn

app = FastAPI()

app.include_router(usuario_router)
app.include_router(ativo_router)
app.include_router(investimento_router)

Base.metadata.create_all(bind=contexto)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)