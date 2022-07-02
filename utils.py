from haversine import haversine
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy import distance

import pandas as pd


def route_to_closest_bike(current_location, bike_list):
    # get the closest bike to the current location
    closest_bike = bike_list[0]
    current_location = (float(current_location.split(',')[0]), float(current_location.split(',')[1]))
    for bike in bike_list:
        bike = (bike[0], bike[1])
        # print("Current loc ", current_location)
        # print("Bike ", bike)
        if haversine(current_location, bike) < haversine(current_location, closest_bike):
            closest_bike = bike
    closest_bike = str(closest_bike[0])+ ',' + str(closest_bike[1])
    return closest_bike

def address_to_coordinates(address):
    location_obj = Nominatim(user_agent='user').geocode(address)
    return f"{location_obj.longitude},{location_obj.latitude}"

