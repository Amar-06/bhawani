import swisseph as swe

from panchang.constants import RASHIS
from .astronomy import AstronomyEngine


class KundliEngine(AstronomyEngine):

    def get_lagna(self):

        jd = self.get_julian_day()

        houses = swe.houses(
            jd,
            self.latitude,
            self.longitude,
            b'P'      # Placidus house system
        )

        ascendant = houses[1][0]

        return round(ascendant, 4)
    def get_lagna_rashi(self):

        lagna = self.get_lagna()

        index = int(lagna // 30)

        return {
            "longitude": lagna,
            "rashi": RASHIS[index]
        }