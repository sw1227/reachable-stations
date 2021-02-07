import requests

class NavitimeClient():
    """Class for NAVITIME Reachable API"""
    def __init__(self, api_key) -> None:
        self.url = "https://navitime-reachable.p.rapidapi.com/reachable_transit"
        self.headers = {
            "x-rapidapi-host": "navitime-reachable.p.rapidapi.com",
            "x-rapidapi-key": api_key
        }

    def search(self, lat, lon, term_min, term_max, transit_limit):
        """Find reachable stations from given conditions
        - lat, lon: departure point
        - term_min, term_max: min/max of search time [minutes]
        - transit_limit: max # of transit
        """
        params = {
            "offset": "0",
            "limit": 2000, # 2000: Maximum value
            "transit_limit": transit_limit,
            "coord_unit": "degree",
            "datum": "wgs84",
            "walk_speed": "5",
            "start": f"{lat},{lon}",
            "term": term_max,
            "term_from": term_min,
            "node_type": "station"
        }
        resp = requests.get(self.url, headers=self.headers, params=params)
        assert resp.ok, "Error: Response not OK!"
        return resp.json()
