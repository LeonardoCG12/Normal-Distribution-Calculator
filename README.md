<div id="top"></div>
<div align="center">
  <h1>CurveSpan</h1>
  <h3>
    Lightweight, Precise, and Fast Command-Line Tool in
    <a href="https://www.python.org">Python</a> :bar_chart:
  </h3>
</div>

<details>
  <summary>
    <strong>Table of Contents</strong>
  </summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#how-it-works">How It Works</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#usage">Usage</a>
      <ul>
        <li><a href="#example">Example</a></li>
      </ul>
    </li>
  </ol>
</details>

---

## About

**CurveSpan** is a lightweight, precise, and fast command-line tool to calculate probabilities using the Normal Distribution curve.

---

## How It Works

- **Input Collection:** The script prompts you to define the statistical properties of your dataset: the Mean ($\mu$) and Standard Deviation ($\sigma$).

- **Z-Score Standardization:** Based on your chosen boundaries ($x$ or $x_1, x_2$), it calculates the corresponding Z-scores to measure how many standard deviations your values lie from the mean:

$$
Z = \frac{x - \mu}{\sigma}
$$

- **Probability Integration:** Instead of reading from a static, truncated Z-table, the program calculates the area under the curve using the mathematical error function (`math.erf()`) via Python's native `statistics.NormalDist` class. This enables high-precision integration for any arbitrary Z-score:

$$
\Phi(z) = \frac{1}{2} \left[ 1 + \text{erf}\left( \frac{z}{\sqrt{2}} \right) \right]
$$

- **Formatting:** The tool translates the raw decimal probability into a clean, human-readable percentage output (e.g., `68.27%`).

---

## Features

- **Z-Score Calculation:** Automatically standardizes input values based on the provided mean and standard deviation.
- **Left-tail Probability ($`P(X < x)`$):** Calculates the cumulative probability up to a specific value.
- **Right-tail Probability ($`P(X > x)`$):** Calculates the probability beyond a specific value.
- **Interval Probability ($`P(x_1 < X < x_2)`$):** Computes the probability of a value falling between two boundaries.
- **High Precision:** Uses `math.erf()` under the hood via the `statistics` module, avoiding the $`Z = 3.62`$ limit of traditional static Z-tables.

## Requirements

- Python 3.8 or higher (required for the `statistics.NormalDist` class).
- No external dependencies (pure Python).

## Usage

Clone the repository and run the script directly from your terminal:

```bash
git clone https://github.com/LeonardoCG12/CurveSpan.git
cd CurveSpan
python3 curve_span.py
```

### Example

Upon running the script, you will be prompted to enter the Mean ($\mu$) and Standard Deviation ($\sigma$) of your dataset. Then, choose the type of calculation you want to perform.

```plaintext
------ CurveSpan ------
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

<p align="right">[<a href="#top">Back to top</a>]</p>
