# test = 91, 105, 154 == 7

def ext_euc_gcd(a, b):
    r_prev, r_curr = a, b
    x_prev, x_curr = 1, 0
    y_prev, y_curr = 0, 1

    while r_curr != 0:
        q = r_prev // r_curr
        r_next = r_prev % r_curr

        x_next = x_prev - q * x_curr
        y_next = y_prev - q * y_curr

        r_prev, r_curr = r_curr, r_next
        x_prev, x_curr = x_curr, x_next
        y_prev, y_curr = y_curr, y_next
    
    d, x, y = r_prev, x_prev, y_prev

    return d, x, y

d1, x1, y1 = ext_euc_gcd(105, 91)
d2, x2, y2 = ext_euc_gcd(154, d1)
print(f"GDC(105, 91) = {d1, x1, y1}")
print(f"final GDC(154, 7) = {d2, x2, y2}")