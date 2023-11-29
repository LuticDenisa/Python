import sys
import os

def count_extensions():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Wrong number of parameters")
        directory = sys.argv[1]
        if not os.path.isdir(directory):
            raise FileNotFoundError("Directory not found")
        files = []
        for f in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, f)):
                files.append(f)
        if not files:
            raise ValueError("Directory is empty")
        extensions = {}
        for file_name in files:
            name, extension = os.path.splitext(file_name)
            extension = extension.lower()
            extensions[extension] = extensions.get(extension,0) + 1
        for extension, count in extensions.items():
            print(f"{extension}: {count} files")
    except FileNotFoundError:
        print("Error: Directory not found")
    except PermissionError:
        print("Error: Permission denied")
    except ValueError as v:
        print(f"Error: {v}")

if __name__ == "__main__":
    count_extensions()

#python C:/Users/Denisa/PycharmProjects/pythonProject/lab6/ex4.py C:/Users/Denisa/Desktop/anul_3_sem_1/Python/Laborator6