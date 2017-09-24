FROM python:3.6-jessie
# using Debian base image just because of limits.h (requirement for uwsgi)

ENV UWSGI_BIND=0.0.0.0:8080

WORKDIR /opt/app
COPY . .

RUN apt-get update -y && apt-get install -y --no-install-recommends gcc python-dev libssl-dev \
    && pip install -r requirements.txt \
    && apt-get remove -y libssl-dev gcc python-dev

CMD ["entrypoint.py"]
