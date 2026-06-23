from config import get_api_key
import time
import requests

ROUTING_URL = "https://api.openrouteservice.org/v2/directions/driving-car"

ROUTING_API_KEY = get_api_key("ROUTING_API_KEY")

HEADERS = {
    "Authorization": ROUTING_API_KEY,
    "Content-Type": "application/json",
}

class RouteError(Exception):
    pass

def routing(
    origin_lat: float,
    origin_lon: float,
    destination_lat: float,
    destination_lon: float,
    max_retries: int = 2,
    timeout: int = 15,
):
    body = {
        "coordinates": [
            [origin_lon, origin_lat],
            [destination_lon, destination_lat],
        ],
    }
    for attempt in range(max_retries):
        try:
            res = requests.post(
                ROUTING_URL,
                json=body,
                headers=HEADERS,
                timeout=timeout,
            )
            if res.status_code == 429:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                raise RouteError("ERROR: Rate Limited (OpenRouteService)")
            res.raise_for_status()
            data = res.json()
            if not data.get("routes"):
                raise RouteError("ERROR: No Route Returned")
            summary = data["routes"][0]["summary"]
            if not summary:
                raise RouteError("ERROR: Invalid Response Format")
            return {
                "distance_meters": int(summary["distance"]),
                "duration_seconds": int(summary["duration"]),
            }
        except requests.Timeout:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise RouteError("ERROR: Request Timed Out (OpenRouteService Routing)")
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise RouteError(f"ERROR: Routing Failed; {str(e)}")
    raise RouteError("ERROR: Routing Failed")