"""https://www.youtube.com/watch?v=5mDYZMwTAF8&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=3"""

import itertools
import math

def main():
    # with replacement, order matters
    print(math.prod([52, 52, 52, 52, 52]))
    print(52 ** 5)

    # without replacement, order matters
    print(math.prod([52, 51, 50, 49, 48]))
    print(math.factorial(52) / math.factorial(52 - 5))

    # with replacement, order doesn't matter
    # print(count_via_enumeration(52, 5)) # this is slow
    print(count_via_recursion(52, 5))
    print(count_via_repeated_cumsum(52, 5))
    print(count_via_formula(52, 5))

    # without replacement, order doesn't matter
    print(math.factorial(52) / (math.factorial(52 - 5) * math.factorial(5)))
    print(math.comb(52, 5))

def count_via_enumeration(N: int, k: int) -> int:
    event_space = [event for event in range(1, N + 1)]
    Omega = set([()])
    for i in range(k):
        Omega = [previous_events + (next_event,) for previous_events in Omega for next_event in event_space]
        Omega = set([tuple(sorted(events)) for events in Omega])
    return len(Omega)

def count_via_recursion(N: int, k: int) -> int:
    """count the number of ways to assign n_1, n_2, ..., n_N such that
    n_1 + n_2 + ... + n_N = k
    n_i in [0, 1, ..., k]
    """
    if N == 1 or k == 0:
       return 1
    return sum([count_via_recursion(N - 1, i) for i in range(k + 1)])

def count_via_repeated_cumsum(N: int, k: int) -> int:
    c = (k + 1) * [1]
    for n in range(2, N + 1):
        c = [i for i in itertools.accumulate(c)]
    return c[-1]

def count_via_formula(N: int, k: int) -> int:
    return math.comb(N + k - 1, k)

if __name__ == "__main__":
    main()
