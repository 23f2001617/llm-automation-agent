import os
import json

def extract_h1_title(file_path):
    """Extract the first H1 title (# Heading) from a markdown file."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    return None  # Return None if no H1 heading is found

data_dir = "data/docs"
index = {}

# Traverse all markdown files recursively
for root, _, files in os.walk(data_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, data_dir)  # Remove "data/docs/" prefix
            title = extract_h1_title(file_path) or "Untitled"
            index[relative_path] = title

# Write the index to a JSON file
index_path = os.path.join(data_dir, "index.json")
with open(index_path, "w", encoding="utf-8") as json_file:
    json.dump(index, json_file, indent=4)

print(f"Index saved to {index_path}")
