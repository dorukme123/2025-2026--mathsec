import random
from jacobi_test import jacoby_symbol

def solovay_strassen_test_single(n: int) -> str:
    a = random.randint(2, n - 2)
    r = pow(a, (n - 1) // 2, n)
    
    if r != 1 and r != n - 1:
        return "composite"
    s = jacoby_symbol(a, n)

    if r == (s + n) % n:
        return "probably prime"
    else:
        return "composite"

def run_solovay_strassen_test(n: int, t: int) -> str:
    if n < 5:
        return "input must be bigger than or = 5"
    if n % 2 == 0:
        return "composite even"
    
    for _ in range(t):
        if solovay_strassen_test_single(n) == "composite":
            return "composite"
    return "probably prime"