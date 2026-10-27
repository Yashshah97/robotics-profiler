"""Smoke tests for test_profiler."""
import unittest

from robotics_profiler import test_profiler


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(test_profiler, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(test_profiler) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
