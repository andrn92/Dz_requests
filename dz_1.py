import requests


url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
data_heroes = response.json()
list_heroes = ['Hulk', 'Captain America', 'Thanos']
new_list_heroes = []

for data_hero in data_heroes:
    dict_heroes = {}
    if data_hero['name'] in list_heroes:
        dict_heroes['name'] = data_hero['name']
        dict_heroes['intelligence'] = data_hero['powerstats']['intelligence']
        new_list_heroes.append(dict_heroes)
        
maximum = 0
for data_hero in new_list_heroes:
    if data_hero['intelligence'] > maximum:
        maximum = data_hero['intelligence']
        hero_name = data_hero['name']

print(hero_name)
