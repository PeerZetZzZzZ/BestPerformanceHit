class DistanceKeeper:
    url = ''
    domain_name = ''
    latitude = 0.0
    longitude = 0.0

    def set_url(self, url):
        self.url = url

    def set_domain_name(self, domain_name):
        self.domain_name = domain_name

    def set_geolocation(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude