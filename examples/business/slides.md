---
theme: tahta
addons:
  - ../..
themeConfig:
  variant: boardroom
layout: cover
kicker: Internal Review · 2026
title: Planning Platform <span class="accent2">Business Review</span>
subtitle: Decisions, metrics, architecture, and next steps
---
---
layout: stats
kicker: Executive summary
title: What changed this quarter
stats:
  - { value: 18, unit: "%", label: quality improvement, tone: good }
  - { value: 23, unit: "%", label: lower p95 latency, tone: good }
  - { value: 3, label: open blockers, tone: warn }
---
---
layout: statement
kicker: Decision
 title: Keep the business story simple; open the technical depth only when it changes the decision.
---
---
layout: default
kicker: Evidence
 title: Interactive engineering evidence remains available
---

<PlotlyGraph src="/plotly-demo.json" :height="360" />

---
layout: default
kicker: Technical appendix
 title: Scientific components work without changing the business theme
aside: "technical deep dive"
---

<EquationBlock title="Optional model detail">

$$
\mathbf{u}^{*}=\arg\min_{\mathbf{u}}\sum_{t=0}^{T}\ell(\mathbf{x}_t,\mathbf{u}_t)+V_\theta(\mathbf{x}_T)
$$

</EquationBlock>

---
layout: end
kicker: Next step
title: Decide · Execute · Measure
---
