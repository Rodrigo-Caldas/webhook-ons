"""Configurações do serviço."""

from pathlib import Path

from pydantic_settings import BaseSettings


class Configuracoes(BaseSettings):
    """
    Configurações relacionadas ao projeto.

    Parameters
    ----------
    usario: str
        Usuário do Webhook.
    senha: str
        Senha do Webhook.
    token_ngrok: str
        Token de usuário do ngrok.
    """

    usuario: str = "usuario-webhook"
    senha: str = "senha-webhook"
    token_ngrok: str = "token-ngrok"
    dominio_ngrok: str = "dominio-ngrok-do-usuario"
    caminho_download: Path = Path("download")


config = Configuracoes()
config.caminho_download.mkdir(parents=True, exist_ok=True)
