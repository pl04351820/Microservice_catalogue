# This script will triggle multiple serverless function in serilized order.
import requests
import time
def main():
    # The requests will be blocking.
    r = requests.get('http://192.168.99.100:32416/fission-function/frontpage')
    print(r.text)
    if r.text:
        r = requests.get('http://192.168.99.100:32416/fission-function/sizepage')
        print(r.text)
        if r.text:
            r = requests.get('http://192.168.99.100:32416/fission-function/tagpage')
            print(r.text)
main()
