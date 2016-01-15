from urllib.parse import urlparse

import requests

from geolocal import GeoLocal
from models import FileProvider

class DistanceCounter:

    def find_winner(self, received_urls):
        investigated_file_domains = self.get_investigated_file_domains()
        for received_url in received_urls:
            received_url_domain = self.get_domain_name_from_url(received_url)
            geo_local = GeoLocal(investigated_file_domains, received_url_domain)
            distance_map = geo_local.get_distance_map() # its investigated_file_domain : km frm recieved url
            print("mam distance map")
            print(distance_map)

    def get_investigated_file_domains(self):
        filedomains = []
        file_providers = FileProvider.objects
        for file_provider in file_providers:
            filepath = file_provider.filepath
            domain_name = self.get_domain_name_from_url(filepath)
            filedomains.append(domain_name)
        return filedomains

    def get_domain_name_from_url(self, url):
        parsed_uri = urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        if domain.startswith('www.'):
            domain = domain[4:] # cut this www. out

        print("Domain name after parsing: " + domain)
        return domain

    def get_my_ip(self):
        request = requests.get('https://api.ipify.org')
        print(request.text)
        return request.text