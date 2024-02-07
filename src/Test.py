# #! TEST CODE UNITAIRE 

import pytest

def addition(a, b):
    return a + b

def test_addition_with_positive_numbers():
    result = addition(3, 5)
    assert result == 8

def test_addition_with_negative_numbers():
    result = addition(-3, -5)
    assert result == -8

def test_addition_with_mixed_numbers():
    result = addition(3, -5)
    assert result == -2

def test_addition_with_zero():
    result = addition(0, 0)
    assert result == 0
    
# # #! TEST CODE SUITE DE FIBONNACCI

import pytest

def fibonacci(n):
    if n <= 0:
        raise ValueError("N doit être un entier positif pour calculer la suite de Fibonacci.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def test_fibonacci_with_positive_integer():
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5

def test_fibonacci_with_invalid_input():
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci(-10)

# #! TEST NOMBREs premiers Jumeaux

import pytest

def est_premier(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def test_est_premier():
    assert est_premier(2) == True
    assert est_premier(3) == True
    assert est_premier(5) == True
    assert est_premier(7) == True
    assert est_premier(11) == True
    assert est_premier(5) == False
    assert est_premier(6) == False
    assert est_premier(9) == False
    assert est_premier(15) == False
    assert est_premier(25) == False

def nombres_premiers_jumeaux(limite):
    paires = []
    for i in range(2, limite):
        if est_premier(i) and est_premier(i + 2):
            paires.append((i, i + 2))
    return paires

def test_nombres_premiers_jumeaux():
    paires_attendues = [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109), (137, 139), (149, 151), (179, 181), (191, 193), (197, 199), (227, 229), (239, 241), (269, 271), (281, 283), (311, 313), (347, 349), (419, 421), (431, 433), (461, 463), (521, 523), (569, 571), (599, 601), (617, 619), (641, 643), (659, 661), (809, 811), (821, 823), (827, 829), (857, 859), (881, 883)]
    assert nombres_premiers_jumeaux(1000) == paires_attendues

if __name__ == '__main__':
    pytest.main()


# #! 