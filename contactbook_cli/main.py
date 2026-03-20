import argparse
import sys
import os
import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

def save_contact(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=2)

parser = argparse.ArgumentParser()
parser.add_argument("name", type=str, nargs="?", help="Add contact's name")
parser.add_argument("email", type=str, nargs="?", help="Add contact's email")
parser.add_argument("-d", "--delete", type=int, help="Delete a contact by ID")
parser.add_argument("-l", "--list", help="List all contacts", action="store_true")

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.list:
    contacts = load_contacts()

    for contact in contacts:
        display_email = contact.get("email")
        print(f"{contact['id']}: {contact['name']}, {display_email}")
    sys.exit(0)

elif args.delete:
    contacts = load_contacts()

    new_contacts = []
    for contact in contacts:
        if contact["id"] != args.delete:
            new_contacts.append(contact)
    contacts = new_contacts
    save_contact(new_contacts)
    print(f"Contact with ID of {args.delete} deleted")

elif args.name:
    contacts = load_contacts()

    if len(contacts) == 0:
        new_id = 1
    else:
        new_id = contacts[-1]["id"] + 1
    
    contacts.append({"id": new_id, "name": args.name, "email": args.email})
    
    save_contact(contacts)
    
    print(f"Contact {args.name}, {args.email} added with the ID of {new_id}")