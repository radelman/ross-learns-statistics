"""https://www.youtube.com/watch?v=m7hI2LulMxE&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=5"""

import itertools
import matplotlib.pyplot as plt
import operator
import random

def main() -> None:
    n = range(1, 50 + 1)

    p = [(365 - i + 1) / 365 for i in n]
    p = [1.0 - x for x in itertools.accumulate(p, operator.mul)]

    q = []
    for i in n:
        Omega = [[random.randrange(0, 365) for j in range(i)] for k in range(1000)]
        A = [omega for omega in Omega if len(set(omega)) < len(omega)]
        P_A = len(A) / len(Omega)
        q.append(P_A)

    fig = plt.figure()
    ax = fig.gca()
    ax.plot(n, p, c="#000000", label="Analytical")
    ax.plot(n, q, c="#FF0000", label="Numerical")
    ax.set_title("Birthday Problem")
    ax.set_xlabel("Number of People in Room")
    ax.set_ylabel("Probability That at Least Two Have Same Birthday")
    ax.legend(loc="lower right")
    plt.show(block=True)

if __name__ == "__main__":
    main()
