"""https://www.youtube.com/watch?v=UXB9eeMZfwo&list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V&index=7"""

import itertools
import math

def main() -> None:
    """this lecture is nominally on the binomial and multinomial distributions, but it's really on the binomial and
    multinomial coefficients:
    - https://en.wikipedia.org/wiki/Binomial_theorem
    - https://en.wikipedia.org/wiki/Multinomial_theorem
    however, these coefficients do appear in the corresponding distributions:
    - https://en.wikipedia.org/wiki/Binomial_distribution
    - https://en.wikipedia.org/wiki/Multinomial_distribution

    steve mentions "without replacement" at the start of the lecture.  while the coefficients do model scenarios where
    there isn't replacement, the distributions model scenarios where there **is** replacement.  the "without
    replacement" versions of these distributions are the hypergeometric distribution (which was used in the previous
    lecture) and its multivariate form.  here is a good discussion of the difference:
    - https://en.wikipedia.org/wiki/Hypergeometric_distribution#Multivariate_hypergeometric_distribution
    in summary,
    - 2  groups with    replacement is the binomial distribution
    - 3+ groups with    replacement is the multinomial distribution
    - 2  groups without replacement is the hypergeometric distribution
    - 3+ groups without replacement is the multivariate hypergeometric distribution

    lastly, there are some comments on the lecture video about whether to include an r! in the denominator of the
    expression for the multinomial coefficient.  the answer is yes if the order of the groups doesn't matter and no if
    the order does matter.  for example, when pairing people off, the order of the pairs doesn't matter, so include
    the r!.  on the other hand, when assigning people to committees that do different work, the order does matter, so
    don't include the r!
    """

    sizes = [1, 2, 2, 3]

    n = sum(sizes)
    indices = [0] + list(itertools.accumulate(sizes))

    Omega1 = set()
    Omega2 = set()
    Omega3 = set()

    for permutation in itertools.permutations(range(n)):
        partitions = tuple(permutation[i : j] for i, j in itertools.pairwise(indices))

        omega1 = partitions
        omega2 = tuple(tuple(sorted(partition)) for partition in partitions)
        omega3 = tuple(sorted(tuple(tuple(sorted(partition)) for partition in partitions)))

        Omega1.add(omega1)
        Omega2.add(omega2)
        Omega3.add(omega3)

    print(f"Omega1 = {Omega1}")
    print(f"Omega2 = {Omega2}")
    print(f"Omega3 = {Omega3}")

    print(len(Omega1))
    print(math.factorial(n))

    print(len(Omega2))
    print(math.factorial(n) / math.prod([math.factorial(size) for size in sizes]))

    print(len(Omega3))
    num_groups_by_size = {}
    for size in sizes:
        num_groups_by_size[size] = num_groups_by_size.get(size, 0) + 1
    print(math.factorial(n) / (math.prod([math.factorial(size) for size in sizes]) * math.prod([math.factorial(num_groups) for num_groups in num_groups_by_size.values()])))

if __name__ == "__main__":
    main()
