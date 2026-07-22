import swisseph as swe
from datetime import datetime

from panchang.constants import (
    TITHIS,
    NAKSHATRAS,
    YOGAS,
    KARANAS
)
from panchang.utils import normalize_angle

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
    
    def get_moon_longitude(self):

        jd = self.get_julian_day()

        moon_position = swe.calc_ut(
                jd,
                swe.MOON
            )

        longitude = moon_position[0][0]

        return longitude
    
    def get_nakshatra(self):

        moon_longitude = self.get_moon_longitude()

        nakshatra_index = int(
            moon_longitude // (360 / 27)
        )

        return NAKSHATRAS[nakshatra_index]
    
    def get_sun_longitude(self):

        jd = self.get_julian_day()

        sun_position = swe.calc_ut(
            jd,
            swe.SUN
        )

        longitude = sun_position[0][0]

        return longitude
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

        