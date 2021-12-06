# Author: przewnic
import unittest
from tram_model.Line import Line, LineType
from tram_model.TramStation import TramStation


class TestLine(unittest.TestCase):
    def test_add_station(self):
        line = Line(0, [], LineType.STRAIGHT)
        self.assertFalse(line.add_station(None))
        s = TramStation("S1", 1)
        self.assertTrue(line.add_station(s))

    def test_get_length(self):
        line = Line(0, None, LineType.STRAIGHT)
        self.assertEqual(line.get_length(), 0)
        s = TramStation("S1", 1)
        s2 = TramStation("S2", 2)
        line = Line(0, [s, s2], LineType.STRAIGHT)
        self.assertEqual(line.get_length(), 2)

    def test_get_number(self):
        line = Line(0, None, LineType.STRAIGHT)
        self.assertEqual(line.get_number(), 0)

    def test_get_stations(self):
        line = Line(0, None, LineType.STRAIGHT)
        self.assertEqual(line.get_stations(), [])

    def test_get_station(self):
        s = TramStation("S1", 1)
        line = Line(0, [s], LineType.STRAIGHT)
        self.assertEqual(line.get_station(0), s)

    def test_get_type(self):
        line = Line(0, None, LineType.STRAIGHT)
        self.assertEqual(line.get_type(), LineType.STRAIGHT)

    def test_info(self):
        line = Line(0, None, LineType.STRAIGHT)
        self.assertEqual(line.info(), f"Linia 0:\n")

    def test_count_number_of_stations(self):
        line = Line(0, None, LineType.STRAIGHT)
        self.assertEqual(line.count_number_of_stations(), 0)
        s = TramStation("S1", 1)
        s2 = TramStation("S2", 2)
        line = Line(0, [s, s2], LineType.STRAIGHT)
        self.assertEqual(line.count_number_of_stations(), 2)


if __name__ == '__main__':
    unittest.main()
