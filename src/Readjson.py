import json


class Readjson:
    def __init__(self, file_path):
        self.file_path = file_path
        self.encodings = ['utf-8', 'utf-16', 'utf-32', 'cp1252', 'windows-1250', 'latin-1']

    def read(self):
        """
        Lee un archivo JSON y carga su contenido en un diccionario.

        Returns:
        - dict: Contenido del archivo JSON cargado en un diccionario.
        """
        for encoding in self.encodings:
            try:
                with open(self.file_path, 'r', encoding=encoding) as file:
                    data = json.load(file)
                return data
            except FileNotFoundError:
                print(f"Error: No se encontró el archivo {self.file_path}.")
                return None
            except json.JSONDecodeError:
                print(f"Error: El archivo {self.file_path} no es un archivo JSON válido.")
                return None
            except UnicodeDecodeError:
                print('encoding no compatible')
                continue