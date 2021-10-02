import requests
from pprint import pprint


def search_hero(hero_name):
    url = f'https://www.superheroapi.com/api.php/2619421814940190/search/{hero_name}'
    resp = requests.get(url).json()
    return resp

def execute_id(json_response):
    data = json_response['results']
    id = []
    for list in data:
        id.append(list['id'])
    
    return id[0]

def execute_intelliigence(hero_id):
    url = f'https://www.superheroapi.com/api.php/2619421814940190/{hero_id}/powerstats'
    resp = requests.get(url).json()
    return resp['intelligence']

def compare_heroes(heroes_names):
    heroes = []
    for hero in heroes_names:
        hero_name = hero
        intellignece = execute_intelliigence(execute_id(search_hero(hero_name)))
        heroes.append({'Hero Name:': hero_name, 'Intelligence': intellignece})
    sorted_list = sorted(heroes, key=lambda k: k['Intelligence'])
    return sorted_list[0]

if __name__ == '__main__':
    #pprint(search_hero('hulk'))
    result = compare_heroes(['Hulk', 'Captain America', 'Thanos'])
    print(f'winnner: {result}')
