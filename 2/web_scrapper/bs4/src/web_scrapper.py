import requests
from bs4 import BeautifulSoup

base_url = 'https://yasdl.com'
header = {
    "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36As:"
}

r = requests.get(base_url,header)


final = BeautifulSoup(r.content,"lxml")

print(final)