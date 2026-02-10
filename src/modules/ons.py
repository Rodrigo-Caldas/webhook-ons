"""Módulo para lidar com os produtos que chegam do webhook."""

from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

import httpx
from fastapi import Request
from loguru import logger

from src.modules.utils import normalize
from src.schemas import ons as schemas
from src.settings.config import config


async def download_archive(request: schemas.RequestWebhook) -> Path:
    """
    Realiza o download do arquivo através da url.

    Parameters
    ----------
    request : RequestWebhook
        Estrutura bruta dos dados vindos do Webhook.

    Returns
    -------
    Path
        Caminho do arquivo webhook localmente.

    Raises
    ------
    erro
        Erro levantado.
    """
    try:
        async with config.task_limiter:
            async with httpx.AsyncClient() as cliente:
                answer = await cliente.get(request["url"], timeout=60)

                cd = answer.headers.get("Content-Disposition")

                if cd and "filename=" in cd:
                    filename = cd.split("filename=")[-1].strip('"; ')
                    filename = unquote(filename)
                    filename = filename.lower()

                else:
                    filename = Path(request["name"])

                save_path: Path = Path(config.download_path) / filename

                with open(
                    f"{save_path}",
                    "wb",
                ) as arquivo:
                    arquivo.write(answer.content)

                logger.success(f"Arquivo '{save_path}' baixado!")

                return save_path

    except Exception as erro:
        logger.error("Erro ao baixar arquivo!")
        raise erro


async def receive_webhook(
    request_webhook: Request,
) -> None:
    """
    Executa o pipeline do Webhook de forma assíncrona.

    1º) recebe informações do webhook (S0),
    2º) faz o download do arquivo (S1),
    3º) organiza o documento que será registrado no BD (S2),
    4º) registra informações do arquivo no BD (S3).

    Parameters
    ----------
    request_webhook : schemas.RequestWebhook
        Objeto request contendo informações do arquivo.

    Raises
    ------
    error
        Erro levantado caso ocorra.
    """
    logger.info(f"Etapa S0: chegou arquivo do webhook!")

    received_time = datetime.now()
    raw_request = await request_webhook.json()

    try:
        request_object = schemas.RequestWebhook(
            process=raw_request["processo"],
            macro_process=raw_request["macroProcesso"],
            product_date=raw_request["dataProduto"],
            url=raw_request["url"],
            name=raw_request["nome"],
            periodicity=raw_request["periodicidade"],
            final_periodicity=raw_request["periodicidadeFinal"],
            received_time=received_time,
        )

    except ValueError as error:
        logger.error("Erro no payload!")
        raise ValueError(f"Campo inválido no payload do Webhook -> {error}")

    logger.success(
        f"Chegou o arquivo '{request_object['name']} "
        f"de {request_object['product_date']}'!"
    )

    logger.info(f"Etapa S1: Baixando arquivo '{request_object['name']}'..")
    local_path = await download_archive(request=request_object)

    logger.info(
        "Etapa S2: Organizando documento para ser registrado no Banco de Dados.."
    )

    std_name = normalize(string=request_object["name"])

    try:

        webhook_db = schemas.WebhookDB(
            process=request_object["process"],
            macro_process=request_object["macro_process"],
            product_date=datetime.strptime(request_object["product_date"], "%d/%m/%Y"),
            url=request_object["url"],
            name=request_object["name"],
            std_name=std_name,
            download_name=local_path.name,
            extension=local_path.suffix,
            local_path=str(local_path),
            periodicity=datetime.fromisoformat(request_object["periodicity"]),
            final_periodicity=datetime.fromisoformat(
                request_object["final_periodicity"]
            ),
            received_time=request_object["received_time"],
        )
    except ValueError as error:
        logger.error("Erro no payload!")
        local_path.unlink()
        raise ValueError(f"Campo inválido no payload do Webhook -> {error}") from error

    logger.success("Fim do pipeline!")
