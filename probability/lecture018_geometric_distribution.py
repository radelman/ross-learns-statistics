"""https://www.youtube.com/watch?v=0lpOeU6JZZw&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=18"""

import matplotlib.pyplot as plt
import numpy as np

def main() -> None:
    plot_geometric_distribution(0.1, 10, 1000)
    plot_geometric_distribution(0.1, 10, 10000)
    plot_geometric_distribution(0.1, 10, 100000)

    plot_geometric_distribution(0.3, 10, 1000)
    plot_geometric_distribution(0.5, 10, 1000)

    plt.show(block=True)

def plot_geometric_distribution(p: float, n: int, num_samples: int) -> None:
    k = np.arange(1, n + 1)
    f = ((1.0 - p) ** (k - 1)) * p

    # in a sample of n trials, it's possible that none succeeded.  in this case, the first success would've happened
    # on or after the (n + 1)th trial.  label these samples as such
    samples = [np.random.random(n) < p for _ in range(num_samples)]
    samples = [np.argmax(sample) + 1 if True in sample else n + 1 for sample in samples]

    fig = plt.figure()
    ax = fig.gca()
    ax.hist(samples, bins=np.linspace(1 - 0.5, n + 1 + 0.5, n + 2), density=True, label=f"Histogram of {num_samples} Samples")
    ax.plot(k, f, marker=".", label="Analytical")
    ax.set_title(f"Geometric Distribution for p = {p}")
    ax.set_xlabel("k")
    ax.set_ylabel("P(K = k)")
    ax.legend(loc="upper right")

if __name__ == "__main__":
    main()
