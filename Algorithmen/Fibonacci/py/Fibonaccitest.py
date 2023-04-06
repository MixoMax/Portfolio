from math import sqrt

def is_fibonacci(i:int) -> bool:
    """Checks if a number is a fibonacci number."""
    
    f = [n, m] = [0, 1]
    
    while f[-1] < i:
        n, m = m, n + m
        f.append(m)
    
    
    return i in f

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(is_fibonacci(n))