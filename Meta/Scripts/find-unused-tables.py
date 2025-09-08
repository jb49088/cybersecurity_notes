import os
import re

# Define the path to the vault and the new target directory
vault_path = r"C:\Users\justin\Obsidian Vault"
target_dir = r"C:\Users\justin\Obsidian Vault\Educational\Meta\Tables"

# Function to get all files in a directory
def get_files_in_directory(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):  # Only consider markdown files
                file_paths.append(os.path.join(root, file))
    return file_paths

# Function to get all links from a markdown file
def get_links_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Regex pattern for internal Obsidian links (e.g., [[file_name|optional_text]])
    # This matches links with pipes and strips the part after the pipe.
    return re.findall(r'\[\[([^\|\]]+)(?:\|[^\]]*)?\]\]', content)

# Step 1: Get a list of all files in the target directory
target_files = get_files_in_directory(target_dir)

# Step 2: Get a set of all file names in the vault (excluding the target directory)
all_files = get_files_in_directory(vault_path)
all_file_names = set(os.path.splitext(os.path.basename(f))[0] for f in all_files)

# Step 3: Collect all the links across the entire vault
linked_files = set()
for file_path in all_files:
    links = get_links_from_file(file_path)
    for link in links:
        # If the link refers to a file that exists in the vault, add it to the linked set
        linked_files.add(link)

# Step 4: Find unused files in the target directory (those not linked to anywhere)
unused_files = []
for target_file in target_files:
    target_file_name = os.path.splitext(os.path.basename(target_file))[0]
    if target_file_name not in linked_files:
        unused_files.append(target_file_name)

# Step 5: Output the unused files in alphabetical order (only file names)
if unused_files:
    unused_files.sort()  # Sort the file names alphabetically
    print("Unused tables found:")
    for unused in unused_files:
        print(f" - {unused}")
else:
    print("No unused files found in the specified directory.")
