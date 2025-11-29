"""https://www.youtube.com/watch?v=2nDYX8IKrwo&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=12"""

def main() -> None:
    Omega = create_deck_of_cards()

    print(f"Omega = {Omega}")
    print(f"|Omega| = {len(Omega)}")

    A = [omega for omega in Omega if "spade" in omega]
    B = [omega for omega in Omega if "q" in omega]

    print(f"A = {A}")
    print(f"|A| = {len(A)}")

    print(f"B = {B}")
    print(f"|B| = {len(B)}")

    P_A = len(A) / len(Omega)
    P_B = len(B) / len(Omega)

    print(f"P(A) = {P_A}")
    print(f"P(B) = {P_B}")

    A_given_B = [omega for omega in B if "spade" in omega]
    B_given_A = [omega for omega in A if "q" in omega]

    print(f"A | B = {A_given_B}")
    print(f"|A | B| = {len(A_given_B)}")

    print(f"B | A = {B_given_A}")
    print(f"|B | A| = {len(B_given_A)}")

    P_A_given_B = len(A_given_B) / len(B)
    P_B_given_A = len(B_given_A) / len(A)

    print(f"P(A | B) = {P_A_given_B}")
    print(f"P(B | A) = {P_B_given_A}")

def create_deck_of_cards() -> set[str]:
    return {
        f"{rank} of {suit}"
        for suit in [
            "clubs (black)",
            "diamonds (red)",
            "hearts (red)",
            "spades (black)",
        ]
        for rank in [str(i) for i in range(2, 10 + 1)] + ["j", "q", "k", "a"]
    }

if __name__ == "__main__":
    main()
