from functools import cache

@cache
def collatz(i: int) -> int:
    """
    Given i, return how many additional collatz terms of i are needed to reach 1.
    """
    if i < 1:
        raise ValueError("i must be >= 1")

    if i == 1:
        return 0

    if i % 2 == 0:
        next_term = i // 2
    else:
        next_term = 3 * i + 1

    return 1 + collatz(next_term)
