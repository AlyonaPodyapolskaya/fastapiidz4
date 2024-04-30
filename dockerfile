FROM python:3.11.0
RUN mkdir /fastapi_app
WORKDIR /fastapi_app
COPY requiremenets.txt .
RUN pip install -r requiremenets.txt
COPY . .
RUN python -c "import sqlalchemy; engine = sqlalchemy.create_engine('postgres://idz4_user:OfT6CwiOYetY9o8YrhSLJY9kjVgOaUxq@dpg-coobeo8l5elc739lhkh0-a.singapore-postgres.render.com/idz4'); engine.connect()" || true
RUN alembic upgrade head
CMD gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8001
