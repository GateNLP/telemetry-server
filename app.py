import json

from datetime import datetime
from flask import request
from flask_api import FlaskAPI, status
from werkzeug.middleware.proxy_fix import ProxyFix

VALID_PRODUCT_NAMES = ['teamware']

app = FlaskAPI(__name__)

# https://flask.palletsprojects.com/en/2.2.x/deploying/proxy_fix/
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.post("/phone_home")
def answer_phone_home():
    payload = request.data
    if valid_payload(payload):
        successful_call(payload)
        return 'Phone home registered', status.HTTP_201_CREATED
    else:
        return 'Invalid phone home', status.HTTP_401_UNAUTHORIZED

def successful_call(payload: dict):
    """ Successful calls are printed to stdout. """
    print(json.dumps({
          '@timestamp': datetime.now().isoformat(),
          payload['product']: payload,
    }))

def valid_payload(payload: dict) -> bool:
    if type(payload) == dict:
        return payload.get('product') in VALID_PRODUCT_NAMES
    else:
        return False
