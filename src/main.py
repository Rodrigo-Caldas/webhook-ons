from fastapi import FastAPI, Request
from pyngrok import conf, ngrok

from src.config import config
from src.logit import log

app = FastAPI()


@app.on_event("startup")
def iniciar_ngrok():
    conf.get_default().auth_token = config.token_ngrok
    public_url = ngrok.connect(8000)
    log.info(f"Servidor exposto no Ngrok: {public_url}")


@app.post("/webhook")
async def receber_webhook(payload: Request, usuario):
    try:
        body = await payload.body()
        log.warning("Payload recebido bruto:\n%s", body.decode())

    except Exception as erro:
        print(erro)
