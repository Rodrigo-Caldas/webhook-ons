"""Configurações do serviço."""

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


config = Configuracoes()
