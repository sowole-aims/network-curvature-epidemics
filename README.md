Here’s an updated `README.md` you can paste into your repo:

```markdown
# Network-Based Epidemic Modelling with Forman–Ricci Curvature

This repository contains Python implementations for computing Forman–Ricci Curvature (FRC) on both undirected and directed networks and applying them to epidemic simulations using network-based SIR (Susceptible–Infected–Recovered) models.

## 📁 Repository Structure

```

network_curvature_epidemics/
│
├── frc_lib/
│   ├── **init**.py
│   ├── directed_frc.py            # FRC for directed graphs
│   └── undirected_frc.py          # FRC for undirected graphs
│
├── notebooks/
│   ├── directed_simulations.ipynb         # Simulations & analysis on directed networks
│   ├── undirected_simulations.ipynb       # Simulations & analysis on undirected networks
│   ├── controlled hidden-truth benchmark.ipynb   # Controlled benchmarks with known ground truth
│   ├── public_health_implication.ipynb           # Policy-facing analyses & PH implications
│   └── sensitivity_frc_vs_baselines.ipynb        # Sensitivity & baseline model comparisons
│
└── README.md

````

## 🔧 Requirements

- Python 3.8+
- networkx
- numpy
- matplotlib
- pandas
- scipy
- tqdm

Install dependencies via `pip`:

```bash
pip install networkx numpy matplotlib pandas scipy tqdm
````

> Optional (recommended): create and activate a virtual environment before installing:
>
> ```bash
> python -m venv .venv
> source .venv/bin/activate  # Windows: .venv\Scripts\activate
> ```

## 📊 Project Overview

This project extends classical SIR modeling by integrating a discrete geometric measure—**Forman–Ricci Curvature (FRC)**—to capture local structural heterogeneity in networks. It includes:

* Generation of synthetic networks (Erdős–Rényi, Watts–Strogatz, Barabási–Albert, Power-Law Cluster)
* Computation of node/edge FRC
* SIR simulations with curvature-aware transmission modulation
* Sensitivity analysis vs. classical baselines and controlled ground-truth benchmarks
* Public-health interpretation of findings

## ▶️ Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/sowole-aims/network-curvature-epidemics.git
cd network-curvature-epidemics
```

2. **Launch Jupyter**

```bash
jupyter notebook
```

3. **Run notebooks in `notebooks/`:**

* **`undirected_simulations.ipynb`** – Build undirected graphs, compute FRC, run SIR, visualize (S(t), I(t), R(t)).
* **`directed_simulations.ipynb`** – Directed variants (in/out neighborhoods) with directed FRC and SIR dynamics.
* **`controlled hidden-truth benchmark.ipynb`** – Evaluate methods on synthetic data with known ground truth to verify identifiability and accuracy.
* **`sensitivity_frc_vs_baselines.ipynb`** – Sensitivity studies across ($\beta$,$\gamma$), topology, and comparisons vs. centrality-weighted baselines.
* **`public_health_implication.ipynb`** – Summarize actionable insights (e.g., targeting high-risk substructures) and scenario analyses for policy.

## 🧩 Using the Library

Import FRC utilities directly in your notebooks/scripts:

```python
from frc_lib.undirected_frc import node_frc_undirected, edge_frc_undirected
from frc_lib.directed_frc import node_frc_directed, edge_frc_directed
```

Typical workflow:

1. Construct a NetworkX graph (ER/WS/BA/PLC or your own).
2. Compute FRC (node/edge).
3. Run SIR with curvature-modulated transmission.
4. Plot trajectories and compare metrics (e.g., RMSE, $t_{\text{peak}}$, $R(\infty)$).

## 📦 Reproducibility

* All notebooks are seeded where applicable for reproducible simulations.
* Figures are generated in-notebook; adjust DPI/size in the last plotting cells to match our manuscript needs.

## 🧠 Citation

If you find this code useful, please cite the related manuscript:

**Title:** Analysing Disease Spread on Complex Networks Using Forman–Ricci Curvature
**Authors:** Oladimeji Samuel Sowole, Nicola Luigi Bragazzi, Geminpeter A. Lyakurwa

```bibtex
@article{Sowole2025FRC,
  author  = {Sowole, Oladimeji Samuel and Bragazzi, Nicola Luigi and Lyakurwa, Geminpeter A.},
  title   = {Analysing Disease Spread on Complex Networks Using Forman--Ricci Curvature},
  journal = {Preprint / Manuscript},
  year    = {2025},
  note    = {Under review}
}
```

## 📬 Contact

**Oladimeji Samuel Sowole**
Email: [sowoleo@nm-aist.ac.tz](mailto:sowoleo@nm-aist.ac.tz)

---

**License:** Apache 2.0

