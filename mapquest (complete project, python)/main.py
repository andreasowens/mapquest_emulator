#andres owens // 58449528 // project 3 // ics32 // lab 3

import classes
import functions

if __name__ == '__main__':
    mapquest_url = functions.build_mapquest_url(functions.destination_list())
    MQ_OBJ = functions.create_json_object(mapquest_url)

    if MQ_OBJ != None:
        if MQ_OBJ['info']['statuscode'] == 0:
            latlong = functions.LATLNG(MQ_OBJ)
            distance = functions.TIME_DISTANCE(MQ_OBJ)
            directions = functions.STEPS(MQ_OBJ)
            l1, l2 = LATLNG(MQ_OBJ)
            for item in l1:
                elevation_url = functions.build_elevation_url(item)
                EV_OBJ = functions.create_json_object(elevation_url)
                elevation = functions.ELEVATION(EV_OBJ)
        else:
            print('\nNO ROUTE FOUND')
        
