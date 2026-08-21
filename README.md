# scientific-slidev

A scientific presentation toolkit for Slidev. It keeps **HEP** and **Scholarly** as the two primary presentation themes, while moving reusable scientific functionality into one theme-agnostic addon.

## Why this structure

Slidev allows one theme and multiple addons per deck. Themes should mainly define visual language; reusable functionality is better implemented as an addon. This repository therefore avoids maintaining two divergent forks of HEP and Scholarly.

```text
                         slidev-addon-scientific
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
         equations            figures          visualizations
              │                   │                   │
              └──────────── shared scientific layer ──┘
                                  │
                     ┌────────────┴────────────┐
                     │                         │
                  HEP theme              Scholarly theme
             technical / visual       formal / academic
```

## Current components

- `EquationBlock.vue` — consistent container for KaTeX/LaTeX-style equations.
- `ScientificFigure.vue` — publication-style figure, caption, sizing, SVG/PNG support.
- `PlotlyGraph.vue` — renders Plotly figure JSON exported from Python.
- `TrajectoryViewer.vue` — interactive SVG trajectory viewer with progress control.
- `OptimizationViewer.vue` — step-through visualization for optimization iterations.

The components intentionally use theme variables such as `--slidev-theme-primary` when available, so the same component inherits the active HEP or Scholarly visual language.

## Quick start

Requirements: Node.js 20+.

```bash
npm install
npm run dev:hep
# or
npm run dev:scholarly
```

The example decks use the repository itself as a local addon:

```yaml
---
theme: hep       # or scholarly
addons:
  - ../..
---
```

For an external deck, install or reference this addon and keep the selected theme independent.

## Equations

Slidev uses KaTeX, so familiar LaTeX-style math remains available:

```md
<EquationBlock title="Trajectory optimization">

$$
\mathbf{u}^{*}=\arg\min_{\mathbf{u}}
\sum_{t=0}^{T}\ell(\mathbf{x}_t,\mathbf{u}_t)+V_\theta(\mathbf{x}_T)
$$

</EquationBlock>
```

## Python → Plotly → Slidev

The preferred workflow keeps scientific computation in Python and presentation/interaction in Slidev:

```text
Python / NumPy / simulator
          │
          ├── SVG / PNG ───────────> ScientificFigure
          │
          ├── Plotly JSON ─────────> PlotlyGraph
          │
          └── trajectory JSON ─────> TrajectoryViewer
```

Generate Plotly JSON:

```bash
python -m pip install numpy plotly
python python/export_plotly.py --output public/convergence.json
```

Then use it from a slide:

```html
<PlotlyGraph src="/convergence.json" :height="420" />
```

Generate trajectory JSON:

```bash
python python/export_trajectory.py --output public/trajectory.json
```

```html
<TrajectoryViewer src="/trajectory.json" />
```

The trajectory schema is deliberately simple:

```json
[
  {
    "name": "candidate-0",
    "best": false,
    "points": [{"x": 0.0, "y": 0.0}, {"x": 1.0, "y": 0.2}]
  }
]
```

## Theme roles

### HEP

Recommended for technical talks with dense results, experimental plots, trajectories, simulation and interactive visualizations. The upstream HEP theme already established a Python Plotly → JSON → Slidev workflow; this repository generalizes that capability and makes it reusable outside HEP-specific components.

### Scholarly

Recommended for formal academic talks, paper presentations, methodology/results structure, citations, theorems and Beamer-like organization. Scientific visualization components remain available without changing the Scholarly theme itself.

## Design rules

1. Do not fork a theme merely to add scientific functionality.
2. Keep reusable components theme-agnostic.
3. Keep computation and data generation in Python when practical.
4. Prefer SVG for static scientific figures.
5. Prefer JSON data contracts for interactive visualizations.
6. Keep PDF export usable even when interactive controls are present.
7. Add domain-specific viewers as independent components rather than coupling them to HEP or Scholarly.

## Planned extensions

- `FieldViewer` for FEM/CFD scalar and vector fields.
- `BEVViewer` for autonomous-driving scenes.
- richer trajectory layers: lanes, agents, uncertainty envelopes and time playback.
- CMA-ES / MPPI / sampling-distribution evolution viewer.
- reusable ablation/comparison/result layouts that do not override theme layouts.
- citation/paper-card adapter that cooperates with Scholarly's existing bibliography support.
- export checks for browser presentation and PDF fallback.

## Upstream themes

- HEP: `AvencastF/slidev-theme-hep`
- Scholarly: `jxpeng98/slidev-theme-scholarly`

This project is an extension layer and does not replace either upstream theme.
