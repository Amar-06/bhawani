import swisseph as swe
from datetime import datetime


class PanchangEngine:

    def __init__(
        self,
        date_of_birth,
        time_of_birth,
        latitude,
        longitude
    ):

        self.date_of_birth = date_of_birth
        self.time_of_birth = time_of_birth
        self.latitude = latitude
        self.longitude = longitude

    def get_julian_day(self):

        dt = datetime.combine(
            self.date_of_birth,
            self.time_of_birth
        )

        jd = swe.julday(
            dt.year,
            dt.month,
            dt.day,
            dt.hour + dt.minute / 60
        )

        return jd