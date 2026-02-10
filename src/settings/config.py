"""Configurações do serviço."""

import asyncio
from pathlib import Path

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """
    Configurações relacionadas ao projeto.

    Parameters
    ----------
    token_ngrok: str
        Token de usuário do Ngrok.
    ngrok_domain: str
        Domínio do Ngrok.
    download_path: Path
        Caminho onde o arquivo será salvo.
    task_limiter : asyncio.Semaphore
        Limitador de tarefas assíncronas.
    """

    token_ngrok: str = "*********"
    ngrok_domain: str = "*********"
    download_path: Path = Path("download")
    task_limiter: asyncio.Semaphore = asyncio.Semaphore(5)


config = Config()
config.download_path.mkdir(parents=True, exist_ok=True)
