"""https://www.youtube.com/watch?v=7vXLH2H6fZw&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=17"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def main() -> None:
    compare_binomial_and_poisson_distributions(100, 0.003)
    compare_binomial_and_poisson_distributions(100, 0.01)
    compare_binomial_and_poisson_distributions(100, 0.03)
    compare_binomial_and_poisson_distributions(100, 0.1)
    compare_binomial_and_poisson_distributions(100, 0.3)

    plt.show(block=True)

def compare_binomial_and_poisson_distributions(n: int, p: float) -> None:
    k = np.arange(n + 1)

    f = sp.special.comb(n, k) * (p ** k) * ((1.0 - p) ** (n - k))

    rate = n * p
    g = ((rate ** k) * np.exp(-rate)) / sp.special.factorial(k)

    fig = plt.figure()
    ax = fig.gca()
    ax.plot(k, f, label="Binomial Distribution")
    ax.plot(k, g, label="Poisson Approximation")
    ax.set_title(f"Binomial Distribution for n = {n} and p = {p}")
    ax.set_xlabel("k")
    ax.set_ylabel("P(K = k)")
    ax.legend(loc="upper right")

if __name__ == "__main__":
    main()
