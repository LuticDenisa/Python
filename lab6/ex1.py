import sys
import os

def read_files():
    try:
        if len(sys.argv) != 3:
            raise ValueError("Wrong number of parameters")

        directory_path = sys.argv[1]
        file_extension = sys.argv[2]

        if not os.path.isdir(directory_path):
            raise FileNotFoundError("Directory not found")

        for filename in os.listdir(directory_path):
            if filename.endswith(file_extension):
                file_path = os.path.join(directory_path, filename)
                try:
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        print(f"Contents of {filename}:\n{contents}")
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    except FileNotFoundError:
        print("Error: Directory not found.")
    except ValueError as v:
        print(f"Error: {v}")


if __name__ == "__main__":
    read_files()

#  python C:\Users\Denisa\PycharmProjects\pythonProject\lab6\ex1.py C:\Users\Denisa\Desktop\anul_3_sem_1\Python\Laborator6 txt