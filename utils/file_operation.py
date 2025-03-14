import os

def dump_python_code(code:str, file_name:str) -> None:
    with open(file_name, 'w') as f:
        f.write(code)