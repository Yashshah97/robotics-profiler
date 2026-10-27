import unittest
from robotics_profiler import util

class TestUtils(unittest.TestCase):
    def test_format_time_ns(self):
        self.assertEqual(util.format_time_ns(123456789), "123.46 ns")
        self.assertEqual(util.format_time_ns(0), "0.00 ns")

    def test_format_time_s(self):
        self.assertEqual(util.format_time_s(1.23456789), "1.23 s")
        self.assertEqual(util.format_time_s(0), "0.00 s")

    def test_format_memory_bytes(self):
        self.assertEqual(util.format_memory_bytes(1024), "1 KB")
        self.assertEqual(util.format_memory_bytes(123456789), "117 MB")
        self.assertEqual(util.format_memory_bytes(0), "0 B")

if __name__ == "__main__":
    unittest.main()
