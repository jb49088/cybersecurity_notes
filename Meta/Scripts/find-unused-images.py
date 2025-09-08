import os
import re

# Define the path to the Obsidian vault and the target folder for images
vault_dir = r"C:\Users\justin\Obsidian Vault"
image_dir = r"C:\Users\justin\Obsidian Vault\Educational\Meta\Images"

# Function to get all PNG files in the image directory
def get_png_files(image_dir):
    return {f for f in os.listdir(image_dir) if f.lower().endswith('.png')}

# Function to find all image references in the markdown files within the vault
def get_image_references(vault_dir):
    image_refs = set()

    # Traverse the entire vault directory to check Markdown files
    for root, dirs, files in os.walk(vault_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)

                # Open each markdown file and look for image references
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Regex to find ![[image.png|...]] and ![image](image.png|...)
                    # Strip any |attributes part to get the filename
                    image_refs.update(re.findall(r'!\[\[([^\]]+\.png)(?:\|[^\]]*)?\]\]', content))
                    image_refs.update(re.findall(r'!\[.*\]\(([^)]+\.png)(?:\|[^\)]*)?\)', content))

    return image_refs

# Function to find unused PNG images
def find_unused_images(image_dir, vault_dir):
    # Get all the PNG images in the specified directory
    png_files = get_png_files(image_dir)

    # Get all the image references in the vault
    image_refs = get_image_references(vault_dir)

    # Remove the attributes part from the references to match only the filenames
    cleaned_image_refs = {ref.split('|')[0] for ref in image_refs}

    # Find unused images by checking which ones are not referenced in any Markdown file
    unused_images = png_files - cleaned_image_refs

    return unused_images

# Main function to run the process
def main():
    unused_images = find_unused_images(image_dir, vault_dir)
    
    if unused_images:
        print("Unused images found:")
        # Sort unused images in alphabetical order and add a dash with a space before each file name
        for image in sorted(unused_images):
            print(f" - {image}")
    else:
        print("No unused images found.")

if __name__ == "__main__":
    main()
