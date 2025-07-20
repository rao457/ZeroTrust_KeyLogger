import os

def create_folder_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)
def write_to_file(path, content, mode="a"):
    with open(path, mode) as f:
        f.write(content)
        
def read_file(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return ""

def clear_file(path):
    open(path, 'w').close()