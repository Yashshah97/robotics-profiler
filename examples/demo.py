"""Demo for Robotics Micro-Profiler."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import robotics_profiler

print("Robotics Micro-Profiler", "v" + robotics_profiler.__version__)
print("modules:", [m for m in dir(robotics_profiler) if not m.startswith('_')])
