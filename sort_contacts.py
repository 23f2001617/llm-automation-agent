import json

input_file = "data/contacts.json"
output_file = "data/contacts-sorted.json"

# Load contacts from JSON file
with open(input_file, "r") as f:
    contacts = json.load(f)

# Sort contacts by last_name, then first_name
contacts_sorted = sorted(contacts, key=lambda x: (x["last_name"], x["first_name"]))

# Write sorted contacts back to JSON file
with open(output_file, "w") as f:
    json.dump(contacts_sorted, f, indent=4)

print("Contacts sorted successfully!")
