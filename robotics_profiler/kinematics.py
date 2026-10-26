"""
Kinematics module for calculating robot movements.

This module provides functions to calculate the kinematic parameters of a robot,
such as its position, velocity and acceleration.
"""

def distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points (x1, y1) and (x2, y2).

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        float: The Euclidean distance between the two points.
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def speed(distance, time):
    """
    Calculate the speed of a robot given its distance and time.

    Args:
        distance (float): The distance traveled by the robot.
        time (float): The time taken to travel the distance.

    Returns:
        float: The speed of the robot.
    """
    return distance / time


def acceleration(distance, time):
    """
    Calculate the acceleration of a robot given its distance and time.

    Args:
        distance (float): The distance traveled by the robot.
        time (float): The time taken to travel the distance.

    Returns:
        float: The acceleration of the robot.
    """
    return speed(distance, time) / time


def position(x, y):
    """
    Calculate the position of a robot given its x and y coordinates.

    Args:
        x (float): The x-coordinate of the robot's position.
        y (float): The y-coordinate of the robot's position.

    Returns:
        tuple: A tuple containing the x and y coordinates of the robot's position.
    """
    return x, y
