def main():
    filename = "my_file.txt"

    # Part 1: Create a new text file and write to it
    try:
        with open(filename, 'w') as file:
            file.write("First line of text.\n")
            file.write("Second line with number 123.\n")
            file.write("Third line with number 201.\n")
        print(f"Successfully wrote to {filename}.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error writing to file: {e}")

    # Part 2: Read the contents of the file and display them
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("\nContents of the file after initial write:")
        print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading from file: {e}")

    # Part 3: Append additional lines to the file
    try:
        with open(filename, 'a') as file:
            file.write("Fourth line of additional text.\n")
            file.write("Fifth line with number 789.\n")
            file.write("Sixth line with some more text.\n")
        print(f"Successfully appended to {filename}.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error appending to file: {e}")

    # Part 4: Read the updated contents of the file and display them
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("\nContents of the file after appending:")
        print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading from file: {e}")

if __name__ == "__main__":
    main()
