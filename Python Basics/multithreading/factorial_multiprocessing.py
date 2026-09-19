import multiprocessing
import math
import sys
import time

# Allow very large integers to be printed
sys.set_int_max_str_digits(100000)

# Factorial computation function
def compute_factorial(n):
    print(f'Computing factorial of {n}')
    return math.factorial(n)

if __name__ == '__main__':
    numbers = [100000, 200000, 300000, 400000, 500000]
    start_time = time.time()

    # Create a pool of processes
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the compute_factorial function to the list of numbers
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()
