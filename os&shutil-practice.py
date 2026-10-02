# OS, SHUTIL, and INPUT REVIEWER
# This program moves files into different folders.

import os
import shutil

# Ask the user for the folder where the files are
source_folder = input("Enter the folder name: ")

# Check if the folder exists
if not os.path.exists(source_folder):
    print("Folder does not exist.")

else:
    # Create folders for different file types
    os.makedirs("PDF", exist_ok=True)
    os.makedirs("JPEG", exist_ok=True)
    os.makedirs("TXT", exist_ok=True)

    # Look at every file inside the folder
    for filename in os.listdir(source_folder):

        # Get the complete file location
        file_path = os.path.join(source_folder, filename)

        # Move PDF files
        if filename.lower().endswith(".pdf"):
            shutil.move(file_path, "PDF")
            print(filename, "moved to PDF folder.")

        # Move JPEG files
        elif filename.lower().endswith(".jpeg"):
            shutil.move(file_path, "JPEG")
            print(filename, "moved to JPEG folder.")

        # Move TXT files
        elif filename.lower().endswith(".txt"):
            shutil.move(file_path, "TXT")
            print(filename, "moved to TXT folder.")

        # Ignore other file types
        else:
            print(filename, "was not moved.")