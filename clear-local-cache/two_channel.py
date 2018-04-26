# A -> B -> A -> B -> A -> B -> B -> A -> A
# A -> A -> A -> B -> B -> B -> C -> C -> C
import os
import time
import json
from multiprocessing import Process

def workerA():
    B = []
    start_time = time.time()
    for _ in range(10):
        os.system("hey -c 5 -n 80 http://192.168.99.100:31998/fission-function/randomtag")
        B.append(time.time()-start_time)
        start_time = time.time()
    res = {}
    res["frontpage_raw"] = B
    res["frontpage"] = sum(res["frontpage_raw"]) / len(res["frontpage_raw"])
    with open('parallel.txt', 'a') as outfile:
        json.dump(res, outfile)
    
def workerB():
    C = []
    start_time = time.time()
    for _ in range(10):
        os.system("hey -c 5 -n 80 http://192.168.99.100:31998/fission-function/randomtagnew")
        C.append(time.time()-start_time)
        start_time = time.time()
    res = {}
    res["sizepage_raw"] = C
    res["sizepage"] = sum(res["sizepage_raw"]) / len(res["sizepage_raw"])
    with open('parallel.txt', 'a') as outfile:
        json.dump(res, outfile)

def main():
    start_time = time.time()
    A = []
    for _ in range(10):
        os.system("hey -c 10 -n 80 http://192.168.99.100:31998/fission-function/randomtag")
        A.append(time.time()-start_time)
        start_time = time.time()

    for _ in range(10):
        os.system("hey -c 10 -n 80 http://192.168.99.100:31998/fission-function/randomtagnew")
        A.append(time.time()-start_time)
        start_time = time.time()

    # Data aggregate
    res_serilize = {}
    res_serilize["frontpage_raw"] = A[0:10]
    res_serilize["sizepage_raw"] = A[10:20]
    res_serilize["frontpage"] = sum(res_serilize["frontpage_raw"]) / len(res_serilize["frontpage_raw"])
    res_serilize["sizepage"] = sum(res_serilize["sizepage_raw"]) / len(res_serilize["sizepage_raw"])
    
    with open('serilize.txt', 'w') as outfile:
        json.dump(res_serilize, outfile)
    
    # Parallel runnning process
    t = Process(target=workerA)
    t.start()

    d = Process(target=workerB)
    d.start()

    t.join()
    d.join()

main()