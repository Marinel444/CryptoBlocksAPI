FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python manage.py migrate && \
    python manage.py loaddata currency_provider_fixtures.json && \
    uvicorn K1core.asgi:app --host 0.0.0.0 --port 8000
