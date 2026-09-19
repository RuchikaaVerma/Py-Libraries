import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(0.5)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(0.5)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":  # Entry point
    # Creating processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    # Start processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(f"Finished in: {finished_time} seconds")
#ctrl+z,=tab