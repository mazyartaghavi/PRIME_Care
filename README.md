# PRIME-Care: A Unified Reinforcement Learning and Mathematical Optimization Framework for Personalized Treatment Planning Under Clinical Uncertainty

This repository contains the full implementation of PRIME-Care, a hybrid reinforcement learning (RL) and mathematical optimization framework for safe, robust, and personalized clinical decision-making under uncertainty.

## Features
- Personalized **digital twin** for patient-specific simulation.
- **Bilevel safety-constrained learning** (RL + optimization).
- **Safety MPC layer** for feasibility-preserving control.
- **Uncertainty-aware modeling** using parametric and distributional approaches.
- **Offline RL** with conservative policy improvement.
- Complete evaluation suite: AUC, calibration error, DCA, SHAP interpretability.

## Installation
```bash
pip install -r requirements.txt
