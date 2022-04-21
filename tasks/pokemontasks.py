import requests
import prefect
from prefect import Task

class ExtractPokemon(Task):
    def run(self, **kwargs):
        logger = prefect.context.get("logger")
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        if response.ok: 
            return response.json()
        logger.warning(f"Could not load pokemon list! Error {response.status_code}")
        return {"results": []}


class TransformPokemon(Task):
    def run(self, pokemon):
        logger = prefect.context.get("logger")
        url = pokemon["url"]
        name = pokemon["name"].title()
        logger.info(f"Getting {name} from {url}")
        response = requests.get(url)
        if response.ok:
            return response.json()
        logger.warning(f"Could not load pokemon {name}! Error {response.status_code}")
        return {} 
        
        
class LoadPokemon(Task):
    def run(self, pokemon):
        logger = prefect.context.get("logger")
        logger.info(len(pokemon))

