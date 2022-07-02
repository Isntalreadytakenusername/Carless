'''
json has a following structure:
{"routes":[{"geometry":{"coordinates":[[21.243125,48.730963],[21.242998,48.731155],[21.244662,48.730244],[21.247102,48.727243],[21.247254,48.72676],[21.248489,48.726613],[21.251085,48.725974],[21.253288,48.716762],[21.253535,48.716377],[21.256345,48.71611],[21.260967,48.716484],[21.263084,48.717157],[21.262926,48.717359],[21.263619,48.717603]],"type":"LineString"},"legs":[{"summary":"","weight":1033.6,"duration":877.1,"steps":[],"distance":2811.4}],"weight_name":"cyclability","weight":1033.6,"duration":877.1,"distance":2811.4}],"waypoints":[{"distance":1.1705536350145918,"name":"","location":[21.243125,48.730963]},{"distance":29.60905335663898,"name":"","location":[21.263619,48.717603]}],"code":"Ok","uuid":"hgK_qGetwPzAEn9aVUA3HxshsfJ1raqa7ir490ajMeqSl-f_7f207w=="}
Get duration and distance from json as floats

'''
import json
import pandas as pd
import requests

json_data = "https://api.mapbox.com/directions/v5/mapbox/cycling/21.279109,48.743239;21.278919,48.745906?geometries=geojson&access_token=pk.eyJ1IjoidmxhZHlzbGF2LXJvbWFub3YiLCJhIjoiY2w0dHlsb202MHYzZDNqbnV4dTd0Y21kaCJ9.PonOJfTH4SiS18--xjZclA"
response = requests.get(json_data)
json_response = response.json()
duration = json_response['routes'][0]['duration']
distance = json_response['routes'][0]['distance']
print("Duration and distance", duration, distance)