# Whisper a.k.a [Credstash](https://github.com/fugue/credstash)'s API
Since you are going to tell a secret, at least whisper it.

![alt text](https://github.com/migueleliasweb/whisper/blob/master/whisper.jpg "Best logo evar!!!")

## Configuration - Environment variables

* AWS_ACCESS_KEY_ID  - AWS access key to be used to accessing the API
* AWS_SECRET_ACCESS_KEY - AWS secret to be used to accessing the API
* AWS_PROFILE [Optional] - AWS profile to used then accessing the API (usefull for local testing)
* UWSGI_BIND - [Default: "0.0.0.0:8080"] Address for UWSGI to bind to
* UWSGI_PROCESSES - [Default: 2] Number of processes to use when starting UWSGI
* UWSGI_THREADS - [Default 4] Number of threads to use then starting UWSGI

## About

Whisper implements a HTTP wrapper around the [credstash](https://github.com/fugue/credstash) calls. The API is basically the same as used in the original CLI implementation. The only major difference is that the Whisper API forces namespacing the keys with a "project_name". For more information see examples.

Some caveats:

* The `Content-Type: application/json` is required in all calls
* The "project_name" is required in all calls

### Running inside Docker(official image) - *SIMPLE*

```bash
$ docker build docker/Dockerfile -t whisper .
$ docker run -it --rm -e AWS_ACCESS_KEY_ID=YOURKEY -e AWS_SECRET_ACCESS_KEY=YOURSECRET whisper
```

### Running inside Docker(official image) - *HEAVY LOAD*

Usually you won't need to increase the number of processes/threads used by the API, but
if you find yourself in a very busy environment, feel free to increase the total number
of threads and processes used by UWSGI.

```bash
$ docker build docker/Dockerfile -t whisper .
$ docker run -it --rm \
-e UWSGI_PROCESSES=4 \
-e UWSGI_THREADS=32 \
-e AWS_ACCESS_KEY_ID=YOURKEY \
-e AWS_SECRET_ACCESS_KEY=YOURSECRET whisper
```

### Running inside Docker (official image)

```bash
$ docker build docker/Dockerfile -t whisper .
$ docker run -it --rm \
-e AWS_ACCESS_KEY_ID=YOURKEY \
-e AWS_SECRET_ACCESS_KEY=YOURSECRET whisper
```

### Running locally - TEST (python >=3)

```bash
# You can what profile will be used by Boto by setting ${AWS_PROFILE}="your_profile"
$ pip install -r requirements-dev.text
$ ./entrypoint.py
```

## Examples

### SET SECRET

#### Whisper call
```bash
$ curl -H "Content-Type: application/json" -X POST -d '{"value": "THISISMYVALUE"}' http://${WHISPER_URL}/MY_PROJECT_NAME/MY_KEY
{"success": true}
```

#### Credstash correspondent call
```bash
$ credstash put "MY_PROJECT_NAME.MY_KEY" "THISISMYVALUE"
```

### GET SECRET

#### Whisper call - JSON format
```bash
$ curl -H "Content-Type: application/json" http://${WHISPER_URL}/MY_PROJECT_NAME/MY_KEY
{"value": "foo"}
```

#### Whisper call - PLAIN format (usefull to integrate with bash scripts)
```bash
$ curl -H "Content-Type: application/json" http://${WHISPER_URL}/MY_PROJECT_NAME/MY_KEY?format=plain
foo
```

#### Credstash correspondent call
```bash
$ credstash get "MY_PROJECT_NAME.MY_KEY"
```
