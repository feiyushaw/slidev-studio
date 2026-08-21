# Tahta Theme Guide

Tahta is the **Business** mode of `slidev-studio`. Use it for internal project reviews, strategy, roadmap, management presentations, product reviews, and enterprise-facing decks.

## Minimal deck

```md
---
theme: tahta
addons:
  - slidev-addon-scientific
themeConfig:
  variant: boardroom
layout: cover
kicker: Internal Review · 2026
title: Planning Platform Review
subtitle: Status, decisions, risks, and next steps
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
```

Inside this repository, use the local addon path `../..` as shown in `examples/business/slides.md`.

## Choose a variant deliberately

Recommended variants:

- `boardroom` — enterprise, management, board review, finance
- `minimal` — strategy, data, finance, restrained corporate decks
- `lagoon` — modern company, product, technology presentations
- `soft` — onboarding, product introduction, approachable internal talks

Default recommendation for internal reviews: `boardroom`.

```yaml
themeConfig:
  variant: boardroom
```

## Prefer native Tahta layouts

Use the layout that matches the content structure instead of creating custom CSS.

### Executive metrics

```yaml
---
layout: stats
kicker: Executive summary
title: Q3 performance
stats:
  - { value: 18, unit: "%", label: quality improvement, tone: good }
  - { value: 3, label: blockers, tone: warn }
---
```

### One decisive number

Use `fact`.

### Before / after

Use `compare`.

### Business or system process

Use `steps` or `diagram`.

### One important conclusion

Use `statement`.

### Chart

Use Tahta's native `chart` layout for normal business charts. Use the shared `PlotlyGraph` only when interaction or Python-generated Plotly configuration is useful.

## Business presentation structure

A common internal review structure is:

```text
Cover
→ Executive summary
→ Current status
→ Key metrics
→ Major issue / risk
→ Evidence
→ Decision required
→ Roadmap
→ Owners / next actions
→ Appendix
```

Technical material should normally be placed after the decision-oriented part of the deck or marked as a deep dive.

## Mixing business and technical evidence

Keep Tahta as the theme. Add technical components only where they support a decision.

```html
<PlotlyGraph src="/latency.json" :height="380" />
```

For an optional technical section:

```yaml
---
layout: default
kicker: Technical appendix
title: Optimization behavior
aside: "technical deep dive"
---
```

Then use:

```html
<TrajectoryViewer src="/trajectory.json" />
```

or:

```md
<EquationBlock title="Objective">

$$
J(\tau)=J_{\mathrm{safety}}+J_{\mathrm{comfort}}+J_{\mathrm{efficiency}}
$$

</EquationBlock>
```

## Branding

Tahta supports a deck-level logo through `themeConfig`. Keep brand customization at the theme/configuration layer instead of modifying shared scientific components.

```yaml
themeConfig:
  variant: boardroom
  logo: /company-logo.svg
```

Use a logo with sufficient contrast for the selected variant.

## Presentation writing rule

For Business mode, prefer this information order:

```text
Result / status
→ consequence
→ evidence
→ decision or action
```

Do not lead with a long derivation or implementation detail unless the audience explicitly needs it.

## Validation

Tahta provides its own deck lint command. Run it before final export when using Tahta-specific layouts:

```bash
npx tahta-lint examples/business/slides.md
```

Then preview and export:

```bash
npm run dev:business
npm run export:business
```

## When not to use Tahta

Use Scholarly when the audience evaluates research rigor and academic structure. Use HEP when most slides are technical experiments, algorithms, simulations, or engineering visualizations.
