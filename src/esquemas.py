"""Esquema de requisição do webhook."""

from pydantic import BaseModel

class SintegrePayload(BaseModel):
    DataProduto: str
    MacroProcesso: str
    Nome: str
    Periodicidade: str
    PeriodicidadeFinal: str
    Processo: str
    Url: str
