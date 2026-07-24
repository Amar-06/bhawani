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
    def get_lagna_longitude(self):
        """
        Returns the Ascendant longitude in degrees.
        """

        jd = self.get_julian_day()

        cusps, ascmc = swe.houses(
            jd,
            self.latitude,
            self.longitude,
            b'P'
        )

        ascendant = ascmc[0]

        return round(ascendant, 4)
    def get_lagna(self):

        longitude = self.get_lagna_longitude()

        index = int(longitude // 30)

        return {
            "longitude": longitude,
            "rashi": RASHIS[index]
        }

    def get_house_cusps(self):
        """
        Returns the longitude of all 12 house cusps.
        """

        jd = self.get_julian_day()

        cusps, ascmc = swe.houses(
            jd,
            self.latitude,
            self.longitude,
            b'P'
        )

        houses = {}

        for i in range(12):
            houses[f"House {i + 1}"] = round(cusps[i], 4)

        return houses
    def get_house_rashis(self):

        houses = self.get_house_cusps()

        result = {}

        for house, longitude in houses.items():

            index = int(longitude // 30)

            result[house] = {
                "longitude": longitude,
                "rashi": RASHIS[index]
            }

        return result