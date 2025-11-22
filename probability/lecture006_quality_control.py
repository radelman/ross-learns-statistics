"""https://www.youtube.com/watch?v=e7RAK_iQBp0&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=6"""

import math
import matplotlib.pyplot as plt
import numpy as np
import random

def main() -> None:
    """this code uses the following notation, which is a little different than in the lecture:

    n = population size
    g = number of good objects in the population
    b = n - g = number of bad objects in the population

    k = sample size
    h = number of good objects in the sample
    c = k - h = number of bad objects in the sample
    """

    random.seed()

    simulate_sampling(1000, 800, 20, 1000, plot_results=True)
    simulate_maximum_likelihood_estimate(1000, 20, 16, print_results=True, plot_results=True)
    simulate_maximum_likelihood_estimator(1000, 800, 20, 1000, print_results=True, plot_results=True)

    plt.show(block=True)

def simulate_sampling(
    n: int,
    g: int,
    k: int,
    num_samples: int,
    plot_results: bool = False,
) -> list[int]:
    samples = [sample(n, g, k) for i in range(num_samples)]

    if plot_results:
        h = [h for h in range(k + 1)]
        p = [calculate_P(n, g, k, h) for h in h]

        fig = plt.figure()
        ax = fig.gca()
        ax.hist(samples, bins=[x - 0.5 for x in range(k + 2)], density=True, label=f"Numerical ({num_samples} Samples)")
        ax.plot(h, p, marker=".", label="Analytical")
        ax.set_title(f"P(H | n = {n}, g = {g}, k = {k})")
        ax.set_xlabel("h")
        ax.set_ylabel("P(H = h)")
        ax.legend(loc="upper left")

    return samples

def simulate_maximum_likelihood_estimate(
    n: int,
    k: int,
    h: int,
    print_results: bool = False,
    plot_results: bool = False,
) -> float:
    g = [g for g in range(n + 1)]
    l = [calculate_P(n, g, k, h) for g in g]

    l_max = max(l)
    g_hat = g[l.index(l_max)]

    if print_results:
        print(l_max)
        print(g_hat)

    if plot_results:
        fig = plt.figure()
        ax = fig.gca()
        ax.plot(g, l, label="Likelihood")
        ax.set_xlim(ax.get_xlim())
        ax.set_ylim(ax.get_ylim())
        ax.plot([g_hat, g_hat], [-1.0, l_max], marker=".", label="Maximum Likelihood Estimate")
        ax.set_title(f"L(G | n = {n}, k = {k}, h = {h})")
        ax.set_xlabel("g")
        ax.set_ylabel("L(G = g)")
        ax.legend(loc="upper left")

    return g_hat

def simulate_maximum_likelihood_estimator(
    n: int,
    g: int,
    k: int,
    num_samples: int,
    print_results: bool = False,
    plot_results: bool = False,
) -> dict[str, float]:
    samples = simulate_sampling(n, g, k, num_samples)
    g_hat = [simulate_maximum_likelihood_estimate(n, k, h) for h in samples]

    mean = np.mean(g_hat)
    std = np.std(g_hat)

    if print_results:
        print(mean)
        print(std)

    if plot_results:
        fig = plt.figure()
        ax = fig.gca()
        ax.hist(
            g_hat,
            bins=(n / k) * np.linspace(-0.5, k + 0.5, k + 2),
            density=True,
            label=f"Numerical ({num_samples} Samples)",
        )
        ax.set_title(f"P(G_hat | n = {n}, g = {g}, k = {k})")
        ax.set_xlabel("g_hat")
        ax.set_ylabel("P(G_hat = g_hat)")
        ax.legend(loc="upper left")

    return {
        "mean": mean,
        "std": std,
    }

def sample(
    n: int,
    g: int,
    k: int,
) -> int:
    """from a population with n objects, g of which are good, randomly select k of them.  return the number of good
    objects h in this sample"""

    b = n - g
    objects = g * [True] + b * [False]
    random.shuffle(objects)
    sample = objects[0 : k]
    h = sum([1 for object in sample if object])
    return h

def calculate_P(
    n: int,
    g: int,
    k: int,
    h: int,
) -> float:
    """from a population with n objects, g of which are good, randomly select k of them.  return the probability p
    that h objects in this sample will be good.  this is the hypergeometric distribution
    """

    b = n - g
    c = k - h
    p = (math.comb(g, h) * math.comb(b, c)) / math.comb(n, k)
    return p

if __name__ == "__main__":
    main()
