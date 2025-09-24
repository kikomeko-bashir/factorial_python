# Factorial solution
# Pair:kikomeko Bashir Musa & Arinda Josephine

def factorial(n: int) -> int:
    """Return factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
