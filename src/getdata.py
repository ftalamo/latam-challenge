import os


def getdata(path, name):
    """
       Verifica si existe un archivo ZIP en un directorio.
"""
    file_path = os.path.join(path,name)
    return os.path.isfile(file_path) and file_path.endswith('.zip')
