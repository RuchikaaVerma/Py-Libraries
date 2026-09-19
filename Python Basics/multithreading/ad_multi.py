#multithreading with thread pool excecutor
from concurrent.futures import ThreadPoolExecutor   
import time

def print_number(number):
    time.sleep(0.5)
    return f"Number: {number}"

numbers = [1, 2, 3, 4, 5]
with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(print_number, numbers))
for result in results:
    print(result)    