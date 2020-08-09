#andres owens // 58449528 // project 3 // ics32 // lab 3

class DistanceTotal:
    def __init__(self, MQ_OBJ):
        '''
        '''
    pass


class TimeTotal:
    pass

class Elevation:
    def __init__(self):

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


    
    pass

class Directions:
    pass
