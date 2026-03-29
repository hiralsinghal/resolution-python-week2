import argparse
import requests
import sys

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

greet_parser = subparsers.add_parser("greet", help="Greet someone")
greet_parser.add_argument("name", type=str, help="Name of the person to greet")

pokemon_parser = subparsers.add_parser("pokemon", help="Search a Pokemon")
pokemon_parser.add_argument("pokemon",type=str, help="Your favourite Pokemon")

args = parser.parse_args()

if args.command == "greet":
    print(f"Hello, {args.name}!")

if args.command == "pokemon":
    print(f"Your favourite pokemon is {args.pokemon}")

if args.command=="pokemon":
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{args.pokemon}")
    if req.status_code != 200:
        print("API returned with error")
        sys.exit(1)
    api_parsed = req.json()
    print(f"args.pokemon")
    print(f"Ablility 1 is {api_parsed['abilities'][0]['ability']['name']}")
    print(f"Ability 1 being hidden is {api_parsed['abilities'][0]['is_hidden']}") 