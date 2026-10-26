import unittest
from robotics_profiler import profiler

class TestProfiler(unittest.TestCase):
    def test_profiler(self):
        with self.assertRaises(AttributeError):
            profiler.Profiler().start_block("non_existent")

    @profiler.profile
    def add(a, b):
        return a + b

    def test_profiled_function(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
