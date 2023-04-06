import math

def is_square(n:int) -> bool:
    return math.sqrt(n) % 1 == 0

def is_cube(n:int) -> bool:
    return n ** (1/3) % 1 == 0

def divisible_by(n:int) -> list or bool:
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 2:
        return False
    else:
        return divisors

def num_sum(n:int) -> int:
    return sum([int(i) for i in str(n)])

def digital_root(n:int) -> int:
    return n if n < 10 else digital_root(num_sum(n))

def is_palindrome(n:int) -> bool:
    return str(n) == str(n)[::-1]