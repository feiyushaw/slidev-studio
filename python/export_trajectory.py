"""Export trajectory data for <TrajectoryViewer>.

Replace the demo arrays with planner/simulator outputs. The JSON schema is:
[{"name": str, "best": bool, "points": [{"x": float, "y": float}, ...]}]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def build_demo() -> list[dict]:
    x = np.linspace(0, 60, 80)
    trajectories = []
    for idx, offset in enumerate((-2.0, -1.0, 0.0, 1.0, 2.0)):
        y = offset + 0.8 * np.sin(x / 11.0 + idx * 0.15)
        trajectories.append({
            "name": f"candidate-{idx}",
            "best": offset == 0.0,
            "points": [{"x": float(px), "y": float(py)} for px, py in zip(x, y)],
        })
    return trajectories


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build_demo(), indent=2), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
