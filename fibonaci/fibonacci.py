# Fibonacci solution
# Pair: Kikomeko Bashir Musa & Arinda Josephine

def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number.
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
    """
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
