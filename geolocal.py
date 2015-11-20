from urllib.request import urlopen
from contextlib import closing
from geopy.distance import great_circle
from geopy.distance import vincenty
import json
import sys


# Automatically geolocate the connecting IP
class GeoLocal():
    srv = 'http://freegeoip.net/json/'
    #mapa zawierajaca {ip:km} np {'212.126.9.83': 146.52335238378765}
    mapa = {}
    def __init__(self, list, host):
        hostC = self.locateIp(host)
        current = ''
        try:
            for adr in list:
                current = adr
                adrC = self.locateIp(adr)
                dist = self.distance(adrC, hostC)
                self.mapa[adr] = dist
        except:
            print(sys.exc_info()[0])
            print("bład przy %s") %(current)



    # lokalizuje ip i zwraca wspolrzedne
    def locateIp(self, ip):
        """

        :string ip: Host
        """
        location_latitude = '0.0'
        location_longitude = '0.0'
        url = self.srv + ip
        try:
            with closing(urlopen(url)) as response:
                # location = json.loads(response.read())
                location = json.loads(response.readall().decode('utf-8'))
                #print(location)
                location_city = location['city']
                location_state = location['region_name']
                location_country = location['country_name']
                location_zip = location['zip_code']
                location_latitude = location['latitude']
                location_longitude = location['longitude']
        except:
            print("Location could not be determined automatically")
            print(sys.exc_info()[0])
        return (location_latitude, location_longitude)

    # zwraca dystans miedzy wspolzednymi a i b
    def distance(self, a, b):
        dist = great_circle(a, b).kilometers
        # dist = vincenty(a, b).kilometers
        return dist


    # powinno zwrocic 146.52335238378728 km
    def Test(self):
        myIp = '89.72.127.230'
        dest = '212.126.9.83'
        test = self.distance(self.locateIp(myIp), self.locateIp(dest))
        print(test)
        return (test)
# h = '89.72.127.230'
# a = ['212.126.9.83','212.126.9.83']
# g = GeoLocal(a,h)
# g.Test()
# print(g.mapa)