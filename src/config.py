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
    caminho_download: Path
        Caminho onde o arquivo será salvo.
    """

    usuario: str = "rodrigo_caldas"
    senha: str = "@NS12345"
    token_ngrok: str = "2vkEqj8FJVHt4pGBVacbjOL5vBy_nTQusCD3mnPRxyyEN4Ji"
    dominio_ngrok: str = "totally-eager-cardinal.ngrok-free.app"
    caminho_download: Path = Path("download")


config = Configuracoes()
config.caminho_download.mkdir(parents=True, exist_ok=True)
