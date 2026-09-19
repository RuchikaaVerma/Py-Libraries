#multiprocessing with processpollexceutor
from concurrent.futures import ProcessPoolExecutor
import time

def print_number(number):
    time.sleep(0.5)
    return f"Number: {number}"

numbers = [1, 2, 3, 4, 5]
if __name__ == "__main__":  # Entry point
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(print_number, numbers))
    for result in results:
        print(result)