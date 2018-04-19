# This script will triggle multiple serverless function in serilized order.
import requests
import time
def main():
    r = requests.get('http://192.168.99.100:30876/fission-function/frontpage')
    print(r.text)
    if r.text:
        r = requests.get('http://192.168.99.100:30876/fission-function/sizepage')
        print(r.text)
        if r.text:
            r = requests.get('http://192.168.99.100:30876/fission-function/tagpage')
            print(r.text)
main()
