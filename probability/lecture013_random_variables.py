"""https://www.youtube.com/watch?v=-7QG2itL1u4&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=13"""

import matplotlib.pyplot as plt
import numpy as np

def main() -> None:
    x0 = 3.0
    k = 0.5

    a = -10.0
    b = 20.0
    x = np.linspace(a, b, 1000)
    e = np.exp(-k * (x - x0))
    F = 1.0 / (1.0 + e)
    f = (k * e) / ((1.0 + e) ** 2) # f(x) = F'(x)

    num_samples = 1000
    u = np.random.random(num_samples)
    y = np.interp(u, F, x)

    fig = plt.figure()
    ax = fig.gca()
    ax.hist(y, bins=np.linspace(a, b, 100), density=True, label=f"P(X = x) (Histogram of {num_samples} Samples)")
    ax.plot(x, f, label="P(X = x) (Analytical)")
    ax.plot(x, F, label="P(X <= x) (Analytical)")
    ax.set_title("Logistic Distribution")
    ax.set_xlabel("x")
    ax.legend(loc="upper left")
    plt.show(block=True)

if __name__ == "__main__":
    main()
