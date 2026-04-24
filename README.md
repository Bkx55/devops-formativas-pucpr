# Projeto DevOps Formativas (PUCPR)

Projeto simples para cumprir as Formativas 1 e 2 e a atividade de Docker.

## Executar local

```bash
pip install -r requirements.txt
python app.py
```

## Testes

```bash
pytest -q
```

## Alertas (GitHub Actions)

Configure o secret `ALERT_WEBHOOK_URL` no repositorio para enviar alertas
para Discord, Slack, Teams ou Telegram via webhook.

## Docker

```bash
docker build -t devops-formativas .
docker run -d --name devops-app -p 5000:5000 devops-formativas
docker ps
```
