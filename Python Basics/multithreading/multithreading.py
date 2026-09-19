#I/0 bound tasks:concurrent execution-improve throughput
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")
def print_letters():
    for letter in 'abcde':
        time.sleep(0.5)
        print(f"letter: {letter}")
        #creating two threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
#starting the threads
t1.start()
t2.start()
#waiting for both threads to complete
t1.join()
t2.join()

t=time.time()
#print_numbers()    
#print_letters()
finished_time=time.time()-t
print(finished_time) 
