# Author: przewnic
import unittest
from tram_model.Tram import Tram


class TestTram(unittest.TestCase):
    def test_set_simulation_start(self):
        tram = Tram()
        tram.set_simulation_start(10)
        self.assertEqual(tram.simulation_start, 10)

    def test_set_line(self):
        tram = Tram()
        tram.set_line(10)
        self.assertEqual(tram.line, 10)

    def test_get_line(self):
        tram = Tram()
        self.assertIsNone(tram.get_line())
        tram = Tram(line="SomeLine")
        self.assertEqual(tram.get_line(), "SomeLine")

    def test_get_tram_id(self):
        tram = Tram()
        self.assertEqual(tram.get_tram_id(), 0)
        tram = Tram(tram_id=1)
        self.assertEqual(tram.get_tram_id(), 1)

    def test_get_working_time(self):
        tram = Tram()
        self.assertEqual(tram.get_working_time(), 60*8)
        tram = Tram(working_time=0)
        self.assertEqual(tram.get_working_time(), 0)

    def test_set_my_time(self):
        tram = Tram()
        tram.set_my_time(10)
        self.assertEqual(tram.my_time, 10)

    def test_check_end_thread(self):
        tram = Tram()
        tram.stop = True
        self.assertRaises(Exception, tram.check_end_thread)

    def test_get_time(self):
        tram = Tram()
        from datetime import datetime
        t = datetime.now()
        t = t.replace(hour=10, minute=0)
        tram.my_time = t
        present_time = 10
        self.assertEqual(tram.get_time(present_time), "10:10")

    def test_check_end_of_shift(self):
        tram = Tram(working_time=0)
        self.assertRaises(Exception, tram.check_end_of_shift, 0)

    def test_arrive_on_station(self):
        tram = Tram()
        self.assertRaises(Exception, tram.arrive_on_station)

    def test_drive_to_next(self):
        tram = Tram()
        self.assertRaises(Exception, tram.drive_to_next)

    def test_get_line_number(self):
        tram = Tram()
        self.assertEqual(tram.get_line_number(), None)

    def test_get_station(self):
        tram = Tram()
        self.assertEqual(tram.get_station(0), None)

    def test_get_tram_wait(self):
        tram = Tram()
        self.assertRaises(Exception, tram.get_tram_wait)

    def test_get_distance(self):
        tram = Tram()
        self.assertRaises(Exception, tram.get_distance, 0, 1)

    def test_wait_on_station(self):
        tram = Tram()
        self.assertRaises(Exception, tram.wait_on_station)


if __name__ == '__main__':
    unittest.main()
