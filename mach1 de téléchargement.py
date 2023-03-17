import requests


url = 'truc'
r = requests.get(url, allow_redirects=True)

open('facebook.txt', 'wb').write(r.content)
