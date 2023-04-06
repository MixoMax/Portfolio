import math
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from Primzahlen.py.Primzahltest import is_prime, to_int
from Fibonacci.py.Fibonaccitest import is_fibonacci
from Analyse.Zahlanalyse_functions import *

n = to_int(input("Enter a number: "))

def ascii_table(n:int) -> None:
    print("-"*43)
    
    def print_table_row(name:str, val:bool) -> None:
        if len(str(val) + str(name)) < 41:
            print("|" + name.center(20) + "|" + str(val).center(20) + "|")
        else:
            if len(str(name)) > 20:
                name_rows = [name[i:i+20] for i in range(0, len(name), 20)]
            else:
                name_rows = [name]
            if len(str(val)) > 20:
                val_rows = [str(val)[i:i+20] for i in range(0, len(val), 20)]
            else:
                val_rows = [val]
                
            
            for i in range(max(len(name_rows), len(val_rows))):
                name_str = name_rows[i] if i < len(name_rows) else ""
                val_str = val_rows[i] if i < len(val_rows) else ""
                print("|" + name_str.center(20) + "|" + val_str.center(20) + "|" )
        
    
    print_table_row("Category", "Value")
    print_table_row("Number", n)
    print("-"*43)
    print_table_row("Prime", is_prime(n))
    print_table_row("Fibonacci", is_fibonacci(n))
    print_table_row("Perfect Square", is_square(n))
    print_table_row("Perfect Cube", is_cube(n))
    print_table_row("Divisible by", divisible_by(n))
    print_table_row("Even/Odd", "Even" if n % 2 == 0 else "Odd")
    print_table_row("Sum of Digits", num_sum(n))
    print_table_row("Digital Root", digital_root(n))
    print_table_row("Palindrome", is_palindrome(n))
    
ascii_table(n)