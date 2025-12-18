import math

class BigInt:
    def __init__(self, digits, base=10):
        self.u = digits
        self.b = base
        self.n = len(digits)

    def __repr__(self,):
        return "".join(map(str, self.u))

def add_big_ints(u_list, v_list, b):
    n = max(len(u_list), len(v_list))
    u = [0] * (n - len(u_list)) + u_list
    v = [0] * (n - len(v_list)) + v_list

    w = [0] * (n + 1)
    k = 0

    for j in range(n - 1, -1, -1):
        w[j + 1] = (u[j] + v[j] + k) % b
        k = (u[j] + v[j] + k) // b

    w[0] = k

    if w[0] == 0: w.pop(0)
    return w

def sub_big_ints(u_list, v_list, b):
    n = len(u_list)
    v = [0] * (n - len(v_list)) + v_list

    w = [0] * n
    k = 0

    for j in range(n - 1, -1, -1):
        w[j] = (u_list[j] - v[j] + k) % b
        k = math.floor((u_list[j] - v[j] + k) / b)

    while len(w) > 1 and w[0] == 0: w.pop(0)
    return w

def mul_big_ints(u, v, b):
    n, m = len(u), len(v)
    w = [0] * (m + n)

    for j in range(n - 1, -1, -1):
        if v[j] == 0:
            continue
        k = 0
        for i in range(n - 1, -1, -1):
            t = u[i] * v[j] + w[i + j + 1] + k
            w[i + j + 1] = t % b
            k = t // b
        w[j] = k
    
    while len(w) > 1 and w[0] == 0: w.pop(0)
    return w

def div_big_ints(u_val, v_val, b):
    q = u_val // v_val
    r = u_val % v_val
    return q, r



base = 10
num1 = [9, 9, 9]
num2 = [1, 2, 3]

print(f"Add: {num1=} + {num2=} = {add_big_ints(num1, num2, base)=}")
print(f"Sub: {num1=} - {num2=} = {sub_big_ints(num1, num2, base)=}")
print(f"Mul: {num1=} * {num2=} = {mul_big_ints(num1, num2, base)=}")
print(f"Div: {num1=} / {num2=} = {sub_big_ints(num1, num2, base)=}")