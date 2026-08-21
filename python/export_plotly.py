"""Export a Plotly figure to JSON consumable by <PlotlyGraph>.

Usage:
    python python/export_plotly.py --output examples/shared/public/convergence.json
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import plotly.graph_objects as go


def build_demo() -> go.Figure:
    iteration = np.arange(0, 50)
    objective = np.exp(-iteration / 11.0) + 0.04 * np.cos(iteration / 2.5)
    fig = go.Figure(go.Scatter(x=iteration, y=objective, mode="lines+markers", name="objective"))
    fig.update_layout(
        template="plotly_white",
        margin=dict(l=55, r=20, t=20, b=50),
        xaxis_title="Iteration",
        yaxis_title="Objective",
        showlegend=False,
    )
    return fig


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_demo().to_json(), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
