# NASA Time Series Anomaly Detection

A structured framework for exploring anomaly detection in multivariate time series using the NASA SMAP and MSL telemetry datasets.

The project emphasizes reproducibility, modular analysis, and the evaluation of anomaly detection techniques in a real-world telemetry setting.

## Overview

The SMAP (Soil Moisture Active Passive) and MSL (Mars Science Laboratory) datasets consist of time series collected from various spacecraft sensors. Anomalies are labeled and categorized as either **point** or **contextual**.

This repository is designed to support:

- Data loading and preprocessing
- Statistical analysis and signal inspection
- Anomaly mask generation
- Visual exploration and reporting
- Integration of detection algorithms and evaluation metrics

## Structure

- `data/`: Original and processed datasets (train/test/labels).
- `src/`: Core logic for data processing and modeling.
- `scripts/`: Analysis and visualization utilities.
- `configs/`: YAML or JSON files for experiment configuration.
- `artifacts/`: Optional directory for storing model outputs and metrics.
- `tests/`: Unit tests (if applicable).

## Setup

Install dependencies using [`uv`](https://github.com/astral-sh/uv):

```bash
uv pip install -r requirements.txt
```

## Usage

Run individual scripts via:

```bash
uv run python scripts/<script_name>.py
```

## Data Source

- NASA: Kaggle - Telemetry Data￼
- Reference: Hundman et al., Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding, arXiv:1802.04431
