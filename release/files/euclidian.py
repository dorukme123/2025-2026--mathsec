def euclidean_gcd(a, b):
    r_prev, r_curr = a, b
    # prev = a, curr = b

    while r_curr != 0:
        r_next = r_prev % r_curr
        r_prev = r_curr
        r_curr = r_next
    
    d = r_prev
    
    return d

vala = 12345
valb = [24690, 54321, 12541]
for val in valb:
    print(f"GCD({vala}, {val}) = {euclidean_gcd(vala, val)}")