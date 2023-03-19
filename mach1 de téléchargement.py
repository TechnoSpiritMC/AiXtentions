import requests


url = 'https://gist.githubusercontent.com/TechnoSpiritMC/a54b406837625abac62afee4b108aa18/raw/a70ecd72969dd4b1a149e86175a564da1b50d8e5/gistfile1.txt'
r = requests.get(url, allow_redirects=True)

open('AiScores.aiext', 'wb').write(r.content)
