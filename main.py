""" El modulito principal """
import random

def indicar_positividad(n : float|int) -> str:
    """Indica si un número es positivo, negativo o cero

    Args:
        n (float | int): número a evaluar

    Returns:
        str: 'negativo', 'positivo' o 'cero'
    """
    if n  < 0:
        resultado = "negativo"
    elif n > 0:
        resultado = "positivo"
    else:
        resultado = "cero"

    return resultado

def factorial(n : int) -> int:
    """Calcula el factorial de un número

    Args:
        n (int): número a calcular el factial

    Returns:
        int: el factorial de n
    """
    if n == 0:
        return 1
    return n * factorial(n-1)

def tirar_dado_6caras() -> int:
    """Genera un número entre 1 y 6

    Returns:
        int: el número al azar
    """
    return random.randint(1,6)


if __name__ == "__main__":
    pass
