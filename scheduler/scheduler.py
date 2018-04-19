# A -> B -> A -> B -> A -> B
# A -> A -> A -> B -> B -> B
import os
import time
import threading

def workerA():
    B = []
    start_time = time.time()
    for _ in range(10):
        os.system("hey -c 10 -n 20 http://192.168.99.100:30876/fission-function/frontpage")
        B.append(time.time()-start_time)
        start_time = time.time()
    print(B)
    
def workerB():
    C = []
    start_time = time.time()
    for _ in range(10):
        os.system("hey -c 10 -n 20 http://192.168.99.100:30876/fission-function/anotherfrontpage")
        C.append(time.time()-start_time)
        start_time = time.time()
    print(C)

def main():
    start_time = time.time()
    # serilize with container run 10 times and calculate average number.
    # A -> A -> A -> B -> B -> B
    A = []
    for _ in range(10):
        os.system("hey -c 20 -n 200 http://192.168.99.100:30876/fission-function/frontpage")
        A.append(time.time()-start_time)
        start_time = time.time()

    for _ in range(10):
        os.system("hey -c 20 -n 200 http://192.168.99.100:30876/fission-function/anotherfrontpage")
        A.append(time.time()-start_time)
        start_time = time.time()
    print(A)
    
    # Parallel runnning process
    t = threading.Thread(target=workerA)
    t.start()

    d = threading.Thread(target=workerB)
    d.start()

    t.join()
    d.join()

main()