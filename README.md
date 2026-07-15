# 📊 Normal Distribution Calculator

A lightweight, precise, and fast command-line tool to calculate probabilities using the Normal Distribution curve.

## Features

- **Z-Score Calculation:** Automatically standardizes input values based on the provided mean and standard deviation.
- **Left-tail Probability ($P(X < x)$):** Calculates the cumulative probability up to a specific value.
- **Right-tail Probability ($P(X > x)$):** Calculates the probability beyond a specific value.
- **Interval Probability ($P(x_1 < X < x_2)$):** Computes the probability of a value falling between two boundaries.
- **High Precision:** Uses `math.erf()` under the hood via the `statistics` module, avoiding the $Z = 3.62$ limit of traditional static Z-tables.

## Requirements

- Python 3.8 or higher (required for the `statistics.NormalDist` class).
- No external dependencies (pure Python).

## Usage

Clone the repository and run the script directly from your terminal:

```bash
git clone https://github.com/LeonardoCG12/Normal-Distribution-Calculator.git
cd Normal-Distribution-Calculator/
python3 normal_distribution.py
```

### Example

Upon running the script, you will be prompted to enter the Mean ($\mu$) and Standard Deviation ($\sigma$) of your dataset. Then, choose the type of calculation you want to perform.

```plaintext
--- Normal Distribution Calculator ---
Mean: 100
Standard Deviation: 15

Options:
1: Left side (Less than X)
2: Right side (Greater than X)
3: Between (Between X1 and X2)
Option: 3
Left value: 85
Right value: 115

z1 = -1.00, z2 = 1.00
P(x) = 68.27%
```
