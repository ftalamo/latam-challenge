import unittest
from src.modules.format_date import format_date


class TestFormatDate(unittest.TestCase):
    def test_format_date(self):
        # Caso de prueba 1: Fecha válida
        input_date_1 = "2022-01-15T12:30:45+00:00"
        expected_output_1 = "2022,01,15"
        self.assertEqual(format_date(input_date_1), expected_output_1)

        # Caso de prueba 2: Otra fecha válida
        input_date_2 = "2023-05-20T18:45:30+00:00"
        expected_output_2 = "2023,05,20"
        self.assertEqual(format_date(input_date_2), expected_output_2)

        # Caso de prueba 3: Fecha inválida (formato incorrecto)
        input_date_3 = "2023/05/20 18:45:30"
        with self.assertRaises(ValueError):
            format_date(input_date_3)

        # Puedes agregar más casos de prueba según sea necesario

if __name__ == '__main__':
    unittest.main()