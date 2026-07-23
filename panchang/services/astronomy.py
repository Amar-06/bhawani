import swisseph as swe
from datetime import datetime

from panchang.constants import (
    PLANETS,
    RASHIS,
)


class AstronomyEngine:

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

    def get_moon_longitude(self):

        jd = self.get_julian_day()

        moon_position = swe.calc_ut(
            jd,
            swe.MOON
        )

        return moon_position[0][0]
    def get_sun_longitude(self):

        jd = self.get_julian_day()

        sun_position = swe.calc_ut(
            jd,
            swe.SUN
        )

        longitude = sun_position[0][0]

        return longitude

    def get_rashi(self, longitude):

        rashi_index = int(longitude // 30)

        return RASHIS[rashi_index]

    def get_planet_rashis(self):

        positions = self.get_planet_positions()

        rashis = {}

        for planet, longitude in positions.items():

            rashis[planet] = {
                "longitude": longitude,
                "rashi": self.get_rashi(longitude)
            }
        return rashis
    
    def get_planet_positions(self):

        jd = self.get_julian_day()

        positions = {}

        for planet_name, planet_id in PLANETS.items():

            result = swe.calc_ut(jd, planet_id)

            longitude = result[0][0]

            positions[planet_name] = round(longitude, 4)

        # Ketu is always opposite Rahu
        positions["Ketu"] = round(
            (positions["Rahu"] + 180) % 360,
            4
        )

        return positions