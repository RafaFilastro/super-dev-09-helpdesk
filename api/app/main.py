from fastapi import FastAPI

from app.controllers.usuario_controller import router as usuario_router
from app.core.exceptions import registrar_handler

app = FastAPI()

# Traduz as exceções de dominio (app/core/exceptions.py) para respostas HTTP padronizadas
registrar_handler(app)

app.include_router(usuario_router)


# Executar
# uvicorn app.main:app --reload
