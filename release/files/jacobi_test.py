def jacoby_symbol(a: int, n: int) -> int:
    if n < 3 or n % 2 == 0:
        raise ValueError("must be odd integer")
    a = a % n
    g = 1

    while a != 0:
        if a == 1:
            return g
        k = 0
        a1 = a
        while a1 % 2 == 0 and a1 > 0:
            a1 //= 2
            k += 1
        
        s = 1
        if k % 2 != 0:
            n_mod_8 = n % 8
            if n_mod_8 == 3 or n_mod_8 == 5:
                s = -1
        
        if a1 == 1:
            return g * s
        
        if (n % 4) == 3 and (a1 % 4) == 3:
            s = -s
        
        a = n % a1
        g = g * s
    
    return 0