import argparse
import requests
import sys

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

greet_parser = subparsers.add_parser("greet", help="Greet someone")
greet_parser.add_argument("name", type=str, help="Name of the person to greet")

pokemon_parser = subparsers.add_parser("pokemon", help="Search a Pokemon")
pokemon_parser.add_argument("pokemon",type=str, help="Pokemon")

compare_parser = subparsers.add_parser("compare", help="Compare two pokemon")
compare_parser.add_argument("pokemon1",type=str, help="First Pokemon")
compare_parser.add_argument("pokemon2", type=str, help="Second Pokemon")

args = parser.parse_args()

if args.command == "greet":
    print(f"Hello, {args.name}!")

if args.command=="pokemon":
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{args.pokemon}")
    if req.status_code != 200:
        print("API returned with error")
        sys.exit(1)
    api_parsed = req.json()
    print(f'\033[1m{args.pokemon.capitalize()}\033[0m')
    print(f"Height: {api_parsed['height']}")
    print(f"Weight: {api_parsed['weight']}")
    print(f"Ablility 1: {api_parsed['abilities'][0]['ability']['name'].capitalize()}")
    print(f"Ability 1 being hidden is {api_parsed['abilities'][0]['is_hidden']}")
    print(f"Ability 2: {api_parsed['abilities'][1]['ability']['name'].capitalize()}")
    print(f"Ability 2 being hidden is {api_parsed['abilities'][1]['is_hidden']}")
    print(f"Move: {api_parsed['moves'][0]['move']['name'].capitalize()}")

if args.command=="compare":
    req1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{args.pokemon1}")
    req2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{args.pokemon2}")  

    if req1.status_code != 200 or req2.status_code != 200:
        print("API returned with error")
        sys.exit(1)
    
    p1 = req1.json()
    p2 = req2.json()

    print(f"Pokemon: {args.pokemon1.capitalize()} {args.pokemon2.capitalize()}")
    print(f"Height: {p1['height']} {p2['height']}")
    print(f"Weight: {p1['weight']} {p2['weight']}")
    print(f"Ability 1: {p1['abilities'][0]['ability']['name'].capitalize()} {p2['abilities'][0]['ability']['name'].capitalize()}")
    print(f"Ability 2: {p1['abilities'][1]['ability']['name'].capitalize()} {p2['abilities'][1]['ability']['name'].capitalize()}")
    print(f"Move: {p1['moves'][0]['move']['name'].capitalize()} {p2['moves'][0]['move']['name']}")