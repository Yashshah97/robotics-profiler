"""Smoke tests for profiler."""
import unittest

from robotics_profiler import profiler


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(profiler, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(profiler) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
