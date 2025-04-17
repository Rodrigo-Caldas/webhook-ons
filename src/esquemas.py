"""Esquema de requisição do webhook."""

from pydantic import BaseModel


class SintegrePayload(BaseModel):
    """
    Estrutura do payload dos dados do Webhook.

    Parameters
    ----------
    DataProduto: str
        A data de referência do produto.

    MacroProcesso: str
        O nome do macroprocesso do produto.

    Nome: str
        O nome do produto.

    Periodicidade: str
        A data inicial de referência do produto.

    PeriodicidadeFinal: str
        A data final de referência do produto.

    Processo: str
        Nome do processo do produto.

    Url: str
        Url para dowload do arquivo.
    """

    dataProduto: str
    macroProcesso: str
    nome: str
    periodicidade: str
    periodicidadeFinal: str
    processo: str
    url: str
