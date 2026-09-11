from enum import Enum


class Papel(str,Enum):
    ADMIN = "ADMIN"
    ATENDENTE = "ATENDENTE"
    SOLICITANTE = "SOLICITANTE"

class StatusChamado(str, Enum):
    ABERTO = "ABERTO"
    EM_ANALISE = "EM_ANALISE"
    EM_ATENDIMENTO = "EM_ATENDIMENTO"
    RESOLVIDO = "RESOLVIDO"
    FECHADO = "FECHADO"
    CANCELADO = "CANCELADO"


class PrioridadeChamdo(str, Enum):
    BAIXA = "BAIXA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"

