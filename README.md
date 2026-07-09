# Optimization Project

## Overview

This project contains solutions for optimization tasks implemented in Python. It includes data preprocessing, exploratory data analysis, optimization algorithms, and machine learning models.

To see the business formalization, final solution and results, run Task1 and Task2 notebooks for the tasks 1 and 2 respectively.

## Project Structure

```text
optimization/
├── data/                  # Input datasets
├── src/                   # Source code
│   ├── data_loader.py     # Data loading script
│   ├── task1/             # Task 1 implementation
│   └── task2/             # Task 2 notebooks and scripts
├── Task1.ipynb            # Task 1 final solution and summary
├── Task2.ipynb            # Task 2 final solution and summary
├── pyproject.toml         # Project configuration and dependencies
├── uv.lock                # Dependency lock file
└── README.md
```

## Requirements

* Python 3.12 or later
* `uv` package manager

If you do not have `uv` installed, install it using:

```bash
pip install uv
```

or

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd optimization
```

### 2. Create a virtual environment

```bash
uv venv
```

### 3. Activate the virtual environment

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install project dependencies

```bash
uv sync
```

This command installs all dependencies specified in `pyproject.toml` and `uv.lock`.

## Running the Project

### Launch Jupyter Notebook

```bash
uv run jupyter lab
```

or

```bash
uv run jupyter notebook
```