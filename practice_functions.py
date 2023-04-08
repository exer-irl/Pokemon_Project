import requests
import json
import pandas as pd
from pprint import pprint
from typing import List, Dict, Union

def getMoveURLS(num_moves):
    """
    Write a function that takes in an integer 'num_moves' and returns that
    many moves' URLs in a list
    """
    response = requests.get(f'https://pokeapi.co/api/v2/move?limit={num_moves}')
    assign = json.loads(response.text)
    results_list = assign['results']
    move_list = []
    for move in results_list: 
        move_list.append(move['name'])
        #print(move['name'])
    return move_list









def damageCalc(att_pokemon, target, move, burn = False, weather = None) -> float:
    """
    Calculates the effective power of a move when used by one Pokemon on another using the given inputs.

    Effective Power (EP) is calculated as EP = power * STAB * enemytype1 * enemytype2 * burn_effect * weather_effect

    Parameters:
    
    -----------
    att_pokemon : str
        The name of the attacking Pokemon.
    target : str
        The name of the defending Pokemon.
    move : str
        The name of the move the attacking Pokemon is using.
    burn : bool, optional
        A boolean indicating whether the attacking Pokemon is burned or not. Default is False.
    weather : str, optional
        A string indicating the current weather condition. Default is None.

    Returns:
    --------
    float
        The calculated power as an float.

    Raises:
    -------
    ValueError:
        If any of the input parameters are invalid.

    Examples:
    ---------
    >>> damageCalc('Charizard', 'Blastoise', 'Flamethrower')
    100
    >>> damageCalc('Pikachu', 'Squirtle', 'Thunderbolt', burn=True, weather='rain')
    85
    """
x = damageCalc()

def get_pokemon_type_advantages_disadvantages(pokemon:str) -> dict:
    """
    Takes a Pokemon and returns its strengths and weaknesses against other types.
    
    Args:
    - pokemon_type (str): A string representing the name of a Pokemon.
    
    Returns:
    - A dictionary with keys representing the type(s) that the input Pokemon is strong against ('Advantages')
      and keys representing the type(s) that the input Pokemon is weak against ('Disadvantages').
      The values associated with each key are lists of strings representing the corresponding types.
    """
    pass

def get_pokemon_by_move(move: Union[str, int]) -> List[Dict[str, Union[str, int]]]:
    """
    Return a list of dictionaries containing the name and ID of all Pokemon that can learn a given move.

    Parameters:
    move (Union[str, int]): The name or ID of the move to search for.

    Returns:
    List[Dict[str, Union[str, int]]]: A list of dictionaries, where each dictionary represents a Pokemon that can learn the move.
    Each dictionary contains the keys "name" and "id", which respectively hold the name and ID of the Pokemon.
    """
    pass

from typing import List, Dict, Union
import requests

def get_pokemon_info(name: str) -> Dict[str, Union[str, int, List[Dict[str, str]]]]:
    """
    Given the name of a Pokemon, returns a dictionary containing information
    about the Pokemon, including its name, ID, types, abilities, and more.

    Args:
        name: A string representing the name of the Pokemon to look up.

    Returns:
        A dictionary containing information about the Pokemon. The dictionary
        has the following keys:
        - "name": A string representing the name of the Pokemon.
        - "id": An integer representing the ID of the Pokemon.
        - "types": A list of dictionaries, where each dictionary represents
            a type that the Pokemon has. Each dictionary has the following keys:
            - "name": A string representing the name of the type.
            - "url": A string representing the URL of the type's PokeAPI endpoint.
        - "abilities": A list of dictionaries, where each dictionary represents
            an ability that the Pokemon has. Each dictionary has the following keys:
            - "name": A string representing the name of the ability.
            - "url": A string representing the URL of the ability's PokeAPI endpoint.
        - "stats": A list of dictionaries, where each dictionary represents
            a stat that the Pokemon has. Each dictionary has the following keys:
            - "name": A string representing the name of the stat.
            - "url": A string representing the URL of the stat's PokeAPI endpoint.
            - "base_stat": An integer representing the base value of the stat.
        - "moves": A list of dictionaries, where each dictionary represents
            a move that the Pokemon can learn. Each dictionary has the following keys:
            - "name": A string representing the name of the move.
            - "url": A string representing the URL of the move's PokeAPI endpoint.

    Raises:
        requests.exceptions.HTTPError: If there is an error accessing the PokeAPI.

    Example usage:
        >>> get_pokemon_info("charmander")
        {'name': 'charmander', 'id': 4, 'types': [{'name': 'fire', 'url': 'https://pokeapi.co/api/v2/type/10/'}, {'name': 'normal', 'url': 'https://pokeapi.co/api/v2/type/1/'}], 'abilities': [{'name': 'blaze', 'url': 'https://pokeapi.co/api/v2/ability/66/'}, {'n...
    """
    pass