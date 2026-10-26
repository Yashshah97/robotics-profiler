"""
Path planning module for generating motion plans.

This module provides a simple path planner that generates a sequence of
waypoints between two points in 2D space. The planner uses a basic linear
interpolation algorithm to calculate the waypoints.
"""

class PathPlanner:
    """
    A simple path planner that generates a sequence of waypoints between two points.
    """

    def __init__(self, start, end):
        """
        Initialize the path planner with the start and end points.

        :param start: The starting point (x, y)
        :param end: The ending point (x, y)
        """
        self.start = start
        self.end = end

    def plan(self, num_waypoints=10):
        """
        Generate a sequence of waypoints between the start and end points.

        :param num_waypoints: The number of waypoints to generate (default 10)
        :return: A list of waypoints (x, y) between the start and end points
        """
        if num_waypoints == 0:
            return []

        dx = self.end[0] - self.start[0]
        dy = self.end[1] - self.start[1]

        waypoints = []
        for i in range(num_waypoints):
            t = i / (num_waypoints - 1)
            x = self.start[0] + t * dx
            y = self.start[1] + t * dy
            waypoints.append((x, y))

        return waypoints

def test_path_planner():
    """
    Test the path planner with a simple example.
    """
    planner = PathPlanner((0, 0), (10, 10))
    waypoints = planner.plan()
    print(waypoints)

if __name__ == "__main__":
    test_path_planner()
