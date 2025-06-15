import os

def find_files(folder, filename):
    matches = []
    for root, dirs, files in os.walk(folder):
        if filename in files:
            matches.append(os.path.join(root, filename))
    return matches

def main():
    folder = input("Enter the folder path: ").strip()
    while not os.path.isdir(folder):
        print("Invalid folder path. Please try again.")
        folder = input("Enter the folder path: ").strip()

    filename = input("Enter the filename to delete (e.g., desktop.ini): ").strip()
    if not filename:
        print("Filename cannot be empty.")
        return

    matches = find_files(folder, filename)
    count = len(matches)
    print(f"Found {count} '{filename}' file(s).")

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