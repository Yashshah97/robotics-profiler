import unittest
from robotics_profiler import test_profiler

class TestTestProfiler(unittest.TestCase):

    def test_empty_profile(self):
        result = test_profiler.test_empty_profile()
        self.assertEqual(result, [])

    def test_single_operation(self):
        result = test_profiler.test_single_operation()
        self.assertEqual(result, [42])

    def test_multiple_operations(self):
        result = test_profiler.test_multiple_operations()
        self.assertEqual(result, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
