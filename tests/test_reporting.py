"""Smoke tests for reporting."""
import unittest

from robotics_profiler import reporting


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(reporting, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(reporting) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
