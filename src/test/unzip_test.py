import unittest
import os
import shutil
import tempfile
import zipfile
from src.modules.unzip import unzip_file


class TestUnzipFile(unittest.TestCase):
    def setUp(self):
        # Crear un archivo ZIP de prueba
        self.zip_file = "test_file.zip"
        self.extract_to = tempfile.mkdtemp()
        with zipfile.ZipFile(self.zip_file, 'w') as zip_ref:
            zip_ref.writestr("file1.txt", "Contenido del archivo 1")
            zip_ref.writestr("file2.txt", "Contenido del archivo 2")

    def test_unzip_file(self):
        # Ejecutar la función
        result = unzip_file(self.zip_file, self.extract_to)

        # Verificar si se extraen correctamente los archivos
        extracted_files = os.listdir(self.extract_to)
        expected_files = ["file1.txt", "file2.txt"]
        self.assertCountEqual(extracted_files, expected_files)

        # Verificar si se devuelve una lista de información sobre los archivos extraídos
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(expected_files))
        self.assertTrue(all(isinstance(item, zipfile.ZipInfo) for item in result))

    def tearDown(self):
        # Eliminar el archivo ZIP de prueba y el directorio de extracción
        os.remove(self.zip_file)
        shutil.rmtree(self.extract_to)

if __name__ == '__main__':
    unittest.main()