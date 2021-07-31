import pytest

from collatz import collatz

@pytest.mark.parametrize(
    'i',
    [-2, -1, 0]
)
def test_collatz_bad_value(i: int) -> None:
    with pytest.raises(ValueError):
        collatz(i)

@pytest.mark.parametrize(
    'i, expected',
    [
        (1, 0),
        (2, 1),
        (3, 7),
        (4, 2),
        (5, 5),
        (6, 8),
        (7, 16),
        (8, 3),
        (9, 19),
        (10, 6),
    ]
)
def test_collatz(i: int, expected: int) -> None:
    assert collatz(i) == expected
