"""https://www.youtube.com/watch?v=4T3aOIfNdTY&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=2"""

def main() -> None:
    simulate_coin_flips()
    simulate_dice_rolls()

def simulate_coin_flips() -> None:
    n_flips = 2

    Omega = [""]
    for i in range(n_flips):
        Omega = [previous_events + next_event for previous_events in Omega for next_event in ["h", "t"]]

    print(f"Omega = {Omega}")

    A = [events for events in Omega if "h" in events]
    B = [events for events in Omega if "h" not in events]

    print(f"A = {A}")
    print(f"B = {B}")

    # probability that there was at least one heads
    P_A = len(A) / len(Omega)

    # probability that there were no heads
    P_B = len(B) / len(Omega)

    print(f"P(A) = {P_A}")
    print(f"P(B) = {P_B}")

    if n_flips == 2:
        assert P_A == 3 / 4

    assert P_A + P_B == 1.0

def simulate_dice_rolls() -> None:
    n_rolls = 2

    Omega = [""]
    for i in range(n_rolls):
        Omega = [previous_events + next_event for previous_events in Omega for next_event in ["1", "2", "3", "4", "5", "6"]]

    print(f"Omega = {Omega}")

    A = [events for events in Omega if "5" in events]
    B = [events for events in Omega if "5" not in events]

    print(f"A = {A}")
    print(f"B = {B}")

    # probability that there was at least one 5
    P_A = len(A) / len(Omega)

    # probability that there were no 5s
    P_B = len(B) / len(Omega)

    print(f"P(A) = {P_A}")
    print(f"P(B) = {P_B}")

    if n_rolls == 2:
        assert P_A == 11 / 36

    assert P_A + P_B == 1.0

if __name__ == "__main__":
    main()
