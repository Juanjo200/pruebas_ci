from main import sum
import pytest


def test_sum():
    assert sum(3, 8) == 11
    print("la funcion trabaja bien")


@pytest.mark.parametrize(
    "in_x,in_y,esperado",
    [(3, 4, 7),
     (sum(2, 1), 4, 7),
     (3, sum(3, 1), 7),
     (3, 4, sum(2, 5)),
     ]
)
def test_sum_param(in_x, in_y, esperado):
    assert sum(in_x, in_y) == esperado


if __name__ == '__main__':
    test_sum()
