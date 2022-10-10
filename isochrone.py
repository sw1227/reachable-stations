import requests


class IsochroneClient():
    """Class for Mapbox Isochronne API"""
    def __init__(self, api_key) -> None:
        self.base_url = "https://api.mapbox.com/isochrone/v1/mapbox"
        self.api_key = api_key

    def search(self, lat, lon, minutes, profile="walking"):
        """Find isochrone from given point
        - lat, lon: departure point
        - minutes: time [min] from the departure point
        - profile: walking/cycling/driving
        """
        assert profile in ["walking", "cycling", "driving"], "Invalid profile"
        assert 0 < minutes <= 60, "minutes must be in (0, 60]"

        params = {
            "contours_minutes": minutes,
            "polygons": "true",
            "access_token": self.api_key
        }
        url = f"{self.base_url}/{profile}/{lon},{lat}"
        resp = requests.get(url, params=params)
        assert resp.ok, "Error: Response not OK!"
        data = resp.json()
        # if denoise=1.0 (default), only the largest contour will be returned
        return data["features"][0]
