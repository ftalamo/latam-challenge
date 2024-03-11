import unittest
import json
import os
from src.modules.Readjson import read_json


class TestReadJson(unittest.TestCase):
    def setUp(self):
        # Crear un archivo JSON de prueba
        self.json_file = "test_data.json"
        with open(self.json_file, 'w', encoding='utf-8') as f:
            f.write('{"name": "John", "age": 30}\n')
            f.write('{"name": "Jane", "age": 25}\n')
            f.write('{"name": "Doe", "age": "invalid"}\n')
            f.write('Invalid JSON Line\n')

    def test_read_json_existing_file(self):
        # Verificar si lee correctamente el archivo existente
        result = read_json(self.json_file)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result, list)

    def test_read_json_nonexistent_file(self):
        # Verificar si maneja correctamente un archivo inexistente
        result = read_json("nonexistent_file.json")
        self.assertIsNone(result)

    def test_read_json_invalid_json(self):
        # Verificar si maneja correctamente JSON inválido en el archivo
        result = read_json(self.json_file)
        self.assertEqual(len(result), 2)

    def tearDown(self):
        # Eliminar el archivo JSON de prueba
        os.remove(self.json_file)

if __name__ == '__main__':
    unittest.main()