import random
from prodict import Prodict

from .number import Number
from .person import Person
from .location import Location
from .health import Health
from .car import Car
from .internet import Internet
from .datetime import DateTime


class Mimic:
    @classmethod
    def generate(cls, count=100, skip_ratio=0.0):
        """
        A loop to iterate over to generate data.

        :param count: Loop count
        :param skip_ratio: Ratio of skipping a loop, useful to mimic realistic data
        :return: Returns a Prodict (dot-dict)
        """
        for index in range(count):
            # if random.randint(0, 100) <= skip_ratio * 100:
            #     continue
            yield Prodict()
