import requests

POKEAPI_BASE_URL = 'https://pokeapi.co/api/v2/'

def get_pokemon_data(pokemon_name):
    """
    Fetches JSON data for the given Pokémon from PokéAPI.
    """
    url = f'{POKEAPI_BASE_URL}pokemon/{pokemon_name}'
    response = requests.get(url, timeout = 5)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f'[{response.status_code}] - Invalid Request...')

if __name__ == '__main__':
    pokemon_name = input('Enter a Pokémon: ').strip()

    if not pokemon_name or pokemon_name.isnumeric():
        print('Invalid Input...')
    else:
        pokemon = get_pokemon_data(pokemon_name.lower())

        if pokemon:
            in_meters = pokemon["height"] / 10
            in_kilograms = pokemon["weight"] / 10

            print()
            print(f'Base Experience: {pokemon["base_experience"]}')
            print(f'ID: {pokemon["id"]}')
            print(f'Height: {in_meters}m')
            print(f'Order: {pokemon["order"]}')
            print(f'Weight: {in_kilograms}kg')
            print()
