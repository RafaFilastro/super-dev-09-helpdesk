"""
Pacote de models. Importar `app.models` registra as tabelas em Base.metadata
oque o Alembic precisa para gerar as migratiions.
"""

from app.core.database import Base
from app.core.enums import Papel
from app.models.categoria import Categoria
from app.models.ticket import Ticket
from app.models.usuario import Usuario

__all__ = ["Base", "Categoria", "Papel", "Ticket", "Usuario"]
