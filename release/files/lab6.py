import math
def f(x, n, constant):
    return (x**2 + constant) % n

def pollard_rho(n, c_start=1, constant=1):
    a = c_start
    b = c_start
    d = 1
    i = 0

    print(f"\n{"i":<5} {"a":<15} {"b":<15} {"GCD(a-b, n)":<15}")
    print("-"*55)

    while d == 1:
        i += 1

        a = f(a, n, constant)
        b = f(f(a, n, constant), n, constant)
        d = math.gcd(abs(a - b), n)
        print(f"{i:<5} {a:<15} {b:<15} {d:<15}")

        if d == n:
            return None
        elif 1 < d < n:
            return d
    return d

if __name__ == "__main__":
    target_n = 1359331
    start_c = 1
    func_constant = 5

    factor = pollard_rho(target_n, c_start=start_c, constant=func_constant)

    if factor:
        other_factor = target_n // factor
        print(f"Verify: {factor} * {other_factor} = {target_n}")