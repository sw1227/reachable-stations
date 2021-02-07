import os
import json
import argparse
from navitime import NavitimeClient


def response_to_geojson(result):
    """Convert response from NAVITIME to GeoJSON-like dict"""
    features = [{
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                item["coord"]["lon"],
                item["coord"]["lat"]
            ]
        },
        "properties": {**item}
    } for item in result["items"]]

    return {
        "type": "FeatureCollection",
        "features": features
    }


if __name__ == "__main__":
    # argparse: latitude / longitude / output filename
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "lat",
        help="latitude of point",
        type=float
    )
    parser.add_argument(
        "lon",
        help="longitude of point",
        type=float
    )
    parser.add_argument(
        "geojson_name",
        help="file name (*.json, *.geojson) of the result"
    )
    args = parser.parse_args()
    target_point = {"lat": args.lat, "lon": args.lon}
    print(f"Sending request for {target_point}...")

    # Set up navitime client
    navitime = NavitimeClient(api_key=os.environ["RAPIDAPI_KEY"])

    # Send request and get response
    result = navitime.search(
        lat=target_point["lat"],
        lon=target_point["lon"],
        term_min=0,
        term_max=60,
        transit_limit=1
    )

    # Convert and save as GeoJSON
    geojson = response_to_geojson(result)
    filename = args.geojson_name
    print(f"Saving the result as {filename}")
    with open(filename, "w") as f:
        json.dump(geojson, f)
