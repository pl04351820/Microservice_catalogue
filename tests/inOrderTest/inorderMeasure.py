# A -> B -> C -> A -> B -> C -> A -> B -> C
# A -> A -> A -> B -> B -> B -> C -> C -> C
import os
import time
import json
from multiprocessing import Process

def workerA():
    B = []
    start_time = time.time()
    for _ in range(10):
        os.system("hey -c 5 -n 75 http://192.168.99.100:31486/fission-function/frontpage")
        B.append(time.time()-start_time)
        start_time = time.time()
    res ={}
    res["frontpage_raw"] = B
    res["frontpage"] = sum(res["frontpage_raw"]) / len(res["frontpage_raw"])
    with open('parallel.txt', 'a') as outfile:
        json.dump(res, outfile)
    
def workerB():
    C = []
    start_time = time.time()
    for _ in range(10):
        os.system("hey -c 5 -n 75 http://192.168.99.100:31486/fission-function/sizepage")
        C.append(time.time()-start_time)
        start_time = time.time()
    res ={}
    res["sizepage_raw"] = C
    res["sizepage"] = sum(res["sizepage_raw"]) / len(res["sizepage_raw"])
    with open('parallel.txt', 'a') as outfile:
        json.dump(res, outfile)

def workerC():
    D = []
    start_time = time.time()
    for _ in range(10):
        os.system("hey -c 5 -n 75 http://192.168.99.100:31486/fission-function/tagpage")
        D.append(time.time()-start_time)
        start_time = time.time()
    res ={}
    res["tagpage_raw"] = D
    res["tagpage"] = sum(res["tagpage_raw"]) / len(res["tagpage_raw"])
    with open('parallel.txt', 'a') as outfile:
        json.dump(res, outfile)
    # print(D)

def main():
    start_time = time.time()
    A = []
    for _ in range(10):
        os.system("hey -c 15 -n 75 http://192.168.99.100:31486/fission-function/frontpage")
        A.append(time.time()-start_time)
        start_time = time.time()

    for _ in range(10):
        os.system("hey -c 15 -n 75 http://192.168.99.100:31486/fission-function/sizepage")
        A.append(time.time()-start_time)
        start_time = time.time()
    
    for _ in range(10):
        os.system("hey -c 15 -n 75 http://192.168.99.100:31486/fission-function/tagpage")
        A.append(time.time()-start_time)
        start_time = time.time()

    # Data aggregate
    res_serilize = {}
    res_serilize["frontpage_raw"] = A[0:10]
    res_serilize["sizepage_raw"] = A[10:20]
    res_serilize["tagpage_raw"] = A[20:30]
    res_serilize["frontpage"] = sum(res_serilize["frontpage_raw"]) / len(res_serilize["frontpage_raw"])
    res_serilize["sizepage"] = sum(res_serilize["sizepage_raw"]) / len(res_serilize["sizepage_raw"])
    res_serilize["tagpage"] = sum(res_serilize["tagpage_raw"]) / len(res_serilize["tagpage_raw"])
    
    with open('serilize.txt', 'w') as outfile:
        json.dump(res_serilize, outfile)
    
    # Parallel runnning process
    t = Process(target=workerA)
    t.start()

    d = Process(target=workerB)
    d.start()

    k = Process(target=workerC)
    k.start()

    t.join()
    d.join()
    k.join()

main()