
#andres owens // 58449528 // project 3 // ics32 // lab 3

import json
import urllib.parse
import urllib.request


mapquest_url_base = 'https://open.mapquestapi.com/directions/v2/route?'
elevation_url_base = 'http://open.mapquestapi.com/elevation/v1/profile?'
mapquest_api_key = 'YE0GHfebc5Tu5YBE8xWZcn0HZKCjW2qN'


def destination_list() -> 'list of destinations':
    '''
    '''
    list_of_dest = []
    dest_count = int(input('Number of locations: '))

    for dest in range(dest_count):
        dest_name = input('location: ')
        list_of_dest.append(('to', dest_name)) 
    return list_of_dest

def build_mapquest_url(list_of_dest: list) -> str:
    '''
    '''
    components = [
    ('key', mapquest_api_key), ('ambiguities', 'ignore'),
    ('from', list_of_dest[0][1])] + list_of_dest[1:]
    #('callback', 'renderNarrative')]
    
    return mapquest_url_base + urllib.parse.urlencode(components)

def build_elevation_url(list_of_latlng: list) -> str:
    '''
    '''
    components = [('key', mapquest_api_key),
                  ('inFormat', 'kvp'),
                  ('shapeFormat', 'raw'),
                  ('width', 425),
                  ('height', 350),
                  ('latLngCollection', str(list_of_latlng)[1:-1].replace(' ', '')),
                  ('unit', 'f')]

    return elevation_url_base + urllib.parse.urlencode(components)

def create_json_object(url: str) -> 'json':
    '''
    '''
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        json_object = json.loads(json_text)
        
        return json_object

    except:
        print('MAPQUEST ERROR')
        return None
    
    finally:
        if response != None:
            response.close()


def STEPS(json_object: 'json object') -> str:
    '''
    '''
    print('DIRECTIONS')
    for legs in json_object['route']['legs']:
        for manu in legs['maneuvers']:
            print(manu['narrative'])
        print()

def LATLNG(json_object: 'json object') -> str:
    '''
    '''
    print('\nLATLONGS')    
    list_of_latlng = []
    for info in json_object['route']['locations']:
        list_of_latlng.append(info['latLng']['lat'])
        list_of_latlng.append(info['latLng']['lng'])
        print("{:.2f}".format(info['latLng']['lat']),
            "{:.2f}".format(info['latLng']['lng']))
    print()
    return list_of_latlng

def TIME_DISTANCE(json_object: 'json object') -> str:
    '''
    '''
    print("TOTAL TIME:", "{:.0f}".format(
        int(json_object['route']['time'])/60), 'minutes \n')
    print("TOTAL DISTANCE:","{:.0f}".format(
        json_object['route']['distance']), 'miles \n')

def ELEVATION(json_object: 'json object') -> str:
    '''
    '''
    print('ELEVATIONS')
    for item in json_object['elevationProfile']:
        print("{:.0f}".format(item['height']))



if __name__ == '__main__':
    mapquest_url = build_mapquest_url(destination_list())
    #print('\n', mapquest_url, '\n')
    MQ_OBJ = create_json_object(mapquest_url)

    if MQ_OBJ != None:
        if MQ_OBJ['info']['statuscode'] == 0:
            latlong = LATLNG(MQ_OBJ)
            distance = TIME_DISTANCE(MQ_OBJ)
            directions = STEPS(MQ_OBJ)
            elevation_url = build_elevation_url(latlong)
            #print('\n', elevation_url, '\n')
            EV_OBJ = create_json_object(elevation_url)
            elevation = ELEVATION(EV_OBJ)
        else:
            print('\nNO ROUTE FOUND')
        

    


