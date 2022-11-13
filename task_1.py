import requests

def read_json(url, heroes):
    heroes_iq = {}
    iq_list = []
    json_file = requests.get(url).json()
    for i in json_file:
        hero = i['name']
        if hero in heroes:
            hero_iq = i['powerstats']['intelligence']
            heroes_iq[hero_iq] = hero
            iq_list.append(hero_iq)
    iq_best = max(iq_list)
    print(heroes_iq[iq_best], 'have a top IQ -', iq_best)
    
read_json('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json',
          ['Hulk', 'Captain America', 'Thanos'])
