import requests

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

def get_pokemon_data(name: str) -> dict | None:
    """
    Fetches JSON data for a given Pokémon from PokéAPI.
    Args:
        name (str): The Pokémon name to query.
    Returns:
        dict: A dictionary containing the Pokémon's data if successful.
        None: If the API request fails or the Pokémon is not found.
    """
    url = f"{POKEAPI_BASE_URL}pokemon/{name}"
    response = requests.get(url, timeout = 5)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

if __name__ == "__main__":
    pokemon_name = input("Enter a Pokémon name: ").lower()
    pokemon_info = get_pokemon_data(pokemon_name)

    if pokemon_info:
        print(f"Height: {pokemon_info['height']}")
        print(f"Weight: {pokemon_info['weight']}")
        print(f"ID: {pokemon_info['id']}")
        print(f"Order: {pokemon_info['order']}")
