# ZESTAW 4 - JAKUB PAWLUSEK

# W zadaniach budujemy całe napisy, a nie wyświetlamy po kawałku.
# W przypadku wykrycia błędów (np. nieprawidłowe argumenty) w Pythonie rzucamy wyjątkiem, 
# np. raise ValueError("message"), a nie wypisujemy komunikatów przez print.

# =======================================
# ZADANIE 4.2
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, 
# które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.
# =======================================

def make_ruler(n: int) -> str:
    """Build a measuring ruler string of given length n"""
    if n < 0:
        raise ValueError("Length must be non-negative")
    top = "|"
    for _ in range(n):
        top += "....|"
    bottom = "0"
    for i in range(1, n + 1):
        bottom += str(i).rjust(5)
    return top + "\n" + bottom

def make_grid(rows: int, cols: int) -> str:
    """Build a rectangular grid of given size (rows x cols)"""
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be positive integers")
    horizontal = "+---" * cols + "+\n"
    vertical = "|   " * cols + "|\n"
    result = ""
    for _ in range(rows):
        result += horizontal + vertical
    result += horizontal
    return result

# =======================================
# ZADANIE 4.3
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
# =======================================

def factorial(n: int) -> int:
    """Compute factorial iteratively"""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# =======================================
# ZADANIE 4.4
# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
# =======================================

def fibonacci(n: int) -> int:
    """Compute n-th Fibonacci number iteratively"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# =======================================
# ZADANIE 4.5
# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. 
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
# =======================================

def reverse_section_iterative(L: list, left: int, right: int) -> None:
    """Reverse elements in list L from index left to right (inclusive), in place"""
    if not (0 <= left <= right < len(L)):
        raise ValueError("Invalid index range")
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def reverse_section_recursive(L: list, left: int, right: int) -> None:
    """Recursive version of list section reversal"""
    if not (0 <= left <= right < len(L)):
        raise ValueError("Invalid index range")
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    reverse_section_recursive(L, left + 1, right - 1)


# =======================================
# ZADANIE 4.6
# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, 
# która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, 
# a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
# =======================================

def sum_seq(sequence) -> float:
    """Recursively sum all numbers in a (possibly nested) sequence"""
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        else:
            total += item
    return total

# =======================================
# ZADANIE 4.7
# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, 
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), 
# która zwróci spłaszczoną listę wszystkich elementów sekwencji. 
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
# =======================================

def flatten(sequence) -> list:
    """Recursively flatten a nested sequence into a single list"""
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# ====== TESTS ======
if __name__ == "__main__":
    print(make_ruler(12))
    print(make_grid(2, 4))
    print(factorial(5))         # 120
    print(fibonacci(10))        # 55

    L = [1, 2, 3, 4, 5, 6]
    reverse_section_iterative(L, 1, 4)
    print(L)                    # [1, 5, 4, 3, 2, 6]

    seq = [1, (2, 3), [4, (5, 6, 7)], 8, [9]]
    print(sum_seq(seq))         # 45
    print(flatten(seq))         # [1, 2, 3, 4, 5, 6, 7, 8, 9]