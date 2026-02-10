"""Modelos e tipos gerais do Webhook."""

from datetime import datetime
from pathlib import Path
from typing import TypedDict


class RequestWebhook(TypedDict):
    """
    Estrutura bruta dos dados vindos do Webhook.

    Attributes
    ----------
    product_date: str
        Data do produto.
    macro_process: str
        Macro processo.
    name: str
        Nome do arquivo.
    periodicity: str
        Periodicidade do arquivo.
    final_periodicity: str
        Periodicidade final.
    received_time: datetime
        Data/hora de quando o arquivo foi recebido.
    process: str
        Processo que ele pertence
    url: str
        Url de download.
    """

    product_date: str
    macro_process: str
    name: str
    periodicity: str
    final_periodicity: str
    received_time: datetime
    process: str
    url: str


class WebhookDB(TypedDict):
    """
    Estrutura dos dados Webhook para serem inseridos no BD.

    Attributes
    ----------
    product_date: datetime
        Data do produto.
    macro_process: str
        Macro processo.
    name: str
        Nome do arquivo vindo do webhook.
    std_name: str
        Nome do arquivo vindo do webhook normalizado.
    download_name: str
        Nome do arquivo quando é baixado.
    extension: str
        Extensão do arquivo.
    local_path: Path
        Caminho do arquivo salvo no localmente.
    periodicity: datetime
        Periodicidade do arquivo.
    final_periodicity: datetime
        Periodicidade final.
    received_time: datetime
        Data/hora de quando o arquivo foi recebido.
    process: str
        Processo que ele pertence
    url: str
        Url de download.
    """

    product_date: datetime
    macro_process: str
    name: str
    std_name: str
    download_name: str
    extension: str
    local_path: str
    periodicity: datetime
    final_periodicity: datetime
    received_time: datetime
    process: str
    url: str
