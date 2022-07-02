import streamlit as st
import pandas as pd
import numpy as np
from api_request import get_route
from utils import route_to_closest_bike

from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from utils import address_to_coordinates


## user location

loc_button = Button(label="Get Location")
loc_button.js_on_event("button_click", CustomJS(code="""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
        }
    )
    """))
user_location = streamlit_bokeh_events(
    loc_button,
    events="GET_LOCATION",
    key="get_location",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if user_location:
    if "GET_LOCATION" in user_location:
        # st.write(user_location.get("GET_LOCATION"))
        print("Real location ", user_location.get("GET_LOCATION"))
        print('Real location type ', type(user_location.get("GET_LOCATION")))
        my_location_dict = user_location.get("GET_LOCATION")
        my_location = str(my_location_dict['lon']) + ',' + str(my_location_dict['lat'])
    else:
        st.write("Sorry, we didn't get your location")
        my_location = '21.279109,48.743239'   # (lon, lat) is used by mapbox API
else:
    st.write("Sorry, we didn't get your location")
    my_location = '21.279109,48.743239'  # (lon, lat) is used by mapbox API

# temporary location 48.743239, 21.279109 actual my_location = '21.242385,48.732033'
url = 'https://gbfs.sharing.antik.sk/v2/antiksharing_ke/en/free_bike_status.json'

# read json from url as a dataframe
df = pd.read_json(url)
df = df['data']['bikes']
df = pd.DataFrame(df)
df = df[df['lat'] != 0]

st.markdown('## This is a map of shared vehicles in Kosice 📍')

destination = address_to_coordinates(st.text_input('Enter the destination', value='Letna 9, Kosice'))


types = ["bicycle", "e-bicycle", "scooter", "moped", "all vechiles"]
selected_item = st.selectbox('Select a type', types)


# st.map(df[df['vehicle_type_id'] == str((types.index(selected_item) + 1))])
#
# st.write(df[df['vehicle_type_id'] == str((types.index(selected_item) + 1))])

## make the same map with pydeck
import pydeck as pdk

if selected_item != 'all vechiles':
    df_map = df[df['vehicle_type_id'] == str((types.index(selected_item) + 1))]
else:
    df_map = df

df_map = df_map[['lat', 'lon', 'bike_id']]
df_map.dropna(inplace=True)
# st.write(df_map)
bikes_layer = pdk.Layer('ScatterplotLayer', data=df_map, get_position=['lon', 'lat'], get_radius=30, pickable=True, opacity=0.5, stroke_width=0.5, get_fill_color=[119, 107, 255, 140])
# layer = pdk.Layer('LineLayer', data=get_route('cycling', '21.241816,48.732730', '21.250981,48.716627'), get_position=['lon', 'lat'], get_color=[119, 107, 255, 140], pickable=True, opacity=0.5, stroke_width=0.5)

## take lon lat from df_map and make list of lists
lon_lat = df_map[['lon', 'lat']].values.tolist()

print("Route to closest bike: ", route_to_closest_bike(my_location, lon_lat))
print("My location: ", my_location)

route_to_bike = get_route('cycling', my_location, route_to_closest_bike(my_location, lon_lat))
route_from_bike_to_dest = get_route('cycling', route_to_closest_bike(my_location, lon_lat), destination)
route_to_bike_layer = pdk.Layer(
    type="PathLayer",
    data= route_to_bike,
    pickable=True,
    get_color="color",
    width_scale=5,
    width_min_pixels=2,
    get_path="path",
    get_width=3,
)

route_from_bike_to_dest_layer = pdk.Layer(
    type="PathLayer",
    data= route_from_bike_to_dest,
    pickable=True,
    get_color="color",
    width_scale=5,
    width_min_pixels=2,
    get_path="path",
    get_width=3,
)


#
#




init_view_state = pdk.ViewState(latitude=48.717299, longitude=21.254107, zoom=12, max_zoom=15)
r = pdk.Deck(layers = [bikes_layer, route_to_bike_layer, route_from_bike_to_dest_layer], initial_view_state=init_view_state, map_style='mapbox://styles/mapbox/light-v10')
st.pydeck_chart(r)


