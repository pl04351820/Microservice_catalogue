import socket 
import threading 
import requests

class Threadspool():
    # Redirect threading pool on python multiple threading model.
    # The communication is based on linux sockets.
    def __init__(self, n, t):
        self.maxsize = n
        self.count = 0
        self.queue = []  # List append operation.
        self.timeout = t    # Record timeout to avoid starve of threads.
        self.lock = threading.Lock()   # Synchronizaiton lock for requests queue.

    def httphandler(self,request_url):
        # Handle HTTP requests 
        pass
    
    def triggle(self):
        # Triggle batch requests when count is maximum value
        pass

def main():
    # Init socket listener configuration.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind("localhost","8000")
    s.listen(5)
    # Init threadpool.

if __name__ == "__main__":
    main()