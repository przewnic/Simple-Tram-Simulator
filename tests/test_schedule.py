# Author: przewnic
import unittest
from tram_model.Schedule import Schedule


class TestSchedule(unittest.TestCase):
    def test_get_work_start(self):
        schedule = Schedule(0, None, None)
        self.assertEqual(schedule.get_start_time(), 0)

    def test_get_interval(self):
        schedule = Schedule(0, None, None)
        self.assertEqual(schedule.get_interval(), 15)

    def test_add_tram(self):
        schedule = Schedule(0, None, None)
        self.assertFalse(schedule.add_tram(0))


if __name__ == '__main__':
    unittest.main()
