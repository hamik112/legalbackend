FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt
COPY ./gunicorn_conf.py /gunicorn_conf.py

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY app /app/app
