"""
Unit tests for the robotics_profiler module.

This module contains unit tests to ensure the correctness of the
robotics_profiler library.
"""

import unittest
from io import StringIO
from contextlib import redirect_stdout

class TestProfiler(unittest.TestCase):

    def test_empty_profile(self):
        from robotics_profiler import Profiler
        profiler = Profiler()
        result = profiler.profile([])
        self.assertEqual(result, [])

    def test_single_operation(self):
        from robotics_profiler import Profiler
        profiler = Profiler()
        result = profiler.profile([lambda: 42])
        self.assertEqual(result, [42])

    def test_multiple_operations(self):
        from robotics_profiler import Profiler
        profiler = Profiler()
        result = profiler.profile([
            lambda: 1,
            lambda: 2,
            lambda: 3,
        ])
        self.assertEqual(result, [1, 2, 3])

    def test_flame_report(self):
        from robotics_profiler import Profiler
        profiler = Profiler()
        f = StringIO()
        with redirect_stdout(f):
            profiler.profile([
                lambda: 1,
                lambda: 2,
                lambda: 3,
            ])
        self.assertIn('Flame Report:', f.getvalue())

if __name__ == '__main__':
    unittest.main()
