import requests
import json
from pprint import pprint


access_token = 2619421814940190
names_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}


def get_id_by_name(sh_name):
    url = 'https://superheroapi.com/api/' + str(access_token) + '/search/' + sh_name
    r = requests.get(url)
    r_data = r.json()
    return r_data['results'][0]['id']


def get_powerstats(sh_id):
    url = 'https://superheroapi.com/api/' + str(access_token) + '/' + sh_id + '/powerstats'
    r = requests.get(url)
    r_data = r.json()
    return r_data['intelligence']


if __name__ == '__main__':
    pprint(names_dict)
    for name in list(names_dict.keys()):
        names_dict.update({name: get_powerstats(get_id_by_name(name))})

    pprint(names_dict)
