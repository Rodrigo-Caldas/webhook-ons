from fastapi import FastAPI
from src.esquemas import SintegrePayload
from pyngrok import ngrok

import logging

app = FastAPI()

# Configura um logger simples para ver os dados recebidos
logging.basicConfig(level=logging.INFO)

public_url = ngrok.connect(8000)
logging.info(f"Servidor exposto no Ngrok: {public_url}")

# Rota para receber o webhook
@app.post("/webhook/rodrigo-caldas")
async def receber_webhook(payload: SintegrePayload):
    logging.info("Produto recebido: %s", payload.Nome)
    logging.info("URL de download: %s", payload.Url)
    logging.info("Payload completo: %s", payload.json(indent=2))

    # Aqui você pode processar o dado ou acionar outro sistema
    print({"status": "recebido", "produto": payload.Nome})
    return {"status": "recebido", "produto": payload.Nome}