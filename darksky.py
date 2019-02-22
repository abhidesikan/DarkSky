import configparser
import requests

class darksky_auth(object):
    def __init__(self):
        self._config = None

    def get_secret_key(self):
        return self._get_option('SECRET_KEY')

    def _get_option(self, option):
        try:
            return self._get_config().get('DarkSky', option)
        except:
            return None

    def _get_config(self):
        if not self._config:
            self._config = configparser.ConfigParser()
            self._config.read(u'.secrets')
        return self._config

def fetch_forecast(auth, latitude, longitude):
    url = 'https://api.darksky.net/forecast/' + auth.get_secret_key() + '/' + latitude + ',' + longitude
    print url
    r = requests.get(url)
    data = r.json()
    result = data['currently']
    for key,value in result.items():
        print key, value

def run():
    auth = darksky_auth()
    fetch_forecast(auth, '33.873010', '-84.256750')

if __name__ == '__main__':
    run()
