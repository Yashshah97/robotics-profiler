# Robotics Micro-Profiler

This project provides a lightweight micro-profiler for robotics applications, allowing developers to easily measure and analyze the performance of complex kinematics and path planning algorithms. With its simple, flame-style text reports, this library makes it easy to identify bottlenecks and optimize your code. Built with test-driven development and thorough documentation in mind, this instrumentation library is designed to be a reliable tool for robotics engineers.

## What makes it unique

Combines kinematics and path planning with an instrumentation library with flame-style text reports — a niche where few ready-made tools exist.

## Features

- **`robotics_profiler/profiler.py`** — Core instrumentation logic and API
- **`robotics_profiler/kinematics.py`** — Kinematics module for calculating robot movements
- **`robotics_profiler/path_planning.py`** — Path planning module for generating motion plans
- **`robotics_profiler/reporting.py`** — Flame-style text reporting functionality
- **`robotics_profiler/util.py`** — Utility functions and constants used throughout the library
- **`robotics_profiler/test_profiler.py`** — Unit tests for the profiler module

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/robotics-profiler.git
cd robotics-profiler

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
robotics-profiler/
├── robotics_profiler/
│   ├── profiler.py
│   ├── kinematics.py
│   ├── path_planning.py
│   ├── reporting.py
│   ├── util.py
│   ├── test_profiler.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **robotics** · Archetype: **profiler** ·
Built autonomously by JARVIS on 2026-10-26. MIT licensed.
