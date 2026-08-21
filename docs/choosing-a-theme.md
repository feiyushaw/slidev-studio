# Choosing a Theme

`slidev-studio` uses three primary themes with different roles. Choose the theme from the audience and communication goal, not from the subject area alone.

| Situation | Theme | Typical use |
| --- | --- | --- |
| Paper presentation, defense, conference | Scholarly | formal academic structure |
| Algorithm review, experiment report, engineering deep dive | HEP | dense technical material and visualization |
| Internal review, strategy, roadmap, management presentation | Tahta | business communication and decisions |

## Scholarly — Academic

Use Scholarly when the presentation should resemble a well-structured academic talk. It is suitable when citations, methodology, formal equations, references, theorems, and research results are central to the deck.

Typical structure:

```text
Problem
→ Related work
→ Method
→ Mathematical formulation
→ Experiment
→ Results
→ Discussion
→ References
```

Prefer Scholarly for:

- conference talks
- thesis or project defense
- paper reading and literature review
- formal research proposals
- presentations where bibliography and academic conventions matter

See [Scholarly Guide](./scholarly.md).

## HEP — Technical

Use HEP for research and engineering talks where plots, experimental results, algorithms, trajectories, system behavior, and technical evidence occupy a large part of the presentation.

Typical structure:

```text
Problem
→ System / algorithm
→ Experimental setup
→ Visualization
→ Benchmark
→ Failure cases
→ Engineering conclusions
```

Prefer HEP for:

- algorithm reviews
- R&D technical meetings
- simulation results
- performance analysis
- optimization or planning demonstrations
- visualization-heavy talks

See [HEP Guide](./hep.md).

## Tahta — Business

Use Tahta when the audience primarily needs status, decisions, metrics, risks, priorities, or a roadmap. Technical evidence can still be embedded through the shared addon, but it should support the business narrative rather than dominate every slide.

Typical structure:

```text
Executive summary
→ Current status
→ Key metrics
→ Problem / risk
→ Decision
→ Plan / roadmap
→ Next actions
```

Recommended variants:

- `boardroom` — enterprise, management, board review
- `minimal` — strategy, finance, data-heavy corporate presentation
- `lagoon` — modern product or technology-company deck
- `soft` — product introduction, onboarding, approachable internal presentation

See [Tahta Guide](./tahta.md).

## Mixed technical and business presentations

Do not switch themes halfway through one deck. Keep one visual language and use the shared addon to add technical depth.

For example, an internal project review can stay on Tahta while using:

```html
<PlotlyGraph src="/latency.json" />
<TrajectoryViewer src="/trajectory.json" />
```

A formal research presentation can stay on Scholarly while using the same Plotly component.

## Default decision rule

```text
Does the audience evaluate research rigor?
    yes → Scholarly
    no
     ↓
Does the audience need substantial technical evidence?
    yes → HEP
    no  → Tahta
```

This rule is a starting point. Audience and desired communication style take precedence over topic labels.
