"""Smoke tests for kinematics."""
import unittest

from robotics_profiler import kinematics


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(kinematics, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(kinematics) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
