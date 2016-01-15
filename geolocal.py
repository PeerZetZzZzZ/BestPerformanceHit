import json
import sys

import requests
from geopy.distance import great_circle


# Automatically geolocate the connecting IP
class GeoLocal():
    GEOIP_URL = 'https://freegeoip.net/json/'
    #mapa zawierajaca {ip:km} np {'212.126.9.83': 146.52335238378765}

    distance_map = {}
    def __init__(self, list, host):
        hostC = self.locateIp(host)
        current = ''
        try:
            for adr in list:
                current = adr
                adrC = self.locateIp(adr)
                dist = self.distance(adrC, hostC)
                self.distance_map[adr] = dist
        except:
            print(sys.exc_info()[0])
            print("bład przy %s") %(current)



    # lokalizuje ip i zwraca wspolrzedne
    def locateIp(self, domain_name):
        """

        :string ip: Host
        """
        location_latitude = '0.0'
        location_longitude = '0.0'
        url = self.GEOIP_URL + domain_name
        print(url)
        try:
                response = requests.get(url)
                location = json.loads(response.text)
                location_latitude = location['latitude']
                location_longitude = location['longitude']
        except:
            print("Location could not be determined automatically")
            print(sys.exc_info()[0])
        return (location_latitude, location_longitude)

    # zwraca dystans miedzy wspolzednymi a i b
    def distance(self, a, b):
        dist = great_circle(a, b).kilometers
        return dist

    def get_distance_map(self):
        return self.distance_map