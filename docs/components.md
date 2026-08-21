# Shared Components

The shared addon provides reusable presentation capabilities that are independent of the selected theme.

## Design principle

```text
Theme = visual language
Addon = reusable capability
```

The same component can therefore be used in Scholarly, HEP, or Tahta without changing the component implementation.

## ScientificFigure

Use for publication-quality SVG/PNG figures with consistent sizing and captions.

```html
<ScientificFigure
  src="/benchmark.svg"
  caption="Benchmark across evaluation conditions."
/>
```

Prefer SVG for plots, diagrams, and vector graphics when practical.

## PlotlyGraph

Use for interactive Plotly figures generated from Python.

```html
<PlotlyGraph src="/convergence.json" :height="420" />
```

Recommended pipeline:

```text
Python / Plotly
→ JSON
→ public/*.json
→ PlotlyGraph
```

## EquationBlock

Use when an equation is a principal object on the slide and benefits from a visual container.

```md
<EquationBlock title="Objective function">

$$
J(\tau)=\sum_t \ell(x_t,u_t)
$$

</EquationBlock>
```

Normal inline and block KaTeX equations do not require `EquationBlock`.

## TrajectoryViewer

Use for interactive trajectory data.

```html
<TrajectoryViewer src="/trajectory.json" />
```

The current JSON contract is intentionally simple so simulation or planning code can export it directly.

## OptimizationViewer

Use when optimization evolution is part of the argument and the audience needs more than the final objective value.

Typical uses include:

- iterative optimization
- candidate evolution
- convergence inspection
- algorithm comparison

## Theme-specific usage

### Scholarly

Use shared components as research evidence inside methodology/results slides.

### HEP

Use them freely; visualization and technical evidence are central to this mode.

### Tahta

Use them selectively. Prefer native Tahta business layouts for executive metrics and standard charts, and use shared components for technical evidence or appendices.

## Avoid component duplication

Do not create `ScholarlyPlotlyGraph`, `HEPPlotlyGraph`, and `TahtaPlotlyGraph` unless their behavior is genuinely different. Styling should inherit from or adapt to the active theme whenever possible.
