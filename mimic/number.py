import random


class Number:
    @classmethod
    def integer(cls):
        return random.randint(1, 1000)

    @classmethod
    def between(cls, a, b):
        return random.randint(a, b)

    @classmethod
    def binomial_dist(cls):
        return None

    @classmethod
    def normal_dist(cls):
        return None

    @classmethod
    def poisson_dist(cls):
        return None

    @classmethod
    def geometric_dist(cls):
        return None

    @classmethod
    def exponential_dist(cls):
        return None

    @classmethod
    def percent(cls, precision=0):
        return None
