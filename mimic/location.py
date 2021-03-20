import random
from collections import namedtuple

LatLong = namedtuple('LatLong', {'lat', 'long'})


class Location:
    _continents = [('Africa', 'AF'),
                   ('Asia', 'AS'),
                   ('Europe', 'EU'),
                   ('North America', 'NA'),
                   ('South America', 'SA'),
                   ('Australia', 'AU')]

    @classmethod
    def continent(cls, short=False):
        ix = random.randint(0, len(cls._continents) - 1)
        name_ix = 1 if short else 0
        return cls._continents[ix][name_ix]

    @classmethod
    def country(cls, continent=None):
        return None

    @classmethod
    def capital(cls, continent=None, country=None):
        return None

    @classmethod
    def city(cls, continent=None, country=None):
        return None

    @classmethod
    def timezone(cls, continent=None, country=None):
        return None

    @classmethod
    def language(cls, continent=None, country=None):
        return None

    @classmethod
    def currency(cls, continent=None, country=None):
        return None

    @classmethod
    def longitude(cls, continent=None, country=None):
        return None

    @classmethod
    def latitude(cls, continent=None, country=None):
        return None

    @classmethod
    def lat_long(cls, continent=None, country=None):
        return LatLong(1, 2)

    @classmethod
    def postal_code(cls, country=None):
        return None

    @classmethod
    def state(cls, country=None):
        return None

    @classmethod
    def street_name(cls):
        return None

    @classmethod
    def street_address(cls):
        return None

    @classmethod
    def address(cls):
        return None

    @classmethod
    def avenue(cls):
        return None

    @classmethod
    def road(cls):
        return None
