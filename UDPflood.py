import socket
import threading
import time

target_ip = "127.0.0.1"   # ONLY localhost
target_port = 9999

def udp_traffic():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = b"Test Packet"
    
    for _ in range(10000):   # limited packets (safe)
        client.sendto(message, (target_ip, target_port))
        time.sleep(0.001)    # small delay to avoid system crash

# create multiple threads (simulate load)
threads = []
for i in range(20):
    t = threading.Thread(target=udp_traffic)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
