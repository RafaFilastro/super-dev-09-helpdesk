from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.usuario_shcema import UsuarioCriar
from app.services.usuario_service import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def criar(
    dado: UsuarioCriar,
    db: Annotated[Session, Depends(get_db)],
):
    return UsuarioService(db).criar(dado)
