import os

file_folder: str = 'D:/gb/s/d/seminar.exe'
    

def parse_path(path: str) -> tuple[str]:
    
    *folder, file, ext = (i for i in path.split('/') for i in i.split('.'))
    temp_str : str = ''
    for i in folder:
        temp_str += i + '/'
    return temp_str, file, ext

print(parse_path(file_folder))

#Или так:

def parse_path2(path: str) -> tuple[str]:
    file_path, ext = os.path.splitext(path)
    folder, file = os.path.split(file_path)
    return folder, file, ext

print(parse_path2(file_folder))
