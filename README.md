# Publications API server
This is a simple product to manage a list of publications. Each publication can have simple information about the publications, along with a list of the publication's authors. This app is built with the technologies:
1. FastAPI: A blazing fast Python async framework.
2. Pydantic: Pydantic is used for most of the validation for the API's input and output.
3. Tortoise: Asynchronous Relational Database object relational mapper (ORM). This ORM brings a Django-like API only asynchronously and without the need to django.
4. Pytest: Fast python test runner configured and running. Currently has a simple smoke test for the API server. 
5. Docker compose: For deployment and developer environment.
6. Poetry: Elegant python environment/dependency management. 

# How to use

## Run locally

```shell
C:\coding\publications-server>docker compose -f docker-compose-dev.yml up
```

This will spawn a postgres database and API server with it.

## Testing

```shell
pip install poetry
poetry install
pytest
```
