"""https://www.youtube.com/watch?v=Tc6g-Y-l0Rg&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=14"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def main() -> None:
    n = 10
    p = 0.3

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
    plt.show(block=True)

if __name__ == "__main__":
    main()
