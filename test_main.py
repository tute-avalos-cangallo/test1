import pytest
import main

def test_fatorial():
    nf5 = main.factorial(5)
    assert nf5 == 120


def test_dado():
    tirada = main.tirar_dado_6caras()
    assert tirada >= 1 and tirada <= 6

@pytest.mark.parametrize("n", [
    2,
    4.6,
    999,
    36473.1232,
    10.2
])
def test_positividad_pos(n):
    pos = main.indicar_positividad(n)
    assert pos == "positivo"
