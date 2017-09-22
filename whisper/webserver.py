from whisper import secret_helpers
from flask import Flask, request
import json

app = Flask('WHISPER')

@app.route('/<project_name>/<secret_key>', methods = ['GET'])
def get_secret(project_name, secret_key):
    generated_key = secret_helpers.create_secret_key(project_name, secret_key)
    return json.dumps({"value": secret_helpers.get_secret(generated_key)})

@app.route('/<project_name>/<secret_key>', methods = ['POST'])
def set_secret(project_name, secret_key):
    generated_key = secret_helpers.create_secret_key(project_name, secret_key)
    result = secret_helpers.set_secret(generated_key, request.json['value'])

    return json.dumps({"success": result})
