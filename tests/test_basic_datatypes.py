import math

import pytest

import tutorial.basic_datatypes as bdt


def reference_addition_multiplication(a: float, b: float, c: float) -> float:
    return (a + b) * c


@pytest.mark.parametrize(
    "a, b, c",
    [
        (1, 2, 3),
        (4, 5, 9),
        (10, 11, 21),
        (-5, 1, 2),
        (23.1, 1.8, 14.2),
        (-10.5, 7.4, 84),
        (1e-5, 3.5e-5, 2.5),
    ],
)
def test_addition_multiplication(
    a: float,
    b: float,
    c: float,
):
    assert math.isclose(
        bdt.solution_addition_multiplication(a, b, c),
        reference_addition_multiplication(a, b, c),
    )
