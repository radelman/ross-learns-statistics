"""https://www.youtube.com/watch?v=8n1n0OM4gLk&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=15"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def main() -> None:
    compare_binomial_and_normal_distributions(10, 0.003)
    compare_binomial_and_normal_distributions(10, 0.03)
    compare_binomial_and_normal_distributions(10, 0.3)
    compare_binomial_and_normal_distributions(100, 0.3)
    compare_binomial_and_normal_distributions(1000, 0.3)

    plt.show(block=True)

def compare_binomial_and_normal_distributions(n: int, p: float) -> None:
    k = np.arange(n + 1)
    f = sp.special.comb(n, k) * (p ** k) * ((1.0 - p) ** (n - k))

    mu = n * p
    sigma = np.sqrt(n * p * (1.0 - p))
    x = np.linspace(-n / 10.0, n, 100 * n)
    g = (1.0 / np.sqrt(2.0 * np.pi * (sigma ** 2))) * np.exp(-((x - mu) ** 2) / (2.0 * (sigma ** 2)))

    fig = plt.figure()
    ax = fig.gca()
    ax.plot(k, f, label="Binomial Distribution")
    ax.plot(x, g, label="Normal Approximation")
    ax.set_title(f"Binomial Distribution for n = {n} and p = {p}")
    ax.set_xlabel("k")
    ax.set_ylabel("P(K = k)")
    ax.legend(loc="upper right")

if __name__ == "__main__":
    main()
