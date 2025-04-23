"""Aplicação webhook."""

import secrets
from datetime import datetime

import requests
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pyngrok import conf, ngrok

from src.config import config
from src.esquemas import SintegrePayload
from src.logit import log

app = FastAPI()
seguranca = HTTPBasic()


def autenticar(credentials: HTTPBasicCredentials = Depends(seguranca)):
    """
    Autentica as credenciais do usuário para acesso do Webhook.

    Parameters
    ----------
    credentials : HTTPBasicCredentials, optional
        credenciais de quem está acessando o webhook, by default Depends(seguranca)

    Raises
    ------
    HTTPException
        Erro de usuário não autorizado.
    """
    if not (
        secrets.compare_digest(credentials.username, config.usuario)
        and secrets.compare_digest(credentials.password, config.senha)
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
        )


@app.on_event("startup")
def iniciar_ngrok():
    """Inicia servidor Ngrok."""
    conf.get_default().auth_token = config.token_ngrok
    public_url = ngrok.connect(addr=8000, domain=config.dominio_ngrok)
    log.info(f"Servidor exposto no Ngrok: {public_url}")


@app.get("/")
def hello_world() -> str:
    """
    Checa se o app está funcionando.

    Returns:
        str: Retorna mensagem de funcionamento do app
    """
    return f"""Aplicação webhook funcionando!!! Olá {config.usuario}!"""


@app.post("/webhook")
async def baixar_arquivo(payload: Request, acesso=Depends(autenticar)):
    """
    Baixa o arquivo através das informações do payload.

    Parameters
    ----------
    payload : Request
        Payload contendo informações do arquivo.
    acesso : None, optional
        verifica se as credenciais são as mesmas, by default Depends(autenticar)
    """
    try:
        dict_payload = await payload.json()
        obj_payload = SintegrePayload(**dict_payload)

        log.info(f"[bright_green]Chegou o arquivo '{obj_payload.nome}'! Baixando..")

        data_obj = datetime.strptime(obj_payload.dataProduto, "%d/%m/%Y")
        resposta = requests.get(url=obj_payload.url)

        with open(
            f"{config.caminho_download}/{obj_payload.nome} - {data_obj.strftime("%d-%m-%Y")}",
            "wb",
        ) as arquivo:
            arquivo.write(resposta.content)

        log.info("[bright_green]Arquivo Baixado!")

    except Exception as erro:
        log.error("[bright_red]Erro ao receber informações do arquivo..")
        raise erro
