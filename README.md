# Buzz Solutions Coding Challenge

This project is developed using FastAPI and ElasticSearch to provide autocomplete suggestions for large cities in the USA and Canada with a population above 5000 people. The suggestions are scored and can be influenced by the caller's location, if provided.

I chose ElasticSearch as the database of this project because of its capabilities in text search, geo-spatial support and scalability. ElasticSearch has text and geo-spacial search score functions that were used in this project to calculate the scores of the suggestions endpoint. We can scale ElasticSearch to handle high levels of traffic by implementing the strategies like horizontal scaling, sharding, using replicas.

To scale the FastAPI container, you can use the docker-compose up command with the --scale option. For example, to run three instances of the API service: `docker-compose up --scale app=3`. This will start three instances of the API container, and Docker Compose will manage the load balancing between them.

## API Endpoint

The API endpoint is exposed at `/suggestions`. It allows users to retrieve autocomplete suggestions for cities based on their search query.

### Endpoint Parameters

- `q` (required): A query string parameter for the search term, which can be partial or complete.
- `latitude` (optional): A query string parameter for the caller's latitude, which can be used to improve relative scores.
- `longitude` (optional): A query string parameter for the caller's longitude, which can be used to improve relative scores.

### Endpoint Response

The endpoint returns a JSON response with an array of scored suggested matches. The suggestions are sorted by descending score.

Each suggestion in the response contains the following attributes:

- `score`: A floating-point number between 0 and 1 (inclusive) indicating confidence in the suggestion (1 is the most confident).
- `name`: The name of the location, which can be used to disambiguate between similarly named locations.
- `latitude`: The latitude coordinate of the location.
- `longitude`: The longitude coordinate of the location.


## Prerequisites

Before running this project, you will need Docker and Docker Compose installed on your system.

## Installation and Usage

1. Run the project with docker-compose.
   ```
   cd suggestions_api
   docker-compose up -d
   ```

2. The FastAPI application will be accessible at http://localhost:8000/suggestions

## Tests
To run unit tests, run the command

```
docker exec suggestions_api pytest --disable-pytest-warnings
```