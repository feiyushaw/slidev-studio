# Slidev Studio

`slidev-studio` is a reusable presentation toolkit built on Slidev with three primary presentation modes:

- **Scholarly / Academic** — papers, defenses, conferences, literature reviews and formal research talks.
- **HEP / Technical** — algorithms, experiments, engineering reviews and visualization-heavy R&D talks.
- **Tahta / Business** — internal reviews, strategy, product, roadmap, management and enterprise presentations.

Reusable scientific and technical capabilities live in one theme-agnostic addon instead of theme forks.

```text
                            Slidev Studio
                                  │
                  shared presentation capabilities
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
          Scholarly              HEP                Tahta
           Academic           Technical            Business
```

## Quick start

Requirements: Node.js 20+.

```bash
git clone https://github.com/feiyushaw/slidev-studio.git
cd slidev-studio
npm install

npm run dev:scholarly   # Academic
npm run dev:hep         # Technical
npm run dev:business    # Business / Tahta
```

Built-in templates:

```text
examples/
├── scholarly/slides.md
├── hep/slides.md
└── business/slides.md
```

Start from the example closest to your audience and communication goal.

## Which theme should I use?

| Presentation | Theme | Primary goal |
| --- | --- | --- |
| Paper / conference / defense | Scholarly | academic rigor and structure |
| Algorithm / experiment / engineering review | HEP | technical evidence and visualization |
| Internal project review / management / strategy | Tahta | status, decisions, metrics and roadmap |

For mixed presentations, keep one theme for the whole deck and add shared components where needed. Do not switch themes halfway through a presentation.

See [Choosing a Theme](docs/choosing-a-theme.md) for the detailed decision rule.

## Documentation

### Start here

- [Getting Started](docs/getting-started.md) — installation, template workflow, preview and export.
- [Choosing a Theme](docs/choosing-a-theme.md) — how to select Scholarly, HEP or Tahta.

### Theme guides

- [Scholarly / Academic](docs/scholarly.md)
- [HEP / Technical](docs/hep.md)
- [Tahta / Business](docs/tahta.md)

### Shared capabilities

- [Shared Components](docs/components.md)
- [Python Visualization Workflow](docs/python-visualization.md)

## Shared components

Current reusable components:

- `EquationBlock.vue` — consistent container for KaTeX/LaTeX-style equations.
- `ScientificFigure.vue` — figure, caption and SVG/PNG support.
- `PlotlyGraph.vue` — Plotly figure JSON exported from Python.
- `TrajectoryViewer.vue` — interactive SVG trajectory viewer.
- `OptimizationViewer.vue` — step-through optimization visualization.

The design principle is:

```text
Theme = visual language
Addon = reusable capability
```

The same `PlotlyGraph`, `ScientificFigure`, or `TrajectoryViewer` can therefore be reused in Academic, Technical and Business decks.

## Python → Slidev

Keep numerical computation and data preparation in Python and use Slidev for presentation and interaction:

```text
Python / NumPy / Pandas / simulator
          │
          ├── SVG / PNG ───────────> ScientificFigure
          ├── Plotly JSON ─────────> PlotlyGraph
          └── trajectory JSON ─────> TrajectoryViewer
```

See [Python Visualization Workflow](docs/python-visualization.md).

## Tahta business variants

Recommended Tahta variants:

- `boardroom` — enterprise, management and board review; default recommendation.
- `minimal` — strategy, data and finance.
- `lagoon` — modern company and product decks.
- `soft` — product introduction and onboarding.

Example:

```yaml
---
theme: tahta
addons:
  - ../..
themeConfig:
  variant: boardroom
---
```

## Design rules

1. Choose the theme from audience and communication goal.
2. Prefer the active theme's native layouts before custom CSS.
3. Keep reusable components theme-agnostic.
4. Keep computation and data generation in Python when practical.
5. Prefer SVG for static scientific figures and JSON for interactive visualization.
6. Check PDF export separately for interactive slides.
7. In Business mode, lead with status, consequence and decision; move unnecessary technical depth to appendix or deep-dive slides.

## Planned extensions

- `FieldViewer` for FEM/CFD scalar and vector fields.
- `BEVViewer` for autonomous-driving scenes.
- richer trajectory layers: lanes, agents, uncertainty envelopes and time playback.
- CMA-ES / MPPI / sampling-distribution evolution viewer.
- company metadata and classification support for Business mode.
- export checks and CI.

## Upstream themes

- HEP: `AvencastF/slidev-theme-hep`
- Scholarly: `jxpeng98/slidev-theme-scholarly`
- Tahta: `zcag/tahta` (`slidev-theme-tahta`)

Slidev Studio integrates these upstream themes; it does not replace them.
