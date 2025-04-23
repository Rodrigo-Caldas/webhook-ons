FROM python:3.13-slim

WORKDIR /home

COPY src src
COPY requirements.txt .

VOLUME ["/home/download"]

RUN python -m venv webhook-ons
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]