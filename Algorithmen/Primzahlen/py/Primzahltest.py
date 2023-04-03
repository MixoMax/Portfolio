def to_int(x):
    try:
        return int(x)
    except ValueError:
        for char in x:
            if char not in "0123456789.":
                x = x.replace(char, "")
            if x.count(".") > 1:
                x = x.replace(".", "")
            
            return int(x)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
        

n = to_int(input("Primzahl zu testen: "))

print(f"{n} ist eine Primzahl." if is_prime(n) else f"{n} ist keine Primzahl.")
