'''
json has a following structure:
{"routes":[{"geometry":{"coordinates":[[21.241811,48.732736],[21.241711,48.732702],[21.242864,48.731262],[21.244459,48.73042],[21.245141,48.729731],[21.247171,48.727147],[21.247226,48.726778],[21.249543,48.726391],[21.249784,48.726185],[21.248888,48.722458],[21.249337,48.720926],[21.251147,48.716641],[21.250982,48.71665]],"type":"LineString"},"legs":[{"summary":"","weight":624.9,"duration":613.8,"steps":[],"distance":2105.2}],"weight_name":"cyclability","weight":624.9,"duration":613.8,"distance":2105.2}],"waypoints":[{"distance":0.7619230035968971,"name":"Hroncova","location":[21.241811,48.732736]},{"distance":2.558757519344067,"name":"Štúrova","location":[21.250982,48.71665]}],"code":"Ok","uuid":"ciTPmx7kfKrNQJ3H7ERwuO0unBWJIw5MFNOvzhz1dzgz6xR4rqGCpg=="}
Get coordinates to a dataframe

'''
import json
import pandas as pd
import requests

json_data = "https://api.mapbox.com/directions/v5/mapbox/cycling/21.241816,48.732730;21.250981,48.716627?geometries=geojson&access_token=pk.eyJ1IjoidmxhZHlzbGF2LXJvbWFub3YiLCJhIjoiY2w0dHlsb202MHYzZDNqbnV4dTd0Y21kaCJ9.PonOJfTH4SiS18--xjZclA"
response = requests.get(json_data)
json_response = response.json()
json_response = json_response['routes'][0]['geometry']['coordinates']
df = pd.DataFrame(json_response)
df.columns = ['lon', 'lat']
df.dropna(inplace=True)
df.head()
