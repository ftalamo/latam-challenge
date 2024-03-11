import unittest
import os
import psutil
from src.modules.measure_performance import measure_performance


class TestMeasurePerformance(unittest.TestCase):
    def test_measure_performance(self):
        # Función de prueba que solo duerme por un segundo
        @measure_performance
        def test_function():
            import time
            time.sleep(1)

        # Ejecutar la función
        test_function()

        # Verificar si el archivo performance.txt se creó y contiene información
        self.assertTrue(os.path.exists("../performance.txt"))

        # Verificar si la información escrita en el archivo es correcta
        with open("../performance.txt", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertIn("Función: test_function", content)
            self.assertIn("Tiempo:", content)
            self.assertIn("Uso de memoria:", content)
            file.close()

        # Eliminar el archivo de performance después de la prueba
        os.remove("../performance.txt")


if __name__ == '__main__':
    unittest.main()
