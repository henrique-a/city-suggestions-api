import logging
import pandas as pd
from elasticsearch import helpers
from db.client import es


cities_index = "cities"

index_settings = {"number_of_shards": 1, "number_of_replicas": 0}

cities_mapping = {
    "properties": {
        "name": {"type": "text"},
        "location": {"type": "geo_point"},
        "country": {"type": "text"},
        "state": {"type": "text"},
    }
}


def index_city_data():
    tsv_file = "cities_canada-usa.tsv"
    df = pd.read_csv(tsv_file, sep="\t", header=0)
    cities_data = df.to_dict(orient="records")
    cities_data_geo = []
    for city_data in cities_data:
        city_data_geo = {
            "name": city_data["name"],
            "location": {"lat": city_data["lat"], "lon": city_data["long"]},
            "country": city_data["country"],
            "state": city_data["admin1"],
        }
        cities_data_geo.append(city_data_geo)

    actions = [
        {
            "_op_type": "index",
            "_index": cities_index,
            "_source": record,
        }
        for record in cities_data_geo
    ]

    helpers.bulk(es, actions, index=cities_index)
    logging.info(f"Indexed {len(actions)} documents.")
