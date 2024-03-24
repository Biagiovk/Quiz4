import pytest
from calculadora import adicao, subtracao, multiplicacao, divisao

def test_adicao():
    assert adicao(2, 3) == 5
    assert adicao(-1, 1) == 0
    assert adicao(0, 0) == 0

def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(10, 7) == 3
    assert subtracao(0, 0) == 0

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-1, 5) == -5
    assert multiplicacao(0, 10) == 0

def test_divisao():
    assert divisao(6, 3) == 2
    assert divisao(10, 2) == 5
    assert divisao(0, 5) == 0

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)