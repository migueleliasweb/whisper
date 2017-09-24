import credstash
import requests

def create_secret_key(project_name, secret_key):
    return "{}.{}".format(project_name, secret_key)

def get_secret(secret_key):
    try:
        value = credstash.getSecret(secret_key, profile_name='personal')
    except credstash.ItemNotFound as item_not_found:
        value = None

    return value

def set_secret(secret_key, secret_value):
    next_version = credstash.paddedInt(int(credstash.getHighestVersion(
        name=secret_key,
        profile_name='personal'
    )) + 1)

    result = credstash.putSecret(
        name=secret_key,
        secret=secret_value,
        version=next_version,
        profile_name='personal'
    )

    return True if result['ResponseMetadata']['HTTPStatusCode'] < 300 else False
