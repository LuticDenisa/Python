import os
import sys

def compute_size():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Wrong number of parameters")
        directory = sys.argv[1]
        if not os.path.isdir(directory):
            raise FileNotFoundError("Directory not found")
        size = 0
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root,file_name)
                size += os.path.getsize(file_path)
        print(f"Total size = {size} bytes")
    except FileNotFoundError:
        print("Error: Directory not found")
    except PermissionError:
        print("Error: Permission denied")

if __name__ == "__main__":
    compute_size()

# python C:/Users/Denisa/PycharmProjects/pythonProject/lab6/ex3.py C:/Users/Denisa/Desktop/anul_3_sem_1/Python/Laborator6