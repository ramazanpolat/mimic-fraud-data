from typing import List
from prodict import Prodict


class Country(Prodict):
    name: str
    cities: List[str]

