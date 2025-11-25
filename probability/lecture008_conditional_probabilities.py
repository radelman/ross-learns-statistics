"""https://www.youtube.com/watch?v=KjdS_o5HNII&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=8"""

from collections.abc import Callable
import itertools

def main() -> None:
    simulate_dice_rolls()
    simulate_card_deals()

def simulate_dice_rolls() -> None:
    Omega = set(itertools.product(range(1, 6 + 1), repeat=2))

    in_A = lambda omega: omega[0] == 3
    in_B = lambda omega: omega[1] == 5
    in_C = lambda omega: sum(omega) == 6

    simulate_A_given_B(Omega, in_A, in_B)
    simulate_A_given_B(Omega, in_A, in_C)

def simulate_card_deals() -> None:
    Omega = {
        f"{
            "ace" if x == 1
            else "king" if x == 13
            else "queen" if x == 12
            else "jack" if x == 11
            else x
        } of {y}"
        for x in range(1, 13 + 1)
        for y in [
            "clubs (black)",
            "diamonds (red)",
            "hearts (red)",
            "spades (black)",
        ]
    }

    in_A = lambda omega: "spades" in omega
    in_B = lambda omega: "black" in omega
    in_C = lambda omega: "red" in omega

    simulate_A_given_B(Omega, in_A, in_B)
    simulate_A_given_B(Omega, in_A, in_C)

def simulate_A_given_B[T](Omega: set[T], in_A: Callable[[T], bool], in_B: Callable[[T], bool]) -> None:
    print(f"Omega = {Omega}")
    print(f"|Omega| = {len(Omega)}")

    A = {omega for omega in Omega if in_A(omega)}
    B = {omega for omega in Omega if in_B(omega)}
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"|A| = {len(A)}")
    print(f"|B| = {len(B)}")

    P_A = len(A) / len(Omega)
    P_B = len(B) / len(Omega)
    print(f"P(A) = {P_A}")
    print(f"P(B) = {P_B}")

    A_given_B = {omega for omega in B if in_A(omega)}
    print(f"A | B = {A_given_B}")
    print(f"|A | B| = {len(A_given_B)}")

    P_A_given_B_1 = len(A_given_B) / len(B)
    print(f"P(A | B) = {P_A_given_B_1} (via direct calculation)")

    A_intersect_B = A & B
    print(f"A intersect B = {A_intersect_B}")
    print(f"|A intersect B| = {len(A_intersect_B)}")

    P_A_intersect_B = len(A_intersect_B) / len(Omega)
    print(f"P(A intersect B) = {P_A_intersect_B}")

    P_A_given_B_2 = P_A_intersect_B / P_B
    print(f"P(A | B) = {P_A_given_B_2} (via conditional probability)")

if __name__ == "__main__":
    main()
