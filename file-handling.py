# file_handling_assignment.py

def create_file():
    """Create a new file and write initial content."""
    try:
        with open("my_file.txt", "w") as file:
            file.write("Welcome to my file handling example.\n")
            file.write("Here are some interesting numbers: 42, 99, 2024\n")
            file.write("This file demonstrates file operations in Python.\n")
        print("File created and initial content written successfully.")
    except PermissionError:
        print("Error: Permission denied. Cannot write to file.")
    except Exception as e:
        print(f"An unexpected error occurred while creating the file: {e}")

def read_file():
    """Read the contents of the file and display them."""
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Current content of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_to_file():
    """Append additional lines to the existing file."""
    try:
        with open("my_file.txt", "a") as file:
            file.write("Adding a line with more information about file handling.\n")
            file.write("Python makes file operations easy with built-in functions.\n")
            file.write("Here's a final note: Remember to handle files with care!\n")
        print("Additional lines appended successfully.")
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied. Cannot append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while appending to the file: {e}")

def main():
    """Main function to execute the tasks."""
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to show the appended content

if __name__ == "__main__":
    main()
