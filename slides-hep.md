---
theme: hep
addons:
  - slidev-addon-scientific
title: Slidev Studio · HEP
meeting: Slidev Studio Demo
preTitle: Slidev Studio
preDate: 2026-08-21
authors:
  - Researcher: ["Lab / Institution"]
---

# Slidev Studio

HEP theme + shared addon

---
layout: pageBar
---

# Mathematical formulation

<EquationBlock title="Trajectory optimization">

$$
\mathbf{u}^{*}=\arg\min_{\mathbf{u}}\sum_{t=0}^{T}\ell(\mathbf{x}_t,\mathbf{u}_t)+V_\theta(\mathbf{x}_T)
$$

</EquationBlock>

---
layout: pageBar
---

# Interactive trajectory visualization

<TrajectoryViewer src="./trajectory.json" />

---
layout: pageBar
---

# Python → Plotly → Slidev

<PlotlyGraph src="./convergence.json" :height="360" />
