import unittest
from robotics_profiler import reporting

class TestReporting(unittest.TestCase):
    def test_format_report(self):
        report_data = {
            'function1': {'time': 10, 'calls': 5},
            'function2': {'time': 20, 'calls': 3},
            'function3': {'time': 15, 'calls': 7}
        }
        formatted_report = reporting.format_report(report_data)
        self.assertIn("function1: 0.40 (5 calls)\n", formatted_report)
        self.assertIn("function2: 0.80 (3 calls)\n", formatted_report)
        self.assertIn("function3: 0.60 (7 calls)\n", formatted_report)

    def test_generate_report(self):
        report_data = {
            'function1': {'time': 10, 'calls': 5},
            'function2': {'time': 20, 'calls': 3},
            'function3': {'time': 15, 'calls': 7}
        }
        formatted_report = reporting.generate_report(report_data)
        self.assertIn("Flame Report\n", formatted_report)
        self.assertIn("  function1: 0.22 (5 calls)\n", formatted_report)
        self.assertIn("  function3: 0.33 (7 calls)\n", formatted_report)
        self.assertIn("  function2: 0.45 (3 calls)\n", formatted_report)

if __name__ == "__main__":
    unittest.main()
