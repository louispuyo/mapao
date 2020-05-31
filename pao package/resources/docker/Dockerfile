FROM python:3.8-slim

COPY . /app
RUN make /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    echo "P.A.O Framework"

EXPOSE 8000
WORKDIR /app

CMD python3.8 /app/app.py \
alembic upgrade head && \
    uvicorn --host=0.0.0.0 app.main:app

