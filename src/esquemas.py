"""Esquema de requisição do webhook."""

from pydantic import BaseModel


class SintegrePayload(BaseModel):
    """
    Estrutura do payload dos dados do Webhook.

    Parameters
    ----------
    dataProduto: str
        A data de referência do produto.

    macroProcesso: str
        O nome do macroprocesso do produto.

    nome: str
        O nome do produto.

    periodicidade: str
        A data inicial de referência do produto.

    periodicidadeFinal: str
        A data final de referência do produto.

    processo: str
        Nome do processo do produto.

    url: str
        Url para dowload do arquivo.
    """

    dataProduto: str
    macroProcesso: str
    nome: str
    periodicidade: str
    periodicidadeFinal: str
    processo: str
    url: str
