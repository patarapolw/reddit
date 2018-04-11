import requests
import requests.auth

from .const import HEADERS


def access_token(client_id, client_secret, username, password,
                 **kwargs):
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
    }
    r = requests.post('https://www.reddit.com/api/v1/access_token',
                      auth=auth, data=data, headers=HEADERS)

    return r.json()


# def authorize(client_id, redirect_uri,
#               state=str(uuid4()), duration='temporary', scope=('identity', ),
#               **kwarg):
#     params = {
#         'client_id': client_id,
#         'response_type': 'code',
#         'state': state,
#         'redirect_uri': redirect_uri,
#         'duration': duration,
#         'scope': ' '.join(scope)
#     }
#     r = requests.get('https://www.reddit.com/api/v1/authorize', params=params, headers=HEADERS)
#
#     return r.text


if __name__ == '__main__':
    import os, json
    os.chdir('..')

    with open('dev/script.json') as f:
        with open('me/patarapolw.json') as me:
            print(access_token(**json.load(me), **json.load(f)))
