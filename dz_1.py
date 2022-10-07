import requests

def get_data_heroes():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    data_heroes = response.json()
    return data_heroes
    
def get_list_heroes(list_heroes):
    data_heroes = get_data_heroes()
    new_list_heroes = []
    for data_hero in data_heroes:
        dict_heroes = {}
        if data_hero['name'] in list_heroes:
            dict_heroes['name'] = data_hero['name']
            dict_heroes['intelligence'] = data_hero['powerstats']['intelligence']
            new_list_heroes.append(dict_heroes)
    return new_list_heroes
            
def get_max_intelligence(list_heroes):
    new_list_heroes = get_list_heroes(list_heroes)
    maximum = 0
    for data_hero in new_list_heroes:
        if data_hero['intelligence'] > maximum:
            maximum = data_hero['intelligence']
            hero_name = data_hero['name']
    return hero_name


list_heroes = ['Hulk', 'Captain America', 'Thanos']
print(get_max_intelligence(list_heroes))

