# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import pandas as pd
import numpy as np


url = 'https://gbfs.sharing.antik.sk/v2/antiksharing_ke/en/free_bike_status.json'

# read json from url as a dataframe
df = pd.read_json(url)
df = df['data']['bikes']
df = pd.DataFrame(df)
df = df[df['lat'] != 0]

st.markdown('## This is a map of shared vehicles in Kosice 📍')

types = ["bicycle", "e-bicycle", "scooter", "moped"]
selected_item = st.selectbox('Select a type', types)


st.map(df[df['vehicle_type_id'] == str((types.index(selected_item) + 1))])

st.write(df[df['vehicle_type_id'] == str((types.index(selected_item) + 1))])

## make the same map with pydeck
import pydeck as pdk

df_map = df[df['vehicle_type_id'] == str((types.index(selected_item) + 1))]
df_map = df_map[['lat', 'lon', 'bike_id']]
df_map.dropna(inplace=True)
st.write(df_map)
layer = pdk.Layer('ScatterplotLayer', data=df_map, get_position=['lon', 'lat'], get_radius=30, pickable=True, opacity=0.5, stroke_width=0.5, get_fill_color=[119, 107, 255, 140])
init_view_state = pdk.ViewState(latitude=48.717299, longitude=21.254107, zoom=12, max_zoom=15)
r = pdk.Deck(layers = [layer], initial_view_state=init_view_state, tooltip={"html": f"<b>Bike ID:</b> {df_map['bike_id']}"}, map_style='mapbox://styles/mapbox/light-v10')
st.pydeck_chart(r)
