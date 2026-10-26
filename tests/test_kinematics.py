import unittest
from robotics_profiler import kinematics

class TestKinematics(unittest.TestCase):

    def test_distance(self):
        self.assertAlmostEqual(kinematics.distance(0, 0, 3, 4), 5)
        self.assertAlmostEqual(kinematics.distance(-2, -2, 1, 1), 6)

    def test_speed(self):
        self.assertAlmostEqual(kinematics.speed(10, 2), 5)
        self.assertAlmostEqual(kinematics.speed(15, 3), 5)

    def test_acceleration(self):
        self.assertAlmostEqual(kinematics.acceleration(10, 2), 2.5)
        self.assertAlmostEqual(kinematics.acceleration(15, 3), 2.5)

    def test_position(self):
        self.assertEqual(kinematics.position(1, 2), (1, 2))
        self.assertEqual(kinematics.position(-3, -4), (-3, -4))

if __name__ == '__main__':
    unittest.main()
