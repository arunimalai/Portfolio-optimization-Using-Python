# Portfolio Optimization Using Python

## Overview

This project applies **Modern Portfolio Theory (MPT)** concepts to analyze and optimize a portfolio of four technology stocks using historical price data.

The project first evaluates an **equal-weighted portfolio** and then uses **10,000 randomly generated portfolio allocations** to explore the risk-return trade-off and identify the portfolio with the **highest Sharpe ratio**.

## Portfolio

The portfolio consists of:

- AMD
- Apple (AAPL)
- Microsoft (MSFT)
- Oracle (ORCL)

Each stock initially receives an equal allocation of **25%** in the equal-weighted portfolio.

## Objectives

- Analyze historical stock-price data
- Calculate normalized stock performance
- Construct an equal-weighted portfolio
- Calculate portfolio value and cumulative return
- Calculate daily portfolio returns
- Measure portfolio volatility
- Calculate the Sharpe ratio
- Generate 10,000 random portfolio allocations
- Calculate expected return and volatility for each portfolio
- Identify the portfolio with the highest Sharpe ratio
- Visualize the risk-return characteristics of the simulated portfolios

## Methodology

### 1. Data Preparation

Historical adjusted closing prices for the four stocks are imported from CSV files stored in the `main/` folder.

### 2. Equal-Weighted Portfolio

Each stock is assigned an initial allocation of 25%. The portfolio is initialized with a value of **$10,000**.

The performance of each stock and the total portfolio value are then calculated over the historical period.

### 3. Portfolio Performance

The project calculates:

- Cumulative portfolio return
- Mean daily return
- Daily return volatility
- Annualized Sharpe ratio

### 4. Portfolio Simulation

The optimization section generates **10,000 random portfolio weight combinations**.

For each portfolio:

- Random weights are generated and normalized to sum to 1
- Annualized expected return is calculated
- Annualized volatility is calculated using the covariance matrix
- Sharpe ratio is calculated

A fixed random seed is used to make the simulation reproducible.

### 5. Portfolio Selection

The portfolio with the **maximum simulated Sharpe ratio** is identified as the optimal portfolio.

The corresponding portfolio weights, expected return, volatility, and Sharpe ratio are extracted.

## Results

The project produces:

- Equal-weighted portfolio performance
- Individual stock performance within the portfolio
- Cumulative portfolio return
- Daily portfolio return statistics
- Annualized Sharpe ratio
- Optimal portfolio weights
- Risk-return distribution of the 10,000 simulated portfolios
- Visualization highlighting the maximum-Sharpe-ratio portfolio

Results and visualizations are stored in the `results/` folder.

## Project Structure

```text
portfolio-optimization/
│
├── README.md
├── portfolio_optimization.py
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── AMD.csv
│   ├── AAPL.csv
│   ├── MSFT.csv
│   └── ORCL.csv
│
└── results/
    ├── portfolio_optimization.png
    ├── optimal_portfolio_weights.csv
    └── portfolio_summary.csv
```

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
cd portfolio-optimization
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python portfolio_optimization.py
```

The CSV files required by the program are included in the `data/` folder, allowing the project to be reproduced on another computer without relying on local file paths.

## Reproducibility

The project uses a fixed random seed for the portfolio simulation. This ensures that the same set of random portfolio allocations can be reproduced when the program is run again using the same input data.

## Future Improvements

Potential extensions to the project include:

- Incorporating a risk-free rate into the Sharpe ratio calculation
- Implementing constrained optimization using `scipy.optimize`
- Comparing maximum-Sharpe and minimum-volatility portfolios
- Adding an out-of-sample backtest
- Comparing optimized portfolio performance against a benchmark
- Incorporating transaction costs
- Extending the analysis to a larger universe of assets
