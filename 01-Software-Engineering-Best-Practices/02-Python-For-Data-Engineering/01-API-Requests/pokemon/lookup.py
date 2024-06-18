# Make sure to add the correct imports here
from typing import Optional, Union, List
import requests

requests.get("https://pokeapi.co/api/v2/generation/1")

def get_pokemon(limit: int = 100, offset: int = 0) -> dict:
    """Get a list of pokemon. Return a dictionary containing the results. Limit the results to `limit` and offset by `offset`"""
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}")
    df =  response.json()
    print(df)
    return df

def check_pokemon_move(name: str = "bulbasaur", move: str = "swords-dance") -> bool:
    """Check if a pokemon can learn a move. Return True if it can, False otherwise."""
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    df = response.json()
    moves = [m['move']['name'] for m in df['moves']]
    return move in moves


def get_pokemon_types(
    type_one: str = "flying", type_two: Optional[Union[None, str]] = None
) -> List[Optional[str]]:
    """
    Get all pokemon of a given type `type_one`. Return a list of pokemon names.
    If `type_two` is given return only the Pokemon of type_one and type_two.
    """
    response_1 = requests.get(f"https://pokeapi.co/api/v2/type/{type_one}")
    type_1_df = response_1.json()
    pokemon_type_1 = [pokemon['pokemon']['name'] for pokemon in type_1_df['pokemon']]

    if type_two:
        response_2 = requests.get(f"https://pokeapi.co/api/v2/type/{type_two}")
        type_2_df = response_2.json()

        pokemon_type_2 = {pokemon['pokemon']['name'] for pokemon in type_2_df['pokemon']}
        return [pokemon for pokemon in pokemon_type_1 if pokemon in pokemon_type_2]

    return pokemon_type_1


def get_evolutions(name: str) -> dict:
    """
    For a given pokemon return a dictionary containing the pokemon it evolves
    from and into. The structure should be:
    {"from": "pokemon_name", "to": ["pokemon_name"]}
    If the pokemon does not evolve from or into another pokemon
    do not include the relevant key.
    """
    response_species = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{name}")
    species_df = response_species.json()
    evolution_chain_url = species_df['evolution_chain']['url']

    response_evolution_chain = requests.get(evolution_chain_url)
    evolution_chain_df = response_evolution_chain.json()

    evolutions = {}
    chain = evolution_chain_df['chain']

    def traverse_chain(chain, target_name):
        if chain['species']['name'] == target_name:
            return chain
        for evolution in chain.get('evolves_to', []):
            result = traverse_chain(evolution, target_name)
            if result:
                return result
        return None

    target_chain = traverse_chain(chain, name)

    if not target_chain:
        return evolutions

    if 'evolves_to' in target_chain and target_chain['evolves_to']:
        evolutions['to'] = [evo['species']['name'] for evo in target_chain['evolves_to']]

    current_chain = chain
    previous_pokemon = None
    while current_chain['species']['name'] != name:
        for evolution in current_chain.get('evolves_to', []):
            if evolution['species']['name'] == name:
                previous_pokemon = current_chain['species']['name']
                break
            current_chain = evolution
        if previous_pokemon:
            evolutions['from'] = previous_pokemon
            break

    return evolutions
