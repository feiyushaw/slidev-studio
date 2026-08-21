# HEP Theme Guide

HEP is the **Technical** mode of `slidev-studio`. Use it for algorithm reviews, engineering presentations, experimental analysis, simulation results, and visualization-heavy R&D talks.

## Minimal deck

```md
---
theme: hep
addons:
  - slidev-addon-scientific
title: Technical Review
---

# Technical Review

Algorithm, experiments, and engineering evidence

---

# Main formulation

<EquationBlock title="Planning objective">

$$
J(\tau)=J_{\mathrm{safety}}+J_{\mathrm{comfort}}+J_{\mathrm{efficiency}}
$$

</EquationBlock>

---

# Experimental result

<PlotlyGraph src="/convergence.json" :height="420" />
```

Inside this repository, use the local addon path `../..` as shown in `examples/hep/slides.md`.

## What HEP is good at

HEP is appropriate when the deck contains a high density of:

- plots and quantitative results
- trajectories and simulation output
- optimization processes
- algorithm diagrams
- system architecture
- failure cases
- engineering comparisons
- technical equations

The theme itself already follows an academic/technical presentation style and includes structured page chrome and Plotly-oriented ideas. `slidev-studio` keeps the visualization functionality in the shared addon so the same components also work in other themes.

## Recommended slide patterns

### Problem → mechanism → evidence

```text
Observed problem
→ algorithm / system mechanism
→ experimental evidence
→ engineering conclusion
```

### Benchmark review

```text
Evaluation setup
→ metric definition
→ benchmark chart
→ failure cases
→ next engineering action
```

### Optimization / planning presentation

```text
State / input
→ objective
→ candidate generation
→ optimization evolution
→ final trajectory
→ quantitative evaluation
```

## Using trajectories

Export trajectory data to JSON and render it with the shared viewer:

```bash
python python/export_trajectory.py --output public/trajectory.json
```

```html
<TrajectoryViewer src="/trajectory.json" />
```

## Using optimization results

Use `OptimizationViewer` when the audience needs to inspect iteration-by-iteration behavior rather than only the final objective value.

```html
<OptimizationViewer :iterations="iterations" />
```

For publication-quality static plots, keep generation in Python and export SVG:

```python
plt.savefig("public/benchmark.svg", bbox_inches="tight")
```

```html
<ScientificFigure src="/benchmark.svg" caption="Benchmark across configurations." />
```

## Equations

Normal KaTeX/LaTeX syntax works in slide bodies. Use equations to define the quantity being evaluated or optimized; avoid placing a large derivation on every slide.

For a derivation-heavy formal academic presentation, Scholarly is usually the better theme.

## Suggested presentation structure

```text
Cover
→ Engineering problem
→ System / algorithm architecture
→ Key formulation
→ Experiment setup
→ Main plots
→ Interactive / dynamic visualization
→ Failure cases
→ Performance / latency
→ Conclusions and actions
```

## When not to use HEP

Use Scholarly when citations, formal research structure, references, and theorem-like content dominate the talk. Use Tahta when the primary audience needs decisions, roadmap, business status, risks, or executive metrics rather than technical depth.
