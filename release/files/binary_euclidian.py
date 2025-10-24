def binaru_gcd(a, b):
    g = 1

    while a % 2 == 0 and b % 2 == 0:
        a //= 2
        b //= 2
        g *= 2
    
    u, v = a, b

    while u != 0:
        while u % 2 == 0:
            u //= 2
        while v % 2 == 0:
            v //= 2
        if u >= v:
            u = u - v
        else:
            v = v - u

    d = g * v

    return d

vala = 12345
valb = [24690, 54321, 12541]
for val in valb:
    print(f"GCD({vala}, {val}) = {binaru_gcd(vala, val)}")