import os
import requests

SERVER_IP = os.getenv('SERVER_IP', 'http://0.0.0.0:8080')

def test_server():
    assert _send_http_request(SERVER_IP) == 201

def _send_http_request(ip: str):
    r = requests.post(f'{ip}/phone_home', json={
        "product": "teamware",
    })
    return r.status_code
