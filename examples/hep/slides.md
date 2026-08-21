---
theme: hep
addons:
  - .
title: Scientific Slidev · HEP
meeting: Scientific Presentation Demo
preTitle: Scientific Slidev
preDate: 2026-08-21
authors:
  - Researcher: ["Lab / Institution"]
---

# Scientific Slidev

HEP theme + shared scientific addon

---
layout: pageBar
---

# Mathematical formulation

<EquationBlock title="Trajectory optimization" note="KaTeX syntax remains available inside Slidev Markdown.">

$$
\mathbf{u}^{*}=\arg\min_{\mathbf{u}}\sum_{t=0}^{T}\ell(\mathbf{x}_t,\mathbf{u}_t)+V_\theta(\mathbf{x}_T)
$$

</EquationBlock>

---
layout: pageBar
---

# Interactive trajectory visualization

<TrajectoryViewer src="/trajectory.json" />

---
layout: pageBar
---

# Python → Plotly → Slidev

```text
Python experiment → Plotly Figure JSON → <PlotlyGraph> → interactive slide
```

Use `python/export_plotly.py` to export a figure, then:

```html
<PlotlyGraph src="/convergence.json" :height="420" />
```
