import os
import logging

# ---------------------- Logging Setup ----------------------
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------------- Functions ----------------------

# Create Directory
def create_directory():
    try:
        dir_name = input("Enter directory name: ")
        os.makedirs(dir_name, exist_ok=True)
        print("Directory created successfully.")
        logging.info(f"Directory '{dir_name}' created.")
    except Exception as e:
        print("Error creating directory.")
        logging.error(f"Error creating directory: {e}")

# List Files
def list_files():
    try:
        path = input("Enter directory path: ")
        files = os.listdir(path)
        print("Files in directory:")
        for file in files:
            print(file)
        logging.info(f"Listed files in '{path}'.")
    except Exception as e:
        print("Error listing files.")
        logging.error(f"Error listing files: {e}")

# Create & Write File
def write_file():
    try:
        file_name = input("Enter file name: ")
        content = input("Enter content to write: ")
        with open(file_name, 'w') as f:
            f.write(content)
        print("File written successfully.")
        logging.info(f"File '{file_name}' created and written.")
    except Exception as e:
        print("Error writing file.")
        logging.error(f"Error writing file: {e}")

# Read File
def read_file():
    try:
        file_name = input("Enter file name to read: ")
        with open(file_name, 'r') as f:
            content = f.read()
        print("\nFile Content:\n", content)
        logging.info(f"File '{file_name}' read successfully.")
    except Exception as e:
        print("Error reading file.")
        logging.error(f"Error reading file: {e}")

# ---------------------- Menu ----------------------
def menu():
    while True:
        print("\n--- Automation Menu ---")
        print("1. Create Directory")
        print("2. List Files")
        print("3. Write to File")
        print("4. Read File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_directory()
        elif choice == '2':
            list_files()
        elif choice == '3':
            write_file()
        elif choice == '4':
            read_file()
        elif choice == '5':
            print("Exiting...")
            logging.info("Program exited by user.")
            break
        else:
            print("Invalid choice. Try again.")
            logging.warning("Invalid menu choice entered.")

# ---------------------- Main ----------------------
if __name__ == "__main__":
    try:
        logging.info("Program started.")
        menu()
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        print("Unexpected error occurred.")