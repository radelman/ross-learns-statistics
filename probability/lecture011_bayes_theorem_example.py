"""https://www.youtube.com/watch?v=gE6RnZJixUw&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=11"""

from collections.abc import Callable
import math
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.stats import hypergeom

def main() -> None:
    """for the lecture on quality control, i played around with maximum likelihood estimation to estimate the number
    of good objects in a population.  one thing i noticed during that was, the likelihood function looks a lot like a
    probability distribution, but it's not.  in particular, the likelihood function doesn't add up to one like a
    probability distribution does.  so my question was, how do i get a probability distribution of the parameter that
    i'm trying to estimate?  bayes' theorem provides the answer.  in the following examples, i use maximum a
    posteriori estimation to do this
    """

    random.seed()

    # repeated sampling with replacement of a population with good and bad objects

    n = 1000
    g = 800

    Theta = np.arange(n + 1)
    prior = np.ones(n + 1) / (n + 1)
    k = 1
    sample = lambda: hypergeom.rvs(M=n, n=g, N=k)
    forward = lambda h, g: (math.comb(g, h) * math.comb(n - g, k - h)) / math.comb(n, k)
    num_samples = 100

    posteriors = estimate(Theta, prior, sample, forward, num_samples)

    plot_estimate(Theta, posteriors)

    # repeated coin flips

    p = 0.5

    Theta = np.linspace(0.0, 1.0, 100 + 1)
    prior = np.ones(Theta.shape) / Theta.shape
    k = 1
    sample = lambda: sum([1 for i in range(k) if random.random() < p])
    forward = lambda h, p: math.comb(k, h) * (p ** h) * ((1.0 - p) ** (k - h))
    num_samples = 100

    posteriors = estimate(Theta, prior, sample, forward, num_samples)

    plot_estimate(Theta, posteriors)

    plt.show(block=True)

def estimate(
    Theta: np.ndarray, # theta_1, theta_2, ..., theta_n
    prior: np.ndarray, # P(Theta = theta)
    sample: Callable[[], int], # x
    forward: Callable[[float, float], float], # P(X = x | Theta = theta)
    num_samples: int,
) -> list[np.ndarray]:
    posteriors = []

    for i in range(num_samples):
        x = sample()

        P_X_given_Theta = np.array([forward(x, theta) for theta in Theta])

        posterior = P_X_given_Theta * prior
        posterior = posterior / np.sum(posterior)

        posteriors.append(posterior)

        prior = posterior

    return posteriors

def plot_estimate(Theta: np.ndarray, posteriors: list[np.ndarray]) -> None:
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(Theta, posteriors[-1])
    ax.set_title(f"Posterior Distribution After {len(posteriors)} Iterations")
    ax.set_xlabel("theta")
    ax.set_ylabel("P(Theta = theta)")

    fig = plt.figure()
    ax = fig.gca()

    iterations = []
    theta_hats = []
    p01s = []
    p25s = []
    p75s = []
    p99s = []

    for i, posterior in enumerate(posteriors):
        iterations.append(i + 1)

        # the maximum a posteriori estimate is the mode of the posterior distribution
        theta_hat = Theta[np.argmax(posterior)]
        theta_hats.append(theta_hat)

        # percentiles of the posterior distribution
        p01 = Theta[np.argmax(np.cumsum(posterior) >= 0.01)]
        p25 = Theta[np.argmax(np.cumsum(posterior) >= 0.25)]
        p75 = Theta[np.argmax(np.cumsum(posterior) >= 0.75)]
        p99 = Theta[np.argmax(np.cumsum(posterior) >= 0.99)]

        p01s.append(p01)
        p25s.append(p25)
        p75s.append(p75)
        p99s.append(p99)

    ax.plot(iterations, p01s, label="P1")
    ax.plot(iterations, p25s, label="P25")
    ax.plot(iterations, theta_hats, label="MAP Estimate")
    ax.plot(iterations, p75s, label="P75")
    ax.plot(iterations, p99s, label="P99")
    ax.set_xscale("log")
    ax.grid()
    ax.set_title("Posterior Distributions")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("theta")
    ax.legend(loc="lower left")

if __name__ == "__main__":
    main()
