import unittest
from robotics_profiler import path_planning

class TestPathPlanner(unittest.TestCase):

    def test_path_planner_init(self):
        planner = path_planning.PathPlanner((0, 0), (10, 10))
        self.assertEqual(planner.start, (0, 0))
        self.assertEqual(planner.end, (10, 10))

    def test_path_planner_plan(self):
        planner = path_planning.PathPlanner((0, 0), (10, 10))
        waypoints = planner.plan()
        self.assertEqual(len(waypoints), 10)

    def test_path_planner_plan_zero_waypoints(self):
        planner = path_planning.PathPlanner((0, 0), (10, 10))
        waypoints = planner.plan(num_waypoints=0)
        self.assertEqual(waypoints, [])

if __name__ == "__main__":
    unittest.main()
