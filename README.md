# Drift-Diffusion-Model-DDM-Simulation

This project implements a basic Drift Diffusion Model (DDM) to simulate
binary decision-making processes. The model generates reaction times and
decisions by simulating noisy evidence accumulation toward decision boundaries.

The implementation is intentionally minimal and transparent, designed as
a conceptual and computational introduction to DDMs commonly used in
computational cognitive neuroscience.

## Model Overview

The Drift Diffusion Model describes decision-making as a stochastic process:

- Evidence accumulates over time
- A constant drift rate biases accumulation toward one choice
- Gaussian noise introduces trial-to-trial variability
- Decisions are made when evidence reaches one of two boundaries
- Trials that do not reach a boundary within a fixed time are marked as timeouts

## Features

- Binary decisions (+1 / -1)
- Reaction time distributions
- Explicit timeout handling
- Separate visualization of:
    - Positive decisions
    - Negative decisions
    - Timeouts
- Easily adjustable parameters:
    - Drift
    - Noise
    - Boundary height
    - Bias
    - Maximum decision time

## Requirements

- Python 3.10+
- NumPy
- Matplotlib

Install dependencies with:
```bash
pip install numpy matplotlib