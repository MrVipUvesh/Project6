# Personal Journal Manager

Personal Journal Manager is a simple command-line Python application for creating, storing, viewing, searching, and deleting personal journal entries.

The project is built to practice file handling, object-oriented programming, exception handling, date and time formatting, pattern matching with `match-case`, and basic interaction with the operating system.

## Features

- Add new journal entries
- Automatically record the date and time of each entry
- Store entries in a local `journal.txt` file
- View all saved journal entries
- Search journal entries using a keyword or date
- Delete all journal entries
- Handle missing journal files gracefully
- Prevent empty journal entries
- Use a simple menu-driven interface

## Technologies Used

- Python 3.10 or later
- `os` module
- `datetime` module
- File handling
- Classes and objects
- Exception handling
- `match-case`
- String operations

## How It Works

When the program is started, it displays a menu containing five options:

1. Add a New Entry
2. View All Entries
3. Search of an Entry
4. Delete All Entries
5. Exit

The user can select an option by entering its corresponding number.

## Adding a New Entry

Selecting option `1` allows the user to write a new journal entry.

Example:

    Please select an option:

    1. Add a New Entry
    2. View All Entries
    3. Search of an Entry
    4. Delete All Entries
    5. Exit
    User Input:
    1

    Enter your journal entry:
    Today I completed my Python file handling project.

    Entry added successfully!

The program automatically adds a timestamp to the entry.

A journal file is created automatically as `journal.txt` if it does not already exist.

## Journal File Format

The entries are stored in the following format:

    Your Journal Entries:
    -----------------------------
    [08/10/26 - 11:20:15 PM]
    Today I completed my Python file handling project.

    [09/10/26 - 08:45:32 AM]
    Started working on another Python project.

The timestamp follows this format:

    DD/MM/YY - HH:MM:SS AM/PM

For example:

    08/10/26 - 11:20:15 PM

## Viewing All Entries

Selecting option `2` reads the complete contents of `journal.txt` and displays all saved entries.

Example:

    Please select an option:

    1. Add a New Entry
    2. View All Entries
    3. Search of an Entry
    4. Delete All Entries
    5. Exit
    User Input:
    2

    Your Journal Entries:
    -----------------------------
    [08/10/26 - 11:20:15 PM]
    Today I completed my Python file handling project.

    [09/10/26 - 08:45:32 AM]
    Started working on another Python project.

If the journal file does not exist, the program displays an appropriate error message instead of terminating.

## Searching Entries

Selecting option `3` allows the user to search the journal using a keyword or date.

Example using a keyword:

    User Input:
    3

    Enter a keyword or date to search: Python

    Matching Entries:

    -----------------------------
    Today I completed my Python file handling project.

The search is case-insensitive, so searching for `python`, `Python`, or `PYTHON` can find the same matching entry.

The same search system can also be used to search for a date.

Example:

    Enter a keyword or date to search: 08/10/26

    Matching Entries:

    -----------------------------
    [08/10/26 - 11:20:15 PM]

Since the search is performed line by line, matching lines from the journal file are displayed.

If nothing matches the search term, the program displays:

    No entries were found for the keyword: Python

## Deleting All Entries

Selecting option `4` asks the user for confirmation before deleting the journal file.

Example:

    User Input:
    4

    Are you sure you want to delete all entries? (yes/no): yes

    All journal entries have been deleted.

If the user chooses `no`:

    Are you sure you want to delete all entries? (yes/no): no

    Entries deletion terminated.

Any other response is treated as an invalid option.

## Empty Entry Validation

The program does not allow an empty journal entry.

Example:

    Enter your journal entry:

    Error: Journal entry can't be empty!

This prevents blank entries from being added to the journal.

## Program Structure

The main functionality is organized inside the `JournalManager` class.

### `JournalManager`

This class contains the operations required to manage the journal.

### `create_file()`

Creates `journal.txt` using exclusive creation mode.

The file is initialized with a heading when it does not already exist.

It also handles `FileExistsError` so that the program can continue normally if the file has already been created.

### `add_entry(entry)`

Adds a new entry to the journal.

The method:

- Checks whether the entry is empty
- Opens the file in append mode
- Generates the current timestamp
- Writes the timestamp and entry to the file
- Displays a success message

