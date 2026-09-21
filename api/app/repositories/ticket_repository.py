from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.repositories.base import RepositorioBase


class TicketRepository(RepositorioBase[Ticket]):
    def __init__(self, db: Session):
        super().__init__(db, Ticket)

    def obter_ultimo_protocolo(self, prefixo: str) -> str | None:
        statement = (
            select(Ticket.numero_protocolo)
            .where(Ticket.numero_protocolo.like(f"{prefixo}-%"))
            .order_by(Ticket.numero_protocolo.desc())
            .limit(1)
        )

        return self.db.scalar(statement)
