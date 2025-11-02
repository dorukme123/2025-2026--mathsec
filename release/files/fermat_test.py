import random

def fermat_test_single(n: int) -> str:
    a = random.randint(2,n-2)
    r = pow(a, n - 1, n)

    if r == 1:
        return "probably prime"
    else:
        return "composite"
    
def run_feramn_test(n: int, t: int) -> str:
    if n < 5:
        return "input must be bigger than or = 5"
    if n % 2 == 0:
        return "composite even"
    
    for _ in range(t):
        if fermat_test_single(n) == "composite":
            return "composite"
    return "probably prime"
