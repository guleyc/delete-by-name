# delete-by-name
A simple Python script to search for and delete all files with a specific name (e.g., `desktop.ini`) in a chosen folder and its subfolders.

## Features

- Recursively finds files by name in a selected directory
- Shows total number of found files before deletion
- Asks for confirmation before deleting
- Lists each deleted file

## Usage

1. **Clone the repository:**
   ```sh
   git clone https://github.com/guleyc/delete-by-name.git
   cd delete-by-name
   ```

2. **Run the script:**
   ```sh
   python file_deleter.py
   ```

3. **Follow the prompts:**
   - Enter the folder path you want to search.
   - Enter the filename you want to delete (e.g., `desktop.ini`).
   - The script will show how many files were found and ask if you want to delete them.
   - Confirm to delete.

## Example

```
Enter the folder path: C:\Users\YourName\Documents
Enter the filename to delete (e.g., desktop.ini): desktop.ini
Found 12 'desktop.ini' file(s).
Do you want to delete them all? (Y/N): y
Deleted: C:\Users\YourName\Documents\Project1\desktop.ini
Deleted: C:\Users\YourName\Documents\Project2\desktop.ini
...
Deletion completed.
```

## Requirements

- Python 3.x

_No external dependencies._

## License

MIT License
