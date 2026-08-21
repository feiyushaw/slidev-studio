# Getting Started

`slidev-studio` provides three presentation modes on top of Slidev:

- **Academic** → Scholarly
- **Technical** → HEP
- **Business** → Tahta

The repository also provides a shared addon with reusable components such as `PlotlyGraph`, `ScientificFigure`, `EquationBlock`, `TrajectoryViewer`, and `OptimizationViewer`.

## 1. Install

Clone the repository and install dependencies:

```bash
git clone https://github.com/feiyushaw/slidev-studio.git
cd slidev-studio
npm install
```

## 2. Preview the built-in templates

```bash
npm run dev:scholarly
npm run dev:hep
npm run dev:business
```

These commands open the three example decks in development mode.

## 3. Start from a template

Use one of the example decks as a starting point:

```text
examples/
├── scholarly/slides.md
├── hep/slides.md
└── business/slides.md
```

Copy the closest example into your own project and replace the content while preserving the first frontmatter block.

## 4. Select a theme

Academic:

```yaml
---
theme: scholarly
addons:
  - slidev-addon-scientific
---
```

Technical:

```yaml
---
theme: hep
addons:
  - slidev-addon-scientific
---
```

Business:

```yaml
---
theme: tahta
addons:
  - slidev-addon-scientific
themeConfig:
  variant: boardroom
---
```

When working inside this repository, the examples reference the addon locally with `../..` instead of the package name.

## 5. Add shared components only when needed

Static scientific figure:

```html
<ScientificFigure
  src="/result.svg"
  caption="Benchmark results under the selected configuration."
/>
```

Interactive Plotly figure:

```html
<PlotlyGraph src="/convergence.json" :height="420" />
```

Equation:

```md
<EquationBlock title="Optimization problem">

$$
\mathbf{u}^{*}=\arg\min_{\mathbf{u}} J(\mathbf{u})
$$

</EquationBlock>
```

Trajectory visualization:

```html
<TrajectoryViewer src="/trajectory.json" />
```

## 6. Export

The repository provides theme-specific export commands:

```bash
npm run export:scholarly
npm run export:hep
npm run export:business
```

For interactive visualizations, verify the exported PDF separately because browser interaction is reduced to a static frame during PDF export.

## 7. Recommended workflow

```text
Choose audience
    ↓
Choose theme
    ↓
Start from closest example deck
    ↓
Use native theme layouts first
    ↓
Add shared addon components where necessary
    ↓
Preview in browser
    ↓
Export and check PDF
```

See [Choosing a Theme](./choosing-a-theme.md) for the decision rules and the theme-specific guides for detailed usage.
