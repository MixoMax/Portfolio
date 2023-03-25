import time
import math

#boilerplate
max_n = 0
max_count = 0

n = int(input("Enter a number:"))

start_time = time.time()

#calculate
count = 0
i = n
while i != 1:
    if i % 2 == 0:
        i = i / 2
    else:
        i = 3 * i + 1
    count += 1

if count > max_count:
    max_count = count
    max_n = n

#print results
elapsed_time = math.floor((time.time()-start_time)*1000)

print("Starting number:", n)
print("Number of iterations:", max_count)
print("Execution time:", elapsed_time, "ms")