import requests
import json

from .const import HEADERS


class Reddit:
    def __init__(self, token_file):
        with open(token_file) as f:
            self.token = json.load(f)['access_token']

    def get(self, url, params: dict=None):
        if params is None:
            params = dict()
        r = requests.get('https://oauth.reddit.com/{}'.format(url), headers=self.get_headers(), params=params)
        return r.json()

    def post(self, url, params: dict=None):
        if params is None:
            params = dict()
        r = requests.post('https://oauth.reddit.com/{}'.format(url), headers=self.get_headers(), json=params)
        return r.json()

    def get_headers(self):
        return {
            'Authorization': 'bearer {}'.format(self.token),
            **HEADERS
        }