The timestamp is generated using:

    dt.now().strftime("%d/%m/%y - %I:%M:%S %p")

### `view_entries()`

Opens the journal file in read mode and displays all stored entries.

If the file does not exist, `FileNotFoundError` is handled and an error message is displayed.

### `search_entry(keyword)`

Searches the journal file line by line.

The search uses:

    keyword.lower() in entry.lower()

This makes the search case-insensitive.

The method can therefore be used to search for words, phrases, or dates that appear in the journal file.

### `del_entries(decision)`

Deletes the complete journal file after receiving confirmation from the user.

The method uses:

    os.remove("journal.txt")

It also handles the situation where the journal file does not exist.

## File Handling

This project demonstrates three common file modes:

### Write/Create Mode

    open("journal.txt", "x")

The `x` mode creates a new file and raises `FileExistsError` if the file already exists.

### Append Mode

    open("journal.txt", "a")

The `a` mode adds new content to the end of the existing file without removing previous entries.

### Read Mode

    open("journal.txt", "r")

The `r` mode reads the existing contents of the journal file.

The project uses `with open(...)` so that files are automatically closed after the operation is completed.

## Exception Handling

The program uses `try-except` blocks to handle expected file-related errors.

For example:

    try:
        with open("journal.txt", "r") as file:
            entry = file.read()
    except FileNotFoundError:
        print("Error: The Journal file does not exist. Please add a new entry first.")

This prevents the program from crashing when the journal file is unavailable.

The project also handles `FileExistsError` when attempting to create a file that already exists.

## Menu System

The main program continuously displays the menu using a `while True` loop.

The user's choice is processed using Python's `match-case` statement:

    match choice:
        case "1":
            ...
        case "2":
            ...
        case "3":
            ...
        case "4":
            ...
        case "5":
            ...
        case _:
            ...

The program continues running until the user selects option `5`.

## Project Structure

    Personal-Journal-Manager/
    ├── main.py
    ├── journal.txt
    └── README.md

`journal.txt` is created automatically by the program when the first valid entry is added. It does not need to be created manually.

## Requirements

Python 3.10 or later is recommended because the program uses the `match-case` statement, which was introduced in Python 3.10.

No external packages are required.

## How to Run

Open a terminal in the project directory and run:

    python main.py

On some systems, you may need to use:

    python3 main.py

## Example Session

A complete example session can look like this:

    Welcome to Personal Journal Manager!
    Please select an option:

    Please select an option:

    1. Add a New Entry
    2. View All Entries
    3. Search of an Entry
    4. Delete All Entries
    5. Exit
    User Input:
    1

    Enter your journal entry:
    Worked on my Python project today.

    Entry added successfully!

    Please select an option:

    1. Add a New Entry
    2. View All Entries
    3. Search of an Entry
    4. Delete All Entries
    5. Exit
    User Input:
    2

    Your Journal Entries:
    -----------------------------
    [08/10/26 - 11:20:15 PM]
    Worked on my Python project today.

    Please select an option:

    1. Add a New Entry
    2. View All Entries
    3. Search of an Entry
    4. Delete All Entries
    5. Exit
    User Input:
    3

    Enter a keyword or date to search: Python

    Matching Entries:

    -----------------------------
    Worked on my Python project today.

    Please select an option:

    1. Add a New Entry
    2. View All Entries
    3. Search of an Entry
    4. Delete All Entries
    5. Exit
    User Input:
    5

    Thank you for using Personal Journal Manager. Goodbye!

## Learning Objectives

This project is useful for understanding how several Python concepts work together in a practical application.

The main learning objectives are:

- Understanding classes and objects
- Working with text files
- Creating and appending to files
- Reading file contents
- Deleting files using the `os` module
- Handling file-related exceptions
- Working with dates and timestamps
- Searching text inside files
- Using case-insensitive string comparisons
- Building a menu-driven program
- Using `match-case`
- Organizing functionality into class methods

## Conclusion

Personal Journal Manager is a compact file-based Python application that demonstrates how basic Python concepts can be combined to create a useful command-line utility.

The project does not require a database or external dependencies. All journal data is stored locally in `journal.txt`, making it a straightforward example of using Python file handling for persistent data storage.
