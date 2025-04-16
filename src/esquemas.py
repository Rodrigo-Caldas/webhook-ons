"""Esquema de requisição do webhook."""

from typing import TypedDict


class SintegrePayload(TypedDict):
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

    DataProduto: str
    MacroProcesso: str
    Nome: str
    Periodicidade: str
    PeriodicidadeFinal: str
    Processo: str
    Url: str
