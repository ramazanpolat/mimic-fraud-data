import random
from datetime import datetime


class DateTime:
    @classmethod
    def between(cls, from_year=1980, from_month=1, from_day=1, from_hour=0, from_min=0, from_second=1,
                to_year=2020, to_month=12, to_day=31, to_hour=0, to_min=0, to_second=0):
        from_ts = int(datetime(from_year, from_month, from_day, from_hour, from_min, from_second).timestamp())
        to_ts = int(datetime(to_year, to_month, to_day, to_hour, to_min, to_second).timestamp())

        datetime.fromtimestamp(random.randint(from_ts, to_ts))

        return None

    @classmethod
    def between_ts(cls, from_ts=None, to_ts=None):
        from_ts = from_ts or datetime(1980, 1, 1, 1, 1, 1).timestamp()
        to_ts = to_ts or datetime(2020, 1, 1, 1, 1, 1).timestamp()

        return datetime.fromtimestamp(random.randint(int(from_ts), int(to_ts)))

    @classmethod
    def between_dt(cls, from_ts=datetime(1980, 1, 1, 1, 1, 1),
                   to_ts=datetime(2020, 1, 1, 1, 1, 1)):
        return cls.between_ts(int(from_ts.timestamp()), int(to_ts.timestamp()))

    @classmethod
    def between_year(cls, from_year=1980, to_year=2020):
        from_date = datetime(year=from_year, month=1, day=1)
        to_date = datetime(year=to_year, month=12, day=31)

        return cls.between_dt(from_date, to_date)

    @classmethod
    def yield_datetime(cls, from_year=1980, from_month=1, from_day=1, from_hour=0, from_min=0, from_second=1,
                       to_year=2020, to_month=1, to_day=1, to_hour=0, to_min=0, to_second=0):
        from_ts = int(datetime(from_year, from_month, from_day, from_hour, from_min, from_second).timestamp())
        to_ts = int(datetime(to_year, to_month, to_day, to_hour, to_min, to_second).timestamp())

        while True:
            yield datetime.fromtimestamp(random.randint(from_ts, to_ts))
