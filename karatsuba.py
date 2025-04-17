def karatsuba(x: int, y: int) -> int:
    
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    a = x // 10**m
    b = x % 10**m
    
    c = y // 10**m
    d = y % 10**m
    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = karatsuba(a + b, c + d)

    ad_bc = ab_cd - ac - bd
    result = ac * 10**(2 * m) + ad_bc * 10**m + bd

    return result