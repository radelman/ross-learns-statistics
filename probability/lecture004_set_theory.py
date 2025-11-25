"""https://www.youtube.com/watch?v=b_ev4Hdzh-U&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=4"""

def main() -> None:
    n_flips = 3

    Omega = {""}
    for i in range(n_flips):
        Omega = {previous_events + next_event for previous_events in Omega for next_event in ["h", "t"]}

    print(f"Omega = {Omega}")

    A = {events for events in Omega if events[0] == "h"}
    B = {events for events in Omega if events[1] == "t"}

    print(f"A = {A}")
    print(f"B = {B}")

    print(f"A union B = {A | B}")
    print(f"A intersect B = {A & B}")
    print(f"not A = {Omega - A}")

if __name__ == "__main__":
    main()
