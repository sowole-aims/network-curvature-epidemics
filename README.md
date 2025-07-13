
# Network-Based Epidemic Modelling with Forman-Ricci Curvature

This repository contains Python implementations for computing Forman-Ricci Curvature (FRC) on both undirected and directed networks and applying them to epidemic simulations using the Networked-based SIR (Susceptible-Infected-Recovered) model.

## 📁 Repository Structure

```
network_curvature_epidemics/
│
├── frc_lib/
│   ├── __init__.py
│   ├── directed_frc.py       # FRC computation for directed networks (graphs)
│   └── undirected_frc.py         # FRC computation for undirected graphs
│
├── notebooks/
│   ├── directed_simulations.ipynb   # Simulations and analysis on directed networks
│   └── undirected_simulations.ipynb     # Simulations and analysis on undirected networks
│
└── README.md
```

## 🔧 Requirements

- Python 3.8+
- NetworkX
- NumPy
- Matplotlib
- Pandas
- scipy
- tqdm

Install dependencies via pip:

```bash
pip install networkx numpy matplotlib pandas scipy tqdm 
```

## 📊 Project Overview

This project extends classical SIR modeling by integrating a discrete geometric measure — Forman-Ricci Curvature — to capture local structural heterogeneity in networks. It involves:

- Generating synthetic networks (Erdős–Rényi, Watts–Strogatz, Barabási–Albert, Power-Law Cluster)
- Computing FRC values for nodes and edges
- Simulating SIR dynamics with curvature-based transmission modulation
- Visualizing and analyzing the impact of curvature on epidemic spread

## 📁 How to Use

1. Clone the repository:
```bash
git clone https://github.com/your-username/frc_epidemic_modeling.git
cd frc_epidemic_modeling
```

2. Launch Jupyter Notebook:
```bash
jupyter notebook
```

3. Open and run the notebooks inside the `notebooks/` folder.

## 🧠 Citation

If you find this work useful, please cite our related manuscript:

**Title:** Analysing Disease Spread on Complex Networks Using Forman-Ricci Curvature  
**Authors:** Oladimeji Samuel Sowole, Nicola Luigi Bragazzi, Geminpeter A. Lyakurwa

## 📬 Contact

For any inquiries or collaboration, feel free to reach out:

**Oladimeji Samuel Sowole**  
Email: sowoleo@nm-aist.ac.tz

---

**License:** Apache 2.0
