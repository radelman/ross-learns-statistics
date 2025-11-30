"""https://www.youtube.com/watch?v=Tc6g-Y-l0Rg&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=14"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def main() -> None:
    plot_binomial_distribution(10, 0.3)

    # the mean and variance of a binomial distribution are n * p and n * p * (1 - p), respectively.  this means that
    # the distribution is more narrow when p is closer to zero or one than when it's somewhere in the middle
    plot_binomial_distribution(30, 0.01)
    plot_binomial_distribution(30, 0.1)
    plot_binomial_distribution(30, 0.5)
    plot_binomial_distribution(30, 0.9)
    plot_binomial_distribution(30, 0.99)

    # the distribution also gets more narrow as n increases
    plot_binomial_distribution(10, 0.5)
    plot_binomial_distribution(30, 0.5)
    plot_binomial_distribution(100, 0.5)
    plot_binomial_distribution(300, 0.5)

    plt.show(block=True)

def plot_binomial_distribution(n: int, p: float) -> None:
    k = np.arange(n + 1)
    f = sp.special.comb(n, k) * (p ** k) * ((1.0 - p) ** (n - k))

    num_samples = 1000
    samples = [np.sum(np.random.random(n) < p) for _ in range(num_samples)]

    fig = plt.figure()
    ax = fig.gca()
    ax.hist(samples, bins=np.linspace(-0.5, n + 0.5, n + 2), density=True, label=f"Histogram of {num_samples} Samples")
    ax.plot(k, f, label="Analytical")
    ax.set_title(f"Binomial Distribution for n = {n} and p = {p}")
    ax.set_xlabel("k")
    ax.set_ylabel("P(K = k)")
    ax.legend(loc="upper right")

if __name__ == "__main__":
    main()
