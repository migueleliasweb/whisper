FROM python:3.6-jessie
# just because of limits.h (requirement for uwsgi)

WORKDIR /opt/app
COPY . .

RUN apt-get update -y && apt-get install -y --no-install-recommends gcc python-dev libssl-dev \
    && pip install -r requirements.txt \
    && pip install uwsgi==2.0.15 \
    && apt-get remove -y libssl-dev gcc python-dev

CMD ["/usr/local/bin/uwsgi", "--master", "--threads", "4", "--processes", "2", "--http", "0.0.0.0:80", "--module", "whisper.webserver", "--callable", "app"]
