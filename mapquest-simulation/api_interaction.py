# Shanaya Ukuwela. ID: 56649043

import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'ueN38bRkDqG2HlHeXB3o1JKGn2wrauaG'

DIRECT_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'
ELEVAT_MAPQUEST_URL = 'http://open.mapquestapi.com/elevation/v1'


def directions_url(location_list: list):
    query_parameters = [
        ('key', MAPQUEST_API_KEY)
    ]
    for location in location_list:
        if location == location_list[0]:
            query_parameters.append(('from', location))
        else:
            query_parameters.append(('to', location))
    return DIRECT_MAPQUEST_URL + '/route?' \
           + urllib.parse.urlencode(query_parameters)

def elevations_url(latLng_str: str):
    query_parameters = [
        ('key', MAPQUEST_API_KEY), ('latLngCollection','')
    ]
    
    return ELEVAT_MAPQUEST_URL + '/profile?' \
           + urllib.parse.urlencode(query_parameters) \
           + latLng_str[:-1]


def get_json(url: str) -> 'json':

    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response!= None:
            response.close()

def get_latLngs(json_result: 'json') -> None:
    '''
    This functions takes the parsed JSON response from the directions url and
    returns the lat and longs in a list
    '''
    latLng_str = ''
    
    for location in json_result['route']['locations']:
        latLng_str += str(location['latLng']['lat'])+','
        latLng_str += str(location['latLng']['lng'])+','

    return latLng_str


       
