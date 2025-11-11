from math import gcd


def normalize(frac):
    """
    denominator is always positive
    fraction is reduced to its simplest form
    """
    num, den = frac
    if den == 0:
        raise ValueError("Denominator cannot be zero")
    if den < 0:
        num, den = -num, -den
    divisor = gcd(abs(num), abs(den))
    return [num // divisor, den // divisor]

def add_frac(frac1, frac2):
    n1, d1 = frac1
    n2, d2 = frac2
    num = n1 * d2 + n2 * d1
    den = d1 * d2
    return normalize([num, den])

def sub_frac(frac1, frac2):
    n1, d1 = frac1
    n2, d2 = frac2
    num = n1 * d2 - n2 * d1
    den = d1 * d2
    return normalize([num, den])

def mul_frac(frac1, frac2):
    n1, d1 = frac1
    n2, d2 = frac2
    num = n1 * n2
    den = d1 * d2
    return normalize([num, den])

def div_frac(frac1, frac2):
    n1, d1 = frac1
    n2, d2 = frac2
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by a zero fraction")
    num = n1 * d2
    den = d1 * n2
    return normalize([num, den])

def is_positive(frac):
    num, den = normalize(frac)
    return num > 0

def is_zero(frac):
    num, _ = normalize(frac)
    return num == 0

def cmp_frac(frac1, frac2):
    n1, d1 = normalize(frac1)
    n2, d2 = normalize(frac2)
    left = n1 * d2
    right = n2 * d1
    if left < right:
        return -1
    elif left > right:
        return 1
    else:
        return 0

def frac2float(frac):
    num, den = normalize(frac)
    return num / den
