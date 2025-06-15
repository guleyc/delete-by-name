import os
import sys
import fnmatch

HELP_TEXT = """
File Deleter Help
-----------------
This script deletes files in a folder (and its subfolders) matching a given filename or pattern.

Usage:
    python file_deleter.py
        - Interactive mode. Prompts for folder and pattern.

    python file_deleter.py --help
    python file_deleter.py -h
        - Show this help message and exit.

    You can use wildcard patterns:
        Example: *.json   (delete all .json files)
        Example: *temp*   (delete files with 'temp' in the name)

WARNING: Deleted files cannot be recovered.
"""

def find_files(folder, pattern):
    matches = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                matches.append(os.path.join(root, file))
    return matches

def main():
    # Help argument check
    if len(sys.argv) > 1 and sys.argv[1] in ('--help', '-h'):
        print(HELP_TEXT)
        return

    folder = input("Enter the folder path: ").strip()
    while not os.path.isdir(folder):
        print("Invalid folder path. Please try again.")
        folder = input("Enter the folder path: ").strip()

    pattern = input("Enter the filename or pattern to delete (e.g., desktop.ini or *.json): ").strip()
    if not pattern:
        print("Pattern cannot be empty.")
        return

    matches = find_files(folder, pattern)
    count = len(matches)
    print(f"Found {count} file(s) matching '{pattern}'.")

    if count == 0:
        return

    confirm = input("Do you want to delete them all? (Y/N): ").strip().lower()
    if confirm == 'y':
        for path in matches:
            try:
                os.remove(path)
                print(f"Deleted: {path}")
            except Exception as e:
                print(f"Error deleting {path}: {e}")
        print("Deletion completed.")
    else:
        print("Deletion cancelled.")

if __name__ == "__main__":
    main()
