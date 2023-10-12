from elasticsearch import Elasticsearch
from config import ELASTICSEARCH_PORT

# Initialize the Elasticsearch client
es = Elasticsearch([{"host": "elasticsearch", "port": ELASTICSEARCH_PORT, "scheme": "http"}])
