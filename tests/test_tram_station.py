# Author: przewnic
import unittest
from tram_model.TramStation import TramStation


class TestTramStation(unittest.TestCase):
    def test_set_distance(self):
        station = TramStation("S")
        station.set_distance(None, 0)
        self.assertEqual(station.distance_to[None], 0)
        s = TramStation("S1", 1)
        s2 = TramStation("S2", 2)
        s.set_distance(s2, 10)
        self.assertEqual(s.distance_to[s2], 10)

    def test_get_distance(self):
        station = TramStation("S")
        self.assertEqual(station.get_distance(None), None)
        s = TramStation("S1", 1)
        s2 = TramStation("S2", 2)
        s.set_distance(s2, 10)
        self.assertEqual(s.get_distance(s2), 10)

    def test_get_tram_wait(self):
        station = TramStation("S")
        self.assertEqual(station.get_tram_wait(), 0)

    def test_get_name(self):
        station = TramStation("S")
        self.assertEqual(station.get_name(), "S")

    def test_get_trams_queue(self):
        station = TramStation("S")
        self.assertEqual(len(station.get_trams_queue()), 0)

    def test_tram_arrives(self):
        station = TramStation("S")
        station.tram_arrives(None)
        self.assertEqual(station.trams_queue[0], None)

    def test_tram_departs(self):
        station = TramStation("S")
        self.assertFalse(station.tram_departs(None))

    def test_info(self):
        station = TramStation("S")
        self.assertEqual(station.info(), f"Stacja: S Tramwaje: \n")


if __name__ == '__main__':
    unittest.main()
