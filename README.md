# webhook-ons

![texto](https://img.shields.io/static/v1?label=3.13&message=python&color=green&style=flat-square "3.13")
![texto](https://img.shields.io/static/v1?label=ambiente&message=docker&color=blue&style=flat-square "ambiente")

## :world_map: Conteúdo
1. [O que o serviço faz?](#sparkles-O-que-o-serviço-faz)  
2. [Quais tecnologias posso usar?](#warning-Quais-tecnologias-posso-usar) 
3. [Como utilizar o serviço?](#pencil-Como-utilizar-o-serviço)

## :scroll: O que o serviço faz?

Repositório com o webhook do Sintegre configurado, faz o download dos arquivos que o Sintegre disponibiliza. Esse serviço optou por utilizar o Ngrok (ferramenta que te permite criar um túnel seguro, atrás de NATs e Firewalls, que expõem serviços locais para a Internet), fazendo com que o usuário não precise expor uma porta do computador de forma manual.

Para criar sua conta ngrok gratuitamente visite: https://ngrok.com

## :warning: Quais tecnologias posso usar?

Há duas maneiras de executar este repositório, utilizando Python ou Docker.

- [Python](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)
- [Docker](https://docs.docker.com/engine/install/)

## :pencil: Como utilizar o serviço?

Execute o comando abaixo para clonar o repositório:

```bash  
git clone https://github.com/Rodrigo-Caldas/webhook-ons.git
```

Para o webhook ter mais segurança, o serviço foi pensado para ter autenticação por usuário e senha. Não é obrigatório, mas segue uma boa prática de segurança para evitar qualquer tipo de invasão.

No arquivo ``config.py`` altere as 4 variáveis de configuração específicadas aqui no ``readme``. As variáveis ``usuario`` e ``senha`` não são obrigatórias, mas são recomendadas como já explicado anteriormente:

```bash
usuario: str = "usuario-webhook"
senha: str = "senha-do-webhook"
token_ngrok: str = "token-do-usuário-ngrok"
dominio_ngrok: str = "domínio-da-aplicação-ngrok.app"
```

É possível rodar a aplicação de duas formas: através da criação de ambiente python :snake: ou utilizando docker :whale:

### :snake: Via ``Python``

Crie um ambiente com o python 3.13 a partir do comando:

```bash 
python -m venv webhook-ons
```

Ative o ambiente a partir do comando:

```bash 
source webhook-ons/bin/activate
```

Instale as bibliotecas com:

```bash 
pip install -r requirements.txt
```

E por fim rode a aplicação com:

```bash
uvicorn src.main:app --reload
```

### :whale: Via ``Docker``

Para rodar a aplicação em um container, construa a imagem da aplicação a partir do comando:

```bash
docker build . -t webhook-ons
```

Com a imagem construída podemos criar o container onde a aplicação será rodada, mas antes verifique o caminho da pasta ``download`` presente neste repositório. Ela será necessária para criarmos um volume que a ligará com a pasta ``download`` presente no container.

Após verificar o caminho, insira o caminho dela no comando de criação do container:

```bash
docker run -v /caminho/da/pasta/download/local:/home/download -t webhook-ons:latest
```