# Author: przewnic
import unittest
from tram_model.SystemCsvReader import SystemCsvReader
from tram_model.TramStation import TramStation
from tram_model.Line import Line, LineType


class TestSystemCsvReader(unittest.TestCase):
    def test_delete_square_brackets(self):
        stream = """ """
        reader = SystemCsvReader(stream)
        string = "[abc]"
        self.assertEqual(reader.delete_square_brackets(string), "abc")

    def test_create_station(self):
        stream = """"station_name;tram_wait
                 """
        row = {"station_name": "S100", "tram_wait": 3}
        reader = SystemCsvReader(stream)
        self.assertIsInstance(reader.create_station(row), TramStation)
        self.assertEqual(reader.create_station(row).name, "S100")
        self.assertEqual(reader.create_station(row).tram_wait, 3)

    def test_create_line(self):
        stream = """line_number;stations;type
                 """
        row = {"line_number": 1, "stations": None, "type": "CIRCLE"}
        reader = SystemCsvReader(stream)
        self.assertIsInstance(reader.create_line(row, None), Line)
        self.assertEqual(reader.create_line(row, None).stations, [])
        self.assertEqual(reader.create_line(row, None).number, 1)
        self.assertEqual(reader.create_line(row, None).number_of_stations, 0)
        self.assertEqual(reader.create_line(row, None).line_type,
                         LineType.CIRCLE)
