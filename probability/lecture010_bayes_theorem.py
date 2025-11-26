"""https://www.youtube.com/watch?v=akClB1J6b28&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=10"""

import matplotlib.pyplot as plt
import numpy as np

def main() -> None:
    """in the problem statement, steve says that the accuracy is 0.99, but then uses that value for the true positive
    rate (TPR).  these values are not the same: TPR = TP / P, whereas accuracy = (TP + TN) / (P + N).  he also uses
    FPR = 1 - TPR, which isn't right either.  in the code below, i state the problem with values for prevalence, TPR,
    and FPR.  i also use this notation:

    A = test positive
    not A = test negative
    B = real positive
    not B = real negative
    """

    prevalence = 0.001
    TPR = 0.99
    FPR = 0.01
    P_A_given_B, P_B_given_A = invert(prevalence, TPR, FPR)
    print(f"P(test positive | real positive) = {P_A_given_B}")
    print(f"P(real positive | test positive) = {P_B_given_A}")

    prevalence = np.logspace(-4.0, 0.0, 1000)
    TPR = 0.99
    FPR = 0.01
    _, P_B_given_A = invert(prevalence, TPR, FPR)
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(prevalence, P_B_given_A)
    ax.set_xscale("log")
    ax.set_title(f"Varying Prevalence, TPR = {TPR}, FPR = {FPR}")
    ax.set_xlabel("Prevalence")
    ax.set_ylabel("P(Real Positive | Test Positive)")

    prevalence = 0.001
    TPR = np.linspace(0.0, 1.0, 1000)
    FPR = 0.01
    _, P_B_given_A = invert(prevalence, TPR, FPR)
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(TPR, P_B_given_A)
    ax.set_title(f"Prevalence = {prevalence}, Varying TPR, FPR = {FPR}")
    ax.set_xlabel("TPR")
    ax.set_ylabel("P(Real Positive | Test Positive)")

    prevalence = 0.001
    TPR = 0.99
    FPR = np.logspace(-4.0, 0.0, 1000)
    _, P_B_given_A = invert(prevalence, TPR, FPR)
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(FPR, P_B_given_A)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(f"Prevalence = {prevalence}, TPR = {TPR}, Varying FPR")
    ax.set_xlabel("FPR")
    ax.set_ylabel("P(Real Positive | Test Positive)")

    plt.show(block=True)

def invert(prevalence: float, TPR: float, FPR: float) -> float:
    P_A = prevalence
    P_A_given_B = TPR
    P_not_A = 1.0 - prevalence
    P_A_given_not_B = FPR

    P_B_given_A = (P_A_given_B * P_A) / (P_A_given_B * P_A + P_A_given_not_B * P_not_A)

    return P_A_given_B, P_B_given_A

if __name__ == "__main__":
    main()
