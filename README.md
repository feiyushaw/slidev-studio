# scientific-slidev

A reusable presentation toolkit for Slidev with three deliberate presentation modes:

- **Scholarly / Academic** — papers, defenses, conferences, literature and formal research talks.
- **HEP / Technical** — algorithms, experiments, engineering reviews and visualization-heavy R&D talks.
- **Tahta / Business** — internal reviews, strategy, product, roadmap, management and enterprise presentations.

Reusable scientific functionality lives in one theme-agnostic addon instead of forks of the upstream themes.

```text
                         slidev-addon-scientific
                                  │
                 equations · figures · visualizations
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
          Scholarly              HEP                Tahta
           Academic           Technical            Business
```

## Choosing a mode

| Presentation | Theme | Suggested style |
| --- | --- | --- |
| Paper / conference / defense | Scholarly | formal academic |
| Algorithm / experiment / engineering review | HEP | technical and visual |
| Internal project review / management / strategy | Tahta | business |
| Board / enterprise review | Tahta | `boardroom` variant |
| Data / finance / strategy | Tahta | `minimal` variant |
| Modern product / company deck | Tahta | `lagoon` variant |

Tahta is especially useful because its visual variants are design-token driven. For business decks we default to `boardroom`; switching to `minimal` or `lagoon` changes the visual direction without changing the scientific components.

## Current components

- `EquationBlock.vue` — consistent container for KaTeX/LaTeX-style equations.
- `ScientificFigure.vue` — publication-style figure, caption, sizing, SVG/PNG support.
- `PlotlyGraph.vue` — renders Plotly figure JSON exported from Python.
- `TrajectoryViewer.vue` — interactive SVG trajectory viewer with progress control.
- `OptimizationViewer.vue` — step-through visualization for optimization iterations.

The shared components use theme variables where practical, so the same evidence can be reused across Academic, Technical and Business decks.

## Quick start

Requirements: Node.js 20+.

```bash
npm install

npm run dev:scholarly   # Academic
npm run dev:hep         # Technical
npm run dev:business    # Business / Tahta
```

Example decks use this repository as a local addon:

```yaml
---
theme: scholarly # or hep / tahta
addons:
  - ../..
---
```

For Tahta business presentations:

```yaml
---
theme: tahta
addons:
  - ../..
themeConfig:
  variant: boardroom
---
```

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

In a business deck, equations should normally appear only when they materially support a decision or in a technical appendix.

## Python → Slidev

Keep scientific computation in Python and presentation/interaction in Slidev:

```text
Python / NumPy / simulator
          │
          ├── SVG / PNG ───────────> ScientificFigure
          ├── Plotly JSON ─────────> PlotlyGraph
          └── trajectory JSON ─────> TrajectoryViewer
```

Generate Plotly JSON:

```bash
python -m pip install numpy plotly
python python/export_plotly.py --output public/convergence.json
```

Then:

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

## Theme roles

### Scholarly — Academic

Use for formal academic talks, paper presentations, methodology/results structure, citations, theorems and Beamer-like organization.

### HEP — Technical

Use for dense technical results, experimental plots, trajectories, simulation and interactive visualization.

### Tahta — Business

Use for internal reviews, executive summaries, strategy, roadmap, product and enterprise presentations. Prefer Tahta's native `stats`, `fact`, `compare`, `chart`, `steps`, `diagram`, `statement` and other business-oriented layouts before inventing custom layout CSS. Scientific addon components remain available for evidence and technical appendices.

Recommended Tahta variants:

- `boardroom` — default enterprise / management / board review.
- `minimal` — data, finance, corporate strategy.
- `lagoon` — modern company and product decks.
- `soft` — approachable product/onboarding presentations.

## Design rules

1. Themes define visual language; the addon defines reusable capabilities.
2. Do not fork a theme merely to add scientific functionality.
3. Keep reusable components theme-agnostic.
4. Keep computation and data generation in Python when practical.
5. Prefer SVG for static scientific figures and JSON contracts for interactive visualization.
6. Keep PDF export usable even when interactive controls are present.
7. For Business mode, lead with decision, metric and consequence; move unnecessary technical depth to appendix/deep-dive slides.
8. Prefer the active theme's native layouts before custom CSS.

## Planned extensions

- `FieldViewer` for FEM/CFD scalar and vector fields.
- `BEVViewer` for autonomous-driving scenes.
- richer trajectory layers: lanes, agents, uncertainty envelopes and time playback.
- CMA-ES / MPPI / sampling-distribution evolution viewer.
- business adapters for company logo, classification and reusable executive-review metadata.
- export checks for browser presentation and PDF fallback.

## Upstream themes

- HEP: `AvencastF/slidev-theme-hep`
- Scholarly: `jxpeng98/slidev-theme-scholarly`
- Tahta: `zcag/tahta` (`slidev-theme-tahta`)

This project is an extension and integration layer; it does not replace the upstream themes.
