# Implementation with logging

import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)

while True:
    try:
        command = input("Enter a command: ")
        
        if command == "download":
            print("Downloading...")
            # Implement download logic here
        elif command == "search internet":
            print("Searching the internet...")
            # Implement search logic here
        else:
            raise ValueError("Command not recognized.")
    except ValueError as ve:
        print(f"Error: {str(ve)}. Please enter a valid command.")
        logging.error(f"Invalid command: {command}")
    except Exception as e:
        print("An unexpected error occurred. Please try again.")
        logging.error(f"Unexpected error: {str(e)}")
