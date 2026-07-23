from panchang.constants import (
    TITHIS,
    NAKSHATRAS,
    YOGAS,
    KARANAS,
    PLANETS,
    RASHIS
)
from panchang.utils import normalize_angle

from .astronomy import AstronomyEngine

class PanchangEngine(AstronomyEngine):

    
    def get_nakshatra(self):

        moon_longitude = self.get_moon_longitude()

        nakshatra_index = int(
            moon_longitude // (360 / 27)
        )

        return NAKSHATRAS[nakshatra_index]
    

    def get_tithi(self):

        moon_longitude = self.get_moon_longitude()

        sun_longitude = self.get_sun_longitude()

        difference = normalize_angle(
            moon_longitude - sun_longitude
        )

        tithi_index = int(
            difference // 12
        )

        return TITHIS[tithi_index]
    
    def get_yoga(self):

        moon_longitude = self.get_moon_longitude()

        sun_longitude = self.get_sun_longitude()

        total = (moon_longitude + sun_longitude) % 360

        yoga_index = int(
            total // (360 / 27)
        )

        return YOGAS[yoga_index]
    
    def get_karana(self):

        moon_longitude = self.get_moon_longitude()

        sun_longitude = self.get_sun_longitude()

        difference = (
            moon_longitude - sun_longitude
        ) % 360

        karana_index = int(
            difference // 6
        )
        if karana_index >= len(KARANAS):
                karana_index = karana_index % len(KARANAS)

        return KARANAS[karana_index]

    

        