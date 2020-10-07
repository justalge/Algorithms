def factorize(n):  # O(n**0.5)
    mults = []
    powers = []
    for mult in range(2, int(n**0.5)+1):
        i = 0
        while n % mult == 0:
            if i == 0:
                mults += [mult]
            n //= mult
            i += 1
        else:
            if i != 0:
                powers += [i]

    # if one prime is left (example: for n = 6)
    if n != 1 and len(mults) != 0:
        mults += [n]
        powers += [1]

    # if n is prime:
    if len(mults) == 0:
        mults += [n]
        powers += [1]

    return mults, powers


def euler(n: int) -> int:
    """
    Euler function. Gets natural number n > 0.
    O(n**0.5)
    """

    assert n > 0, "Your input is not natural number"

    if n == 1:
        return 1

    result = n
    mults, _ = factorize(n)
    denominator = 1
    for p in mults:
        result *= (p - 1)
        denominator *= p
    result = int(result / denominator)
    return result


if __name__ == '__main__':
    n = int(input())
    print(euler(n))
