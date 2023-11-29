# -*- coding: utf-8 -*-

class Location:
    '''
    En enkel klass för att beskriva en plats
    '''

    def __init__(self, name: str = "", lat: float = 0, lon: float = 0):
        self.name = name
        self.lat = lat
        self.lon = lon
