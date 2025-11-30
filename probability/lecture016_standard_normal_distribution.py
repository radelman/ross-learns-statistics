"""https://www.youtube.com/watch?v=X9Pkzaw0SpE&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=16"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def main() -> None:
    mu = 3.4
    sigma = 2.1

    x = np.linspace(-20.0, 20.0, 1000)

    f = (1.0 / np.sqrt(2.0 * np.pi * (sigma ** 2))) * np.exp(-((x - mu) ** 2) / (2.0 * (sigma ** 2)))

    # when scaling a probability distribution up or down along x, you also have to scale down or up along y,
    # respectively, so that the intregral (total probability) remains one
    print(sp.integrate.trapezoid(f, x))
    print(sp.integrate.trapezoid(f * sigma, (x - mu) / sigma))

    fig1 = plt.figure()
    ax1 = fig1.gca()
    ax1.plot(x, f, label=f"N({mu}, {sigma ** 2})")
    ax1.plot((x - mu) / sigma, f * sigma, label="N(0, 1)")
    ax1.set_title(f"To Standard Distribution")
    ax1.set_xlabel("x")
    ax1.set_ylabel("P(X = x)")
    ax1.legend(loc="upper right")

    g = (1.0 / np.sqrt(2.0 * np.pi)) * np.exp(-(x ** 2) / 2.0)

    # same here
    print(sp.integrate.trapezoid(g, x))
    print(sp.integrate.trapezoid(g / sigma, sigma * x + mu))

    fig2 = plt.figure()
    ax2 = fig2.gca()
    ax2.plot(x, g, label="N(0, 1)")
    ax2.plot(sigma * x + mu, g / sigma, label=f"N({mu}, {sigma ** 2})")
    ax2.set_xlim(ax1.get_xlim())
    ax2.set_title(f"From Standard Distribution")
    ax2.set_xlabel("x")
    ax2.set_ylabel("P(X = x)")
    ax2.legend(loc="upper right")

    plt.show(block=True)

if __name__ == "__main__":
    main()
