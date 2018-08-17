import requests
import requests.auth

from .const import HEADERS


def get_token(client_id, client_secret, username, password):
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
    }
    r = requests.post('https://www.reddit.com/api/v1/access_token',
                      auth=auth, data=data, headers=HEADERS)

    return r.json()
