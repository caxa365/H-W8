import requests

def get_intelligence(id):
    base_url = 'https://akabab.github.io/superhero-api/api'
    uri = f'/powerstats/{id}.json'
    url = base_url + uri
    response = requests.get(url)
    intelligence = response.json().get('intelligence')
    return intelligence

def result():
    superhero = {}
    superhero['Hulk'] = get_intelligence(332)
    superhero['Captain_America'] = get_intelligence(149)
    superhero['Thanos'] = get_intelligence(655)
    print(max(superhero))
    
result()