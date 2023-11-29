# -*- coding: utf-8 -*-

from .Location import Location
import json


class Unicorn:
    '''
    En enkel klass för att representera en enhörning
    '''

    def __init__(
        self,
        id: int = 0,
        name: str = "",
        description: str = "",
        reported_by: str = "",
        spotted_where: Location = Location(),
        spotted_when: int = 0,
        image: str = "",
    ) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.reported_by = reported_by
        self.spotted_where = spotted_where
        self.spotted_when = spotted_when
        self.image = image

    def from_db(self, data) -> None:
        '''
        Populerar en enhörning med data från en databasförfrågan.
        '''

        self.id = data[0]
        self.name = data[1]
        self.description = data[2]
        self.reported_by = data[3]
        self.spotted_where = Location(
            name=data[4],
            lat=data[5],
            lon=data[6]
        )
        self.spotted_when = data[7]
        self.image = data[8]

    def to_dict(self) -> dict:
        '''
        Skapar en dictionary med värden från denna enhörning. Bra att använda
        när man matar in enhörningar i databaser.
        '''

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'reportedBy': self.reported_by,
            'spottedWhereName': self.spotted_where.name,
            'spottedWhereLat': self.spotted_where.lat,
            'spottedWhereLon': self.spotted_where.lon,
            'spottedWhen': self.spotted_when,
            'image': self.image
        }
