import os

def rename_files(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Directory not found")
        files = []
        for f in os.listdir(directory):
            if os.path.isfile(os.path.join(directory,f)):
                files.append(f)
        index = 1
        for file_name in files:
            original_path = os.path.join(directory,file_name)
            new_name = f"file{index}{os.path.splitext(file_name)[1]}"
            new_path = os.path.join(directory,new_name)
            os.rename(original_path,new_path)
            print(f"{file_name} -> {new_name}")
            index += 1
    except FileNotFoundError:
        print("Error: Directory not found")

if __name__=="__main__":
    directory = "C:/Users/Denisa/Desktop/anul_3_sem_1/Python/Laborator6"
    rename_files(directory)
