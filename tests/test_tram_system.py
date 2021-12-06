# Author: przewnic
import unittest
from tram_model.TramSystem import TramSystem


class TestTramSystem(unittest.TestCase):
    def test_set_lines(self):
        tram_system = TramSystem()
        self.assertEqual(tram_system.set_lines(None), None)

    def test_get_trams(self):
        tram_system = TramSystem()
        self.assertEqual(tram_system.get_trams(), [])

    def test_get_stations(self):
        tram_system = TramSystem()
        self.assertEqual(tram_system.get_stations(), [])

    def test_add_station(self):
        tram_system = TramSystem()
        tram_system.add_station(None)
        self.assertEqual(tram_system.stations[0], None)

    def test_add_tram(self):
        tram_system = TramSystem()
        tram_system.add_tram(None)
        self.assertEqual(tram_system.trams[0], None)

    def test_set_trams(self):
        tram_system = TramSystem()
        tram_system.set_trams(None)
        self.assertEqual(tram_system.trams, [])

if __name__ == '__main__':
    unittest.main()
