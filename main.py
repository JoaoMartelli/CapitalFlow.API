from fastapi import FastAPI
from api.UsuarioController import router as usuario_router
from repositorio.contexto.contexto import Base, contexto
import uvicorn

app = FastAPI()

app.include_router(usuario_router)

Base.metadata.create_all(bind=contexto)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)