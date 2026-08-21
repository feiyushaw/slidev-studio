# Python Visualization Workflow

`slidev-studio` keeps numerical computation and data preparation in Python, while Slidev handles presentation, layout, animation, and interaction.

## Recommended architecture

```text
Python / NumPy / Pandas / simulator
          │
          ├── SVG / PNG ───────────> ScientificFigure
          ├── Plotly JSON ─────────> PlotlyGraph
          └── trajectory JSON ─────> TrajectoryViewer
```

This keeps scientific code reusable outside the presentation and avoids embedding large computation pipelines into the browser layer.

## Static figures

Generate plots in Python:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.xlabel("Iteration")
plt.ylabel("Objective")
plt.savefig("public/result.svg", bbox_inches="tight")
```

Use them in Slidev:

```html
<ScientificFigure
  src="/result.svg"
  caption="Objective over iterations."
/>
```

Prefer SVG for line plots and diagrams. Use PNG for raster images or outputs that do not convert well to vector graphics.

## Plotly

Install Python requirements:

```bash
python -m pip install -r python/requirements.txt
```

Generate an example:

```bash
python python/export_plotly.py --output public/convergence.json
```

Render it:

```html
<PlotlyGraph src="/convergence.json" :height="420" />
```

## Trajectory data

Generate the example trajectory file:

```bash
python python/export_trajectory.py --output public/trajectory.json
```

Render it:

```html
<TrajectoryViewer src="/trajectory.json" />
```

Current trajectory data contract:

```json
[
  {
    "name": "candidate-0",
    "best": false,
    "points": [
      {"x": 0.0, "y": 0.0},
      {"x": 1.0, "y": 0.2}
    ]
  }
]
```

## Reuse the same experiment outputs

A useful convention is:

```text
experiment/
├── paper_figure.pdf
├── slide_figure.svg
├── convergence.json
└── trajectory.json
```

Then:

- LaTeX paper uses `paper_figure.pdf`
- Slidev uses `slide_figure.svg`
- interactive slides use the JSON outputs

## PDF export

Browser interaction cannot be preserved fully in PDF. For any interactive visualization:

1. choose a useful default/static state;
2. preview the deck in the browser;
3. export PDF;
4. inspect the exported frame manually.

When a figure must remain publication-quality in PDF, provide a static SVG fallback rather than relying only on interaction.
