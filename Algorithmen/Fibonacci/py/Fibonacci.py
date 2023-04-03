import matplotlib.pyplot as plt
import time

def fibonacci(n:int, m:int, iterations:int, verbose:bool=True) -> list:
    
    f = [n, m]
    
    for i in range(iterations):
        n, m = m, n + m
        f.append(m)
        if verbose:
            print(m)
    
    return f

def plot_fibonacci(f:list) -> None:
    fig, ax = plt.subplots()
    
    ax.plot(f)
    ax.set_xlabel("n")
    ax.set_ylabel("F(n)")
    
    plt.show()

def main() -> None:
    n = input("Enter the first number: ")
    try:
        n = int(n)
    except ValueError:
        n = 0
    
    m = input("Enter the second number: ")
    try:
        m = int(m)
    except ValueError:
        m = 1
    
    iterations = input("Enter the number of iterations: ")
    try:
        iterations = int(iterations)
    except ValueError:
        iterations = 25
    
    plot = input("Do you want to plot the fibonacci sequence? (y/n): ")
    
    
    if plot in ["y", "yes", "j", "ja", "true", "t", "1"]:
        plot = True
    else:
        plot = False
    
    if not plot:
        verbose = input("Do you want to print the fibonacci sequence? (y/n): ")
        
        if verbose in ["y", "yes", "j", "ja", "true", "t", "1"]:
            verbose = True
        else:
            verbose = False
    else:
        verbose = False
        
    t1 = time.time()
    
    f = fibonacci(n, m, iterations, verbose)
    
    if plot:
        plot_fibonacci(f)
    
    t2 = time.time()
    
    time_elapsed = int((t2 - t1) * 1000)
    
    print("Time elapsed: " + str(time_elapsed) + "ms")
    if plot:
        print("Time with plotting should not be taken as a performance measurement.")

if __name__ == "__main__":
    main()