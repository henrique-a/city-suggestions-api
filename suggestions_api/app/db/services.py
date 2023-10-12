from db.client import es
from db.index import cities_index


class CityService:
    def get_suggestions(self, city_name: str, latitude: float | None, longitude: float | None):
        query = {
            "query": {
                "function_score": {
                    "query": {"match": {"name": {"query": city_name, "fuzziness": "AUTO", "max_expansions": 1}}},
                    "boost_mode": "replace",
                    "min_score": 0.01,
                    "functions": [],
                }
            }
        }
        if longitude is not None and latitude is not None:
            query["query"]["function_score"]["functions"].append(
                {
                    "gauss": {
                        "location": {
                            "origin": {"lat": latitude, "lon": longitude},
                            "scale": "500km",
                            "offset": "500km",
                            "decay": 0.33,
                        }
                    }
                }
            )

        results = es.search(index=cities_index, body=query)
        if longitude is None and latitude is None:
            # Normalize score
            MAX_SCORE = 8.04694
            for hit in results["hits"]["hits"]:
                hit["_score"] = hit["_score"] / MAX_SCORE

        suggestions = []
        for hit in results["hits"]["hits"]:
            suggestions.append({**hit["_source"], "score": hit["_score"]})

        return suggestions
