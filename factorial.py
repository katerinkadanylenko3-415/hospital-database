def factorial(n):
    if not isinstance(n, int):
        raise ValueError

    if n < 0:
        raise ValueError

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

