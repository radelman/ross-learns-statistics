"""https://www.youtube.com/watch?v=b_ev4Hdzh-U&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=4"""

def main():
    n_flips = 3

    Omega = set([""])
    for i in range(n_flips):
        Omega = set([previous_events + next_event for previous_events in Omega for next_event in ["h", "t"]])

    print(f"Omega = {Omega}")

    A = set([events for events in Omega if events[0] == "h"])
    B = set([events for events in Omega if events[1] == "t"])

    print(f"A = {A}")
    print(f"B = {B}")

    print(f"A union B = {A | B}")
    print(f"A intersect B = {A & B}")
    print(f"not A = {Omega - A}")

if __name__ == "__main__":
    main()
