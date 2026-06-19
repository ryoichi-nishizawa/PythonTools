import os
import shutil
from dotenv import load_dotenv

# Get multiple paths as strings and split them into lists.
# Read the contents of the .env file.
load_dotenv()

# Get a string from .env (defaults to an empty string "" if not found).
raw_dirs = os.getenv("TARGET_DIRECTORIES", "")

# Convert to a list separated by commas.
TARGET_DIRECTORIES = [d.strip() for d in raw_dirs.split(",") if d.strip()]

# Target files and folders
FILE_MAPPING = {
    '.jpg':     'Images',
    '.jpeg':    'Images',
    '.png':     'Images',
    '.gif':     'Images',
    '.mp4':     'Movies',
    '.mov':     'Movies',
    '.avi':     'Movies',
    '.pdf':     'Documents',
    '.doc':     'Documents',
    '.docx':    'Documents',
    '.xls':     'Documents',
    '.xlsx':    'Documents',
    '.ppt':     'Documents',
    '.pptx':    'Documents',
    '.md':      'Documents',
    '.txt':     'Documents',
    '.csv':     'Documents',
    '.tsv':     'Documents',
    '.zip':     'Archives',
    '.rar':     'Archives',
    '.7z':      'Archives',
    '.exe':     'Apps'
}

def CleanDirectory(targetDirectory):
    # Check if the specified folder exists.
    if not os.path.exists(targetDirectory):
        print("Folder not found : {targetDirectory}.")
        return

    print(f"Starting the cleanup of {targetDirectory}…")

    for filename in os.listdir(targetDirectory):
        file_path = os.path.join(targetDirectory, filename)

        # Ignore folders and target only files.
        if os.path.isdir(file_path):
            continue

        # Extracting the file extension from the file name（'.pdf'）
        _, ext = os.path.splitext(filename)

        # Convert all letters to lowercase.
        ext = ext.lower()

        # Move to the corresponding folder.
        if ext in FILE_MAPPING:
            folder_name = FILE_MAPPING[ext]

            # Get full path.
            destination_dir = os.path.join(targetDirectory, folder_name)

            # If the destination folder does not yet exist, create it.
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            shutil.move(file_path, os.path.join(destination_dir, filename))
            print(f"Move completed : {filename} -> {folder_name}/")
        
    


# Processing is only performed when executed directly.
if __name__ == "__main__":
    print("==================== Start. ====================")
    if not TARGET_DIRECTORIES:
        print("The .env file either does not have a TARGET_DIRECTORIES setting or is empty.")
    else:
        for path in TARGET_DIRECTORIES:
            CleanDirectory(path)

        print("✨The organization is complete❣️")
    print("==================== Finish. ====================")