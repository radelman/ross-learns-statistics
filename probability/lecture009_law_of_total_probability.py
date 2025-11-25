"""https://www.youtube.com/watch?v=UzEPJEQF4W0&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=9"""

import random

def main() -> None:
    random.seed()

    num_B = 5

    Omega = [(random.random(), random.randrange(num_B)) for i in range(1000)]

    in_A = lambda omega: omega[0] < 0.5

    A = [omega for omega in Omega if in_A(omega)]

    P_A_1 = len(A) / len(Omega)
    print(f"P(A) = {P_A_1} (via direct calculation)")

    P_A_2 = 0.0
    for i in range(num_B):
        B_i = [omega for omega in Omega if omega[1] == i]
        A_given_B_i = [omega for omega in B_i if in_A(omega)]

        P_A_given_B_i = len(A_given_B_i) / len(B_i)
        P_B_i = len(B_i) / len(Omega)

        P_A_2 = P_A_2 + P_A_given_B_i * P_B_i
    print(f"P(A) = {P_A_2} (via the law of total probability)")

if __name__ == "__main__":
    main()
