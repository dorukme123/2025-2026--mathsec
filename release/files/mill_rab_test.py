import random

def miller_rabin_test_single(n: int) -> str:
    s = 0
    r = n -1
    while r % 2 == 0:
        s += 1
        r //= 2

    a = random.randint(2, n - 2)
    y = pow(a, r, n)

    if y != 1 and y != n - 1:
        j = 1
        while j <= s - 1 and y != n - 1:
            y = pow(y, 2, n)
            if y == 1:
                return "composite"
            j += 1
        if y != n - 1:
            return "composite"
    return "probably prime"

def run_miller_rabin_test(n: int, t: int) -> str:
    if n < 5:
        return "input must be bigger than or = 5"
    if n % 2 == 0:
        return "composite even"
    
    for _ in range(t):
        if miller_rabin_test_single(n) == "composite":
            return "composite"
    return "probably prime"