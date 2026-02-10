"""Aplicação webhook."""

from fastapi import FastAPI, Request
from loguru import logger
from pyngrok import conf, ngrok

from src.modules import ons
from src.settings.config import config

app = FastAPI()


@app.on_event("startup")
def iniciar_ngrok():
    """Inicia servidor Ngrok."""
    conf.get_default().auth_token = config.token_ngrok
    public_url = ngrok.connect(addr=8000, domain=config.ngrok_domain)
    logger.info(f"Servidor exposto no Ngrok: {public_url}")


@app.get("/")
def hello_world() -> str:
    """
    Checa se o app está funcionando.

    Returns:
        str: Retorna mensagem de funcionamento do app
    """
    return f"""Aplicação webhook funcionando!!!"""


@app.post("/listener")
async def receive_webhook(payload: Request):
    """
    Recebe e executa o pipeline do Webhook de forma assíncrona.

    Parameters
    ----------
    payload : Request
        Payload contendo informações do arquivo.
    """
    await ons.receive_webhook(request_webhook=payload)
