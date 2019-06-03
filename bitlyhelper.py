import urllib
import urllib.parse
import urllib.request
import json

TOKEN = "a7de758bcf390ae75a0bea483f789dda1df32971"
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

class BitlyHelper:

    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            with urllib.request.urlopen(url) as response:
                data = response.read()
                jr = json.loads(data)
                return jr['data']['url']
        except Exception as e:
            print(e)