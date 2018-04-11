import requests
import json

from .auth import access_token
from .const import HEADERS


def get(url, token, params=None):
    if params is None:
        params = dict()

    headers = {
        'Authorization': 'bearer {}'.format(token),
        **HEADERS
    }
    r = requests.get('https://oauth.reddit.com{}'.format(url), headers=headers, params=params)

    return r.json()


class Reddit:
    def __init__(self, username=None, password=None, client_id=None, client_secret=None,
                 **kwargs):
        if username is None:
            with open('dev/script.json') as f:
                with open('me/patarapolw.json') as me:
                    self.token = access_token(**json.load(me), **json.load(f))['access_token']
        else:
            self.token = access_token(client_id, client_secret, username, password)['access_token']

    def get(self, url, params: dict=None):
        return get(url, self.token, params)


if __name__ == '__main__':
    print(get('/r/ChineseLanguage/hot', '71403897348--6bDtSmaQ3B_JxncIlB-uaKCsNM'))
