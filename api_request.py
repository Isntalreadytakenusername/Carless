import pandas as pd
import requests
#this function uses Mapbox API to get route between two points
def get_route(transport_type, starting_coordinates, destination_coordinates):
    json_data = 'https://api.mapbox.com/directions/v5/mapbox/' + transport_type + '/' + starting_coordinates + ';' + destination_coordinates + '?geometries=geojson&access_token=pk.eyJ1IjoidmxhZHlzbGF2LXJvbWFub3YiLCJhIjoiY2w0dHlsb202MHYzZDNqbnV4dTd0Y21kaCJ9.PonOJfTH4SiS18--xjZclA'
    print(json_data)

    response = requests.get(json_data)
    json_response = response.json()
    coordinates = json_response['routes'][0]['geometry']['coordinates']
    duration = json_response['routes'][0]['duration']
    distance = json_response['routes'][0]['distance']
    df = pd.DataFrame(coordinates)
    df.columns = ['lon', 'lat']
    df.dropna(inplace=True)
    # get lon and lat in a list of lists
    lon_lat = df.values.tolist()
    # dict_res = {'path': lon_lat}
    df_route = pd.DataFrame({'name': ['path1', 'empty'], 'path': [lon_lat, [[]]], 'color': [(255, 0, 0),(255, 0, 0)]})
    return df_route, duration, distance


